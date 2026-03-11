# 🌐 Unified Military Analytics and Comparison Dashboard

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow?logo=powerbi&logoColor=black)
---

## 🎯 Project Statement
This project develops a **fully interactive dashboard suite** for analyzing **global military power**.  

- Military metrics for **140+ countries** are scraped from **GlobalFirepower.com**.  
- Python pipelines are used to **scrape, clean, and process** defense data.  
- Dashboards are **cross-platform**: deployable in **Power BI, Tableau, or Python-based apps** (Streamlit/Dash).  
- Covers **50+ defense & economic indicators** across four modules:

| Module | Description |
|--------|-------------|
| **Quick Stats** | Global overview with rankings, trends, KPIs |
| **Nation Overview** | Detailed country-level metrics |
| **Compare Powers** | Side-by-side country comparison |
| **Coalition Builder** | Interactive simulation of alliances |

**KPIs include:** Power Index Rank Gap, Assets per Capita, Defense Budget-to-GDP Ratio.

---

## ⚙️ Approach
1. **Data Collection & Preparation** – Scrape and clean data; handle missing values.  
2. **KPI Engineering** – Compute derived metrics; enrich with region, continent, and alliance data.  
3. **Dashboard Development** – Build interactive **Power BI dashboards** with filters, tooltips, and KPI cards.  

---

## 📂 Repository Structure

```text
Unified Military Analytics and Comparison Dashboard/
│
├─ Milestone_01/                # Data Acquisition & Cleaning
│  ├─ data/                     # Cleaned dataset (CSV)
│  └─ notebooks/                # Data preprocessing scripts
└─ README.md                    # Project documentation
│
├─ Milestone_02/                # Feature Engineering
│  ├─ data/                     # Updated dataset with new metrics
│  └─ notebooks/                # KPI calculations and logic
└─ README.md                    # Project documentation
```
