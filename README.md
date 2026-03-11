# 🌐 Unified Military Analytics and Comparison Dashboard

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=flat-square&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Scraping-4B8BBE?style=flat-square)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow?logo=powerbi&logoColor=black)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
---

Unified Military Analytics & Comparison Dashboard shows the military strength of countries in an easy-to-understand way, It uses data to create dashboards that let you compare countries and see key statistics.

## 🎯 Project Statement
This project develops a **fully interactive dashboard suite** for analyzing **global military power**.  

- Military metrics for **140+ countries** are scraped from **GlobalFirepower.com**.  
- Python pipelines are used to **scrape, clean, and process** defense data.  
- Dashboards are **cross-platform**: deployable in **Power BI, Tableau, or Python-based apps** (Streamlit/Dash).  
- Covers **50+ defense & economic indicators** across four modules:

| Module | Description |
|--------|-------------|
| **Quick Stats 📊** | Global overview with rankings, trends, KPIs |
| **Nation Overview 🏛️** | Detailed country-level metrics |
| **Compare Powers ⚔️** | Side-by-side country comparison |
| **Coalition Builder 🤝** | Interactive simulation of alliances |

**KPIs include:** Power Index Rank Gap, Assets per Capita, Defense Budget-to-GDP Ratio.

---

## ⚙️ Approach
1. **Data Collection & Preparation** – Scrape and clean data; handle missing values.  
2. **KPI Engineering** – Compute derived metrics; enrich with region, continent, and alliance data.  
3. **Dashboard Development** – Build interactive **Power BI dashboards** with filters, tooltips, and KPI cards.  

---

## 🏗️ Architecture
```mermaid
graph LR
    %% Layout Configuration
    %% This makes nodes closer together
    
    subgraph Acquisition [Acquisition]
    A["🌐 Web Data"] --> B{{"🐍 Scraper"}}
    end

    subgraph Processing [Processing]
    B --> C[("📂 Raw CSV")]
    C --> D["🧹 Cleaning"]
    D --> E[("📊 Final CSV")]
    end

    subgraph Insights [Insights]
    E --> F["🚀 Dashboard"]
    end

    %% Visual Styling
    style A fill:#E1F5FE,stroke:#01579B,stroke-width:1px,color:#01579B
    style B fill:#E8EAF6,stroke:#1A237E,stroke-width:1px,color:#1A237E
    style C fill:#ECEFF1,stroke:#263238,stroke-width:1px,color:#263238
    style D fill:#E8F5E9,stroke:#1B5E20,stroke-width:1px,color:#1B5E20
    style E fill:#FFFDE7,stroke:#F57F17,stroke-width:1px,color:#F57F17
    style F fill:#FFF3E0,stroke:#E65100,stroke-width:2px,font-weight:bold,color:#E65100

    %% Container Styling
    classDef cluster stroke:#ccc,stroke-dasharray: 5 5,fill:transparent;
```

## 📂 Repository Structure

```
Unified Military Analytics and Comparison Dashboard
│
├── 📄 README.md
│
├── 📂 milestone_01             
│   ├── Milestone_01_Data_Preprocessing.ipynb
│   ├── README.md
│   └── data/
│       └── military_raw_data.csv
|       └── military_clean_data.csv
│
├── 📂 milestone_02             
│   ├── Milestone_02_KPI_Engineering.ipynb
│   ├── README.md
│   └── data/
│       └── military_updated.csv
```
---

## 🗓️ Milestones

### 📍 Milestone 01: Data Collection & Preparation
> **Goal:** Build a robust data pipeline that extracts raw military intelligence from the web and transforms it into a high-quality, analysis-ready dataset.


| Module | Focus | Primary Tools |
| :--- | :--- | :--- |
| **01. Scraping** | Web Extraction & Raw Storage | `BeautifulSoup`, `Requests` |
| **02. Cleaning** | Type Conversion & Normalization | `Pandas`, `NumPy` |


| 🧩 Scraping | 🧹 Cleaning |
| :--- | :--- |
| **Action:** Extracted 60+ metrics for 140+ nations. | **Action:** Stripped symbols (%, +) & handled nulls. |
| **Tech:** `BeautifulSoup` + `Requests` | **Tech:** `Pandas` + `NumPy` |
| **Output:** `military_raw_data.csv` | **Output:** `military_cleaned.csv` |

---

### 📍 Milestone 02: KPI Engineering & Prototyping
> **Goal:** Transform raw numbers into strategic military intelligence through custom feature engineering and UI/UX design.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#004a99', 'primaryTextColor': '#ffffff', 'lineColor': '#ffffff'}, 'block': {'padding': 10}}}%%
block-beta
  columns 2
  
  k1["📈 <b>Power Index Rank Gap</b>"]
  k2["👥 <b>Assets per Capita</b>"]
  k3["💰 <b>Budget-to-GDP Ratio</b>"]
  k4["🌍 <b>Alliance Flags (NATO)</b>"]
  k5["📍 <b>Regional Mapping</b>"]
  k6["🗺️ <b>Continental Metadata</b>"]

  %% Styling for White Font and Professional Blue
  style k1 fill:#004a99,stroke:#ffffff,color:#ffffff
  style k2 fill:#004a99,stroke:#ffffff,color:#ffffff
  style k3 fill:#004a99,stroke:#ffffff,color:#ffffff
  style k4 fill:#004a99,stroke:#ffffff,color:#ffffff
  style k5 fill:#004a99,stroke:#ffffff,color:#ffffff
  style k6 fill:#004a99,stroke:#ffffff,color:#ffffff
```


| 🧪 **KPI Engineering** | 🎨 **Prototyping** |
| :--- | :--- |
| **Focus:** Metric Derivation & Metadata | **Focus:** Wireframing & UX Planning |
| **Action:** Calculated Power Gap, Assets/Capita, & Budget/GDP ratio. | **Action:** Drafted layouts for Quick Stats & Nation Overview. |
| **Tech:** `Power BI` | **Tech:** `Figma` / `Sketch` |
| **Output:** `military_final.csv` | **Output:** Dashboard Storyboard |
