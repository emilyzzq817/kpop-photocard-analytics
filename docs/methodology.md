# Data Cleaning & Parsing Methodology

## Overview

This document describes how raw Mercari sales data is transformed into structured analytics records, with a focus on the NLP-based entity extraction pipeline.

## Raw data schema

The Mercari seller report CSV contains 21 columns per transaction:

| Field | Description | Used in analysis |
|-------|-------------|-----------------|
| Item Id | Unique order ID (m-prefix = individual, b-prefix = bundle) | Yes |
| Sold Date | Date the item was purchased | Yes |
| Completed Date | Date the order was marked complete | Yes |
| Item Title | Free-text listing title | Yes (NLP target) |
| Order Status | Completed or Cancelled | Yes (filter) |
| Shipped to State | Buyer's US state | Yes |
| Item Price | Listing price in USD | Yes |
| Mercari Selling Fee | Platform fee deducted | Yes |
| Net Seller Proceeds | Amount received after all fees | Yes |

## Entity extraction pipeline

### Challenge

Mercari item titles are unstructured, seller-written free text with no standardized format. Examples:

- `"Seventeen jeonghan spill the feels yizhiyu exclusive photocard pc"`
- `"txt ppulbatu yeonjun selfie pc + hwang choon pc offline merch photocard set"`
- `"IVE Liz Love Dive mokket mok photocard"`

The task: extract (group, member) pairs from these titles with high accuracy.

### Approach: keyword matching with taxonomy

We use a two-level lookup:

1. **Group identification**: Match against a curated dictionary of group names and album-specific keywords (e.g., "ppulbatu" uniquely maps to TXT, "spill the feels" to SEVENTEEN)
2. **Member identification**: Given a known group, match against member name aliases within that group's roster
3. **Fallback**: If no group keyword matches, attempt member-name-first lookup and infer the group

### Key design decisions

**Padding for partial match prevention**: All matching operates on ` {title} ` (space-padded) to avoid false positives like "ive" matching inside "dri**ive**r" or "jay" inside "**jay**walk".

**Album keywords as group identifiers**: Many titles omit the group name but include album-specific terms. "Ppulbatu" (TXT), "Cheshire" (ITZY), and "The Action" (BOYNEXTDOOR) are mapped directly to their groups.

**Disambiguation**: Some member names appear in multiple groups (e.g., "Jaehyun" in both BOYNEXTDOOR and NCT, "Jihoon" in both TWS and SEVENTEEN's Woozi). The group-first approach resolves this: we identify the group first, then only search within that group's member roster.

### Results

- **778 total records** (755 completed, 23 cancelled)
- **682 non-bundle completed orders** analyzed for group/member extraction
- **622 / 682 (91.2%)** successfully identified to a group
- **60 unidentified** items (mostly bundles labeled "for [buyer]", niche groups, or non-K-pop items)

### Limitations

1. **Bundle titles** ("Bundle for username") contain no group/member info
2. **Multi-member sets** may only capture the first member mentioned
3. **Emerging groups** not in the taxonomy are missed (fixable by updating config.py)
4. **IVE identification** is tricky because "ive" is a common English word; we use member-name fallback heavily for this group

## Data filtering

- **Cancelled orders** (23, 3.0%): Excluded from all revenue and volume analytics
- **Bundle orders** (73): Included in total revenue counts but excluded from per-group/member analysis (prices are aggregated and don't map to individual items)
- **2026 spillover** (3 orders sold in Jan 2026): Included in monthly trend for completeness

## Reproducibility

All parsing logic lives in `src/parser.py` and `src/config.py`. To add a new group or member, simply update the dictionaries in `config.py` and re-run the pipeline.
