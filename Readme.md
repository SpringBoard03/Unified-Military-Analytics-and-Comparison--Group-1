# 🛡️ Unified Military Analytics & Comparison (UMAC)

### *Global defense intelligence — automated, analyzed, visualized.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=flat-square&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Scraping-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)

> **UMAC** is a full-stack data analytics platform that evaluates and compares the military capabilities of **140+ countries** using live 2025 defense data — from automated web scraping to interactive Power BI dashboards.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Milestone Deliverables](#milestone-deliverables)
- [Technology Stack](#technology-stack)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)

---

## 🌐 Overview

**UMAC (Unified Military Analytics and Comparison)** automates the full pipeline from raw web data collection to interactive Power BI dashboards, enabling analysts to examine global defense capabilities, compare countries, and uncover strategic military trends.

The dataset spans **140+ countries** and includes more than **50 defense indicators**:

| Category | Indicators |
|---|---|
| 👥 Manpower | Active personnel, reserves, paramilitary |
| ✈️ Air Power | Fighter jets, helicopters, transport aircraft |
| 🚢 Naval Power | Warships, submarines, patrol vessels |
| 🚗 Land Forces | Tanks, armored vehicles, artillery |
| 💰 Economics | Defense budgets, GDP ratios, spending per capita |
| 🏆 Rankings | Global power index, regional standings |

---

## 🏗️ Architecture

```
┌──────────────────────────────────┐
│  Raw Web Data (Global Firepower)  │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│        Python Web Scraper         │
│    (BeautifulSoup + Requests)     │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│           Raw Dataset             │
│       military_raw_data.csv       │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│  Data Cleaning & KPI Engineering  │
│         (Pandas + NumPy)          |
    military_clean_data.csv         │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│           Final Dataset           │
│        military_final.csv         │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│        Power BI Dashboard         │
│   Interactive Military Analytics  │
└──────────────────────────────────┘
```

---

## 📁 Project Structure

```
Unified-Military-Analytics/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 Milestone 1/              # Data Collection
│   ├── Data_Scraping_and_Cleaning.ipynb
│   ├── Quick Stats.pbix
│   ├── Readme.md
│   └── data/
│       ├── military_raw_data.csv
│       └── military_clean_data.csv
│
├── 📂 Milestone 2/              # Data Processing & KPI Engineering
│   ├── Exploratory_Data_Analysis.ipynb
│   ├── Nation Overview.pbix
│   ├── Readme.md
│   └── data/
│       ├── military_final.csv
│       └── military_clean_data.csv
│
├── 📂 Milestone 3/              # Power BI Dashboard (Compare Powers)
│   ├── Compare Powers.pbix
│   ├── Compare Powers.pdf
│   └── Readme.md
│
└── 📂 Milestone 4/              # Power BI Dashboard (Coalition Builder)
    ├── Coalition Builder.pbix
    ├── Coalition Builder.pdf
    └── Readme.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python `3.8+`
- Power BI Desktop

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/SpringBoard03/Unified-Military-Analytics-and-Comparison--Group-1.git
cd Unified-Military-Analytics-and-Comparison--Group-1
```

**2. Install dependencies**

```bash
pip install pandas beautifulsoup4 requests numpy
```

---

### ▶️ Running the Project

#### Step 1 — Data Collection

Run `Milestone_1/Data_Scraping_and_Cleaning.ipynb`

This notebook will:
- Scrape military data from web sources
- Extract manpower, equipment, and budget statistics
- Output → `military_raw_data.csv`

---

#### Step 2 — Data Processing & KPI Engineering

Run `Milestone_2/Exploratory_Data_Analysis.ipynb`

This notebook will:
- Clean the raw dataset
- Handle missing values
- Engineer analytical KPIs
- Output → `military_final.csv`

---

#### Step 3 — Dashboard Visualization

Open the respective `.pbix` files (`Quick Stats.pbix`, `Nation Overview.pbix`, `Compare Powers.pbix`, `Coalition Builder.pbix`) in Power BI Desktop from their milestone folders, then ensure the datasets are correctly linked.

Power BI will generate interactive dashboards for global military comparison.

---

## 📊 Milestone Deliverables

### Milestone 1 — Data Collection

> **Objective:** Automate scraping of military metrics for 140+ countries.

- ✅ Extract manpower data
- ✅ Extract equipment counts (air, land, naval)
- ✅ Extract defense budgets
- 📦 **Output:** `military_raw_data.csv`

---

### Milestone 2 — Data Processing & KPI Engineering

> **Objective:** Transform raw data into actionable analytical metrics.

| KPI | Description |
|---|---|
| Power Index Rank Gap | Deviation from global average rank |
| Assets per Capita | Military assets normalized by population |
| Budget to GDP Ratio | Defense spending as % of national GDP |
| Equipment Strength Index | Composite score of hardware capability |

📦 **Output:** `military_final.csv`

---

### Milestone 3 — Power BI Dashboard

> **Objective:** Build an interactive analytics dashboard.

- 🗺️ Global military rankings map
- 🔍 Side-by-side country comparison
- 🌏 Regional filtering & drill-down
- 📊 Equipment and manpower visualizations

---

### Milestone 4 — Final Report

> **Objective:** Document findings, methodology, and insights.

📄 **Output:** `Final_Project_Report.pdf`

---

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| Data Collection | 🐍 Python, 🌐 Requests, 🍲 BeautifulSoup4 |
| Data Processing | 🐼 Pandas, 🔢 NumPy |
| Visualization | 📊 Power BI |
| Notebooks | 📓 Jupyter |
| Documentation | 📝 Markdown, 🐙 GitHub |

---

## 🔧 Troubleshooting

**`ModuleNotFoundError` — Missing Python packages**

```bash
pip install -r requirements.txt
```

**Power BI cannot load the dataset**

- Confirm `military_final.csv` exists in the correct path
- Ensure column headers have **not** been modified
- Verify file encoding is **UTF-8**

---

## 👥 Contributors

**Group 1** — Unified Military Analytics & Comparison Project

*Developed as part of the SpringBoard03 academic initiative.*

---

## 📄 License

This project is developed for **academic and research purposes only**.

---

*Built for global defense analytics · UMAC 2025*
