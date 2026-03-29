# Unified Military Analytics & Comparison Dashboard

## Project Overview

This project delivers a comprehensive analytics platform for global military intelligence. The system extracts, processes, and visualizes defense data for 145 countries, enabling strategic analysis through interactive dashboards.

**Dataset Coverage:** 145 Countries | 50+ Metrics | 4 Dashboard Modules

---

## Technical Architecture

The project is structured into four sequential milestones:

| Milestone | Focus | Output |
|-----------|-------|--------|
| 01 | Data Collection & Preparation | Cleaned dataset (34 metrics) |
| 02 | KPI Engineering & Feature Creation | Enriched dataset with KPIs (42 metrics) |
| 03 | Dashboard Development | Interactive Power BI dashboard |
| 04 | Final Documentation | Comprehensive project report |

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Web Scraping | Python, Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy, Regex |
| Visualization | Power BI, Matplotlib, Seaborn, Plotly |
| Environment | Jupyter Notebook, Python 3.10 |

---

## Repository Structure
MILITARY_SCRAPER/

├── milestone_01/ # Data Collection & Cleaning
├── milestone_02/ # KPI Engineering & Feature Creation
├── milestone_03/ # Dashboard Development
├── milestone_04/ # Final Documentation
├── LICENSE # MIT License
└── README.md # Project documentation

---

## Data Pipeline

| Stage | Actions |
|-------|---------|
| **Acquisition** | Web Scraping → 145 Countries → 50+ Metrics |
| **Processing** | Data Cleaning → Standardize → Validate |
| **Analytics** | KPI Engine → Dashboard → Insights |

---

## Dataset Specifications

| Attribute | Value |
|-----------|-------|
| Countries Covered | 145 |
| Raw Metrics | 34 |
| Final Metrics (with KPIs) | 42 |
| Data Source | GlobalFirepower.com |
| Coverage | Military, Economic, Geographic |

---

## Key Performance Indicators

| KPI | Formula | Strategic Insight |
|-----|---------|-------------------|
| Assets per Capita | (Aircraft + Tanks + Naval) / Manpower | Equipment density per soldier |
| Budget-to-GDP Ratio | Defense Budget / GDP | Defense spending priority |
| Power Index Rank | Rank of Power Index | Relative military strength |
| Power Index Rank Gap | Rank - 1 | Distance from top military power |

---

## Quick Statistics

| Metric | Value |
|--------|-------|
| Total Defense Spending (Global) | $2.86 Trillion |
| Total Military Manpower | 3.74 Billion |
| Average Power Index | 1.64 |
| NATO Members | 32 |
| Non-Aligned Nations | 113 |

---

## Top 5 Military Powers

| Rank | Country | Power Index | Defense Budget |
|------|---------|-------------|----------------|
| 1 | United States | 0.0741 | $831.5B |
| 2 | Russia | 0.0791 | $212.6B |
| 3 | China | 0.0919 | $303.0B |
| 4 | India | 0.1346 | $109.0B |
| 5 | South Korea | 0.1642 | $44.8B |

---

## Execution Instructions

```bash
# Install dependencies
pip install pandas numpy beautifulsoup4 requests matplotlib seaborn plotly jupyter

# Execute Milestone 01 - Data Collection
jupyter notebook milestone_01/Milestone_01_Data_Preprocessing.ipynb

# Execute Milestone 02 - KPI Engineering
jupyter notebook milestone_02/Milestone_02_KPI_Engineering.ipynb

# Execute Milestone 03 - Dashboard Development
jupyter notebook milestone_03/Milestone_03_Dashboard_Development.ipynb
