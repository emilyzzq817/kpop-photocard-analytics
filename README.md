# K-pop Photocard Resale Market Analytics

An end-to-end data analysis project exploring the economics of my K-pop photocard reselling on Mercari, based on 755 completed transactions across 22 groups in 2025.

## Key findings

- **$12,268** gross revenue from 755 completed sales, with **$10,893** net after fees
- **IVE** leads in revenue ($1,628) while **TXT** leads in volume (86 items)
- Strong seasonality: Sep-Nov accounted for **51%** of annual revenue
- Member pricing varies dramatically within groups (e.g., SEVENTEEN Hoshi avg $28 vs Woozi avg $4.50)
- California alone represents **22%** of all buyers
- Mercari's effective fee rate is **10.9%**, leaving sellers with 88.8% take-home

## Project structure

```
kpop-photocard-analytics/
├── data/                    # Raw sales data
│   └── sales-report.csv
├── src/
│   ├── parser.py            # NLP-based group/member extraction from item titles
│   ├── analyzer.py          # Core analytics functions
│   └── config.py            # Group/member taxonomy
├── notebooks/
│   └── analysis.ipynb       # Full exploratory data analysis
├── outputs/
│   ├── dashboard_data.json  # Processed analytics data
│   └── parsed_records.json  # Parsed transaction records
├── docs/
│   └── methodology.md       # Data cleaning & parsing methodology
├── dashboard.html           # Interactive analytics dashboard
├── requirements.txt
└── README.md
```

## Analysis dimensions

### 1. Group & member value analysis
- Revenue ranking by group (total and per-item average)
- Member-level pricing within each group
- "Premium member" identification (members whose cards consistently sell above group average)

### 2. Seasonality & trends
- Monthly sales volume and revenue trends
- Correlation with K-pop comeback calendars
- Identification of peak selling windows

### 3. Buyer geography
- US state-level heatmap of buyer distribution
- Regional price sensitivity analysis
- Potential correlation with Asian-American population density

### 4. Pricing strategy
- Price distribution analysis across tiers ($0-5, $5-10, etc.)
- Bundle vs. individual item pricing comparison
- Mercari fee impact on effective margins

### 5. Fulfillment efficiency
- Order-to-completion time distribution
- Trends in fulfillment speed over time

## Tech stack

- **Python**: pandas, numpy for data processing
- **NLP**: Custom regex-based entity extraction for group/member identification from unstructured item titles
- **Visualization**: matplotlib, seaborn, plotly for static charts; Chart.js + D3.js for interactive dashboard
- **Dashboard**: Vanilla HTML/JS with Chart.js and D3.js choropleth map

## Getting started

```bash
pip install -r requirements.txt
cd notebooks
jupyter notebook analysis.ipynb
```

Or open `dashboard.html` in your browser for the interactive dashboard.

## Data notes

- Raw data exported from Mercari seller dashboard (Jan-Dec 2025)
- Group/member identification achieved 91.2% accuracy via NLP parsing of item titles
- Bundle orders are included in total revenue but excluded from per-group/member analysis
- 23 cancelled orders (3.0% cancellation rate) are excluded from completed analytics

## License

This project is for portfolio/educational purposes. Raw sales data has been anonymized (no buyer identifiers).
