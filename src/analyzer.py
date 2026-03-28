"""
Core analytics functions for K-pop photocard sales data.
"""

import csv
from datetime import datetime
from collections import defaultdict, Counter
from typing import List, Dict, Any, Optional

from .parser import parse_title, extract_item_type
from .config import GROUP_GENERATION, GROUP_COMPANY


def load_data(filepath: str) -> List[Dict[str, Any]]:
    """Load and parse the Mercari sales CSV into structured records."""
    records = []
    
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            item_id = row["Item Id"]
            if item_id in ("Totals:", "") or item_id.startswith("Report"):
                continue
            
            group, member = parse_title(row["Item Title"])
            item_type = extract_item_type(row["Item Title"])
            
            sold_date = row["Sold Date"]
            try:
                sold_dt = datetime.strptime(sold_date, "%m/%d/%Y")
                month = sold_dt.strftime("%Y-%m")
            except ValueError:
                sold_dt = None
                month = None
            
            completed_date = row.get("Completed Date", "")
            try:
                comp_dt = datetime.strptime(completed_date, "%m/%d/%Y")
                fulfillment_days = (comp_dt - sold_dt).days if sold_dt else None
            except (ValueError, TypeError):
                fulfillment_days = None
            
            records.append({
                "item_id": item_id,
                "title": row["Item Title"],
                "status": row["Order Status"],
                "group": group,
                "member": member,
                "item_type": item_type,
                "is_bundle": item_id.startswith("b"),
                "price": float(row["Item Price"]),
                "buyer_state": row["Shipped to State"],
                "mercari_fee": float(row["Mercari Selling Fee"]),
                "net_proceeds": float(row["Net Seller Proceeds"]),
                "sold_date": sold_date,
                "sold_dt": sold_dt,
                "month": month,
                "fulfillment_days": fulfillment_days,
            })
    
    return records


def get_completed(records: List[Dict]) -> List[Dict]:
    """Filter to completed orders only."""
    return [r for r in records if r["status"] == "Completed"]


def get_non_bundles(records: List[Dict]) -> List[Dict]:
    """Filter out bundle orders."""
    return [r for r in records if not r["is_bundle"]]


def group_stats(records: List[Dict]) -> Dict[str, Dict]:
    """Calculate per-group statistics."""
    stats = defaultdict(lambda: {"count": 0, "total": 0, "prices": []})
    
    for r in records:
        if r["group"]:
            g = r["group"]
            stats[g]["count"] += 1
            stats[g]["total"] += r["price"]
            stats[g]["prices"].append(r["price"])
    
    result = {}
    for g in sorted(stats, key=lambda x: stats[x]["total"], reverse=True):
        s = stats[g]
        result[g] = {
            "count": s["count"],
            "total_revenue": round(s["total"], 2),
            "avg_price": round(s["total"] / s["count"], 2),
            "min_price": round(min(s["prices"]), 2),
            "max_price": round(max(s["prices"]), 2),
            "median_price": round(sorted(s["prices"])[len(s["prices"]) // 2], 2),
        }
    
    return result


def member_stats(records: List[Dict], group: str) -> Dict[str, Dict]:
    """Calculate per-member statistics for a given group."""
    stats = defaultdict(lambda: {"count": 0, "total": 0, "prices": []})
    
    for r in records:
        if r["group"] == group and r["member"]:
            m = r["member"]
            stats[m]["count"] += 1
            stats[m]["total"] += r["price"]
            stats[m]["prices"].append(r["price"])
    
    result = {}
    for m in sorted(stats, key=lambda x: stats[x]["total"], reverse=True):
        s = stats[m]
        result[m] = {
            "count": s["count"],
            "total_revenue": round(s["total"], 2),
            "avg_price": round(s["total"] / s["count"], 2),
            "min_price": round(min(s["prices"]), 2),
            "max_price": round(max(s["prices"]), 2),
        }
    
    return result


def monthly_trend(records: List[Dict]) -> Dict[str, Dict]:
    """Calculate monthly sales trends."""
    stats = defaultdict(lambda: {"count": 0, "revenue": 0})
    
    for r in records:
        if r["month"]:
            stats[r["month"]]["count"] += 1
            stats[r["month"]]["revenue"] += r["price"]
    
    return {
        m: {"count": s["count"], "revenue": round(s["revenue"], 2)}
        for m, s in sorted(stats.items())
    }


def geography_stats(records: List[Dict]) -> Dict[str, Dict]:
    """Calculate buyer geography statistics."""
    stats = defaultdict(lambda: {"count": 0, "revenue": 0, "groups": Counter()})
    
    for r in records:
        s = r["buyer_state"]
        stats[s]["count"] += 1
        stats[s]["revenue"] += r["price"]
        if r["group"]:
            stats[s]["groups"][r["group"]] += 1
    
    return {
        state: {
            "count": s["count"],
            "revenue": round(s["revenue"], 2),
            "avg_price": round(s["revenue"] / s["count"], 2),
            "top_groups": dict(s["groups"].most_common(3)),
        }
        for state, s in sorted(stats.items(), key=lambda x: x[1]["count"], reverse=True)
    }


def fee_analysis(records: List[Dict]) -> Dict[str, float]:
    """Analyze Mercari fee impact."""
    total_price = sum(r["price"] for r in records)
    total_fee = sum(r["mercari_fee"] for r in records)
    total_net = sum(r["net_proceeds"] for r in records)
    
    return {
        "total_item_price": round(total_price, 2),
        "total_mercari_fee": round(total_fee, 2),
        "total_net_proceeds": round(total_net, 2),
        "fee_rate_pct": round(total_fee / total_price * 100, 2) if total_price > 0 else 0,
        "net_rate_pct": round(total_net / total_price * 100, 2) if total_price > 0 else 0,
    }


def company_analysis(records: List[Dict]) -> Dict[str, Dict]:
    """Analyze sales by entertainment company."""
    company_lookup = {}
    for company, groups in GROUP_COMPANY.items():
        for g in groups:
            company_lookup[g] = company
    
    stats = defaultdict(lambda: {"count": 0, "revenue": 0, "groups": Counter()})
    
    for r in records:
        if r["group"]:
            company = company_lookup.get(r["group"], "Other")
            stats[company]["count"] += 1
            stats[company]["revenue"] += r["price"]
            stats[company]["groups"][r["group"]] += 1
    
    return {
        c: {
            "count": s["count"],
            "revenue": round(s["revenue"], 2),
            "avg_price": round(s["revenue"] / s["count"], 2),
            "groups": dict(s["groups"].most_common()),
        }
        for c, s in sorted(stats.items(), key=lambda x: x[1]["revenue"], reverse=True)
    }
