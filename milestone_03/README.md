# Milestone 03: Power BI Dashboard

## Dashboard Overview

This interactive Power BI dashboard transforms military intelligence data into actionable insights through four interconnected modules. Built on the cleaned dataset from Milestone 01 and enriched KPIs from Milestone 02, the dashboard enables comprehensive analysis of global military power.

**Data Source:** 145 Countries | 42 Metrics | 2025 Data

---

## Dashboard Modules

### 1. Quick Stats
**Purpose:** Global overview of military power

| Feature | Description |
|---------|-------------|
| KPI Cards | Total defense spending, manpower, average power index, NATO stats |
| Top 10 Rankings | Countries by Power Index (lower = stronger) |
| Regional Analysis | Defense spending distribution by continent |
| Interactive Filters | Filter by continent, region, or alliance |

### 2. Nation Overview
**Purpose:** Deep-dive analysis of individual countries

| Feature | Description |
|---------|-------------|
| Country Selector | Dropdown to select any of 145 countries |
| Complete Profile | All 42 metrics displayed in organized sections |
| Radar Chart | Visual comparison of military capabilities |
| Category Breakdown | Air Power, Land Power, Naval Power, Economic metrics |

### 3. Compare Powers
**Purpose:** Side-by-side comparison of any two nations

| Feature | Description |
|---------|-------------|
| Country Selection | Choose any two countries for comparison |
| Comparison Table | 12 key metrics displayed side-by-side |
| Visual Charts | Bar charts for defense budget, manpower, aircraft, tanks |
| Winner Indicator | Highlights which country leads in each category |

### 4. Coalition Builder
**Purpose:** Alliance simulation and combined strength analysis

| Feature | Description |
|---------|-------------|
| NATO Analysis | Complete breakdown of NATO vs Non-NATO |
| Custom Coalitions | Build your own alliance by selecting countries |
| Combined Strength | Total defense budget, manpower, aircraft, tanks |
| Comparison | Compare custom coalition against NATO or any reference |

---

## File Structure
milestone_03/
├── UMAC_Dashboard_2025.pbix # Power BI dashboard file
├── README.md # This documentation
├── quick_stats.png
├── nation_overview.png
├── compare_powers.png
└── coalition_builder.png

---

## How to Use

### Prerequisites
- Power BI Desktop (free download from Microsoft)
- Windows 10/11 or Power BI Service (cloud)

### Steps to Open

1. **Download Power BI Desktop**
   - Visit: https://powerbi.microsoft.com/en-us/downloads/
   - Download and install Power BI Desktop

2. **Open the Dashboard**
   - Double-click `UMAC_Dashboard_2025.pbix`
   - Power BI Desktop will open with all 4 pages

3. **Refresh Data (if needed)**
   - Click **Home** → **Refresh**
   - Ensure `military_final.csv` is in the correct location

4. **Navigate Pages**
   - Use tabs at the bottom to switch between 4 dashboard modules

---

## Dashboard Navigation

| Page | Navigation | Key Actions |
|------|------------|-------------|
| Quick Stats | First tab | Use filters (continent, alliance) to explore |
| Nation Overview | Second tab | Select country from dropdown |
| Compare Powers | Third tab | Select two countries from slicers |
| Coalition Builder | Fourth tab | Toggle NATO/Non-NATO or build custom coalition |

---

## Key Insights from Dashboard

### Military Power Rankings
| Rank | Country | Power Index | Defense Budget |
|------|---------|-------------|----------------|
| 1 | United States | 0.0741 | $831.5B |
| 2 | Russia | 0.0791 | $212.6B |
| 3 | China | 0.0919 | $303.0B |
| 4 | India | 0.1346 | $109.0B |
| 5 | South Korea | 0.1642 | $44.8B |

### Alliance Analysis
| Alliance | Countries | Defense Budget | Manpower |
|----------|-----------|----------------|----------|
| NATO | 32 | $1.50 Trillion | 447 Million |
| Non-Aligned | 113 | $1.36 Trillion | 3.30 Billion |

### Regional Distribution
| Continent | Countries | Defense Budget | Manpower |
|-----------|-----------|----------------|----------|
| Asia | 41 | $853 Billion | 2.32 Billion |
| Europe | 38 | $843 Billion | 339 Million |
| North America | 10 | $895 Billion | 260 Million |
| Africa | 35 | $110 Billion | 562 Million |
| South America | 11 | $64 Billion | 217 Million |

---

## KPIs Featured in Dashboard

| KPI | Definition | Insight |
|-----|------------|---------|
| **Assets per Capita** | (Aircraft + Tanks + Naval) ÷ Manpower | Technology intensity of military |
| **Budget-to-GDP Ratio** | Defense Budget ÷ GDP | National defense priority |
| **Power Index Rank** | Rank of Power Index | Global military positioning |
| **Power Index Rank Gap** | Rank − 1 | Distance from top military power |

---

## Data Sources

| File | Source | Description |
|------|--------|-------------|
| `military_final.csv` | Milestone 02 | Final dataset with all KPIs and metadata |
| `military_clean_data.csv` | Milestone 01 | Cleaned raw data (backup) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Dashboard doesn't open | Ensure Power BI Desktop is installed |
| Data not loading | Check file path to `military_final.csv` |
| Filters not working | Click "Reset to default" in filter pane |
| Slow performance | Reduce data load or use aggregated views |

---

## Future Enhancements

- Add historical data for trend analysis
- Incorporate equipment quality scores (Gen 4 vs Gen 5 fighters)
- Add geospatial maps for geographic visualization
- Real-time data refresh from GlobalFirepower.com

---

## Last Updated

March 2026