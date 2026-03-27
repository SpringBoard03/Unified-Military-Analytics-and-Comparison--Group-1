# ⚔️ Unified Military Analytics & Comparison (UMAC)

### *Defense insights — collected, processed, visualized.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=flat-square&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Scraping-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)

> **UMAC** is a full-stack analytics platform that compares military strength across 140+ countries using 2025 data—from automated scraping to interactive dashboards.
---

## 📋 Table of Contents

- [Overview](#overview)
- [Workflow](#workflow)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Project Milestones](#milestone-deliverables)
- [Tech Stack](#tech-stack)
- [Contributors](#contributors)
- [License](#license)

---

## 🌍Overview
**UMAC** converts raw defense data into meaningful insights, helping users analyze capabilities, compare nations, and identify global trends.

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

## 🏗️Workflow
```
┌──────────────────────────────────┐
│   Source Data (Defense Metrics)  │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│      Data Extraction Engine      │
│   (Requests + BeautifulSoup)     │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│         Initial Dataset          │
│        raw_military.csv          │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│   Data Transformation & KPIs     │
│        (Pandas + NumPy)          │
│       cleaned_military.csv       │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│        Processed Dataset         │
│        final_military.csv        │
└─────────────────┬────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│        Analytics Dashboard       │
│      Power BI Visual Insights    │
└──────────────────────────────────┘
```
---

## 📁Project Structure

```
Unified-Military-Analytics/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 Milestone_1/              # Data Collection
│   ├── clean_data.ipynb
│   ├── README.md
│   └── data/
│       └── military_raw_data.csv
|       └── military_cleaned.csv
│
├── 📂 Milestone_2/              # Data Processing & KPI Engineering
│   ├── military_final.ipynb
│   ├── README.md
│   └── data/
│       └── military_final.csv
│
├── 📂 Milestone_3/              # Power BI Dashboard
│   ├── Dashboard_1.pdf
│   └── Dashboard_1.pbix
|   └── Dashboard2.pdf
|
└── 📂 Milestone_4/              # Final Report
    └── Final_Project_Report.pdf
```

---

## 🚦Getting Started

### Requirements: Python 3.8+, Power BI
```bash
git clone <repo-link>
cd Unified-Military-Analytics
pip install -r requirements.txt
```

### ▶️ Execution Guide

#### Step 1 — Data Extraction

Run `Milestone_1/Data_Scraping_and_Cleaning.ipynb`

**This will:**
- Collect defense data from online sources  
- Capture manpower, equipment, and budget details  
- Generate → `military_raw_data.csv`

---

#### Step 2 — Data Processing & KPI Creation

Run `Milestone_2/Exploratory_Data_Analysis.ipynb`

**This will:**
- Refine and structure the dataset  
- Handle missing values  
- Create key performance indicators (KPIs)  
- Generate → `military_final.csv`

---

#### Step 3 — Dashboard Setup

Open `Milestone_3/UMAC_Dashboard_2025.pbix` in Power BI Desktop and load `military_final.csv`.

**This will:**
- Build interactive dashboards  
- Enable global military comparison and insights  

---

## 📈Project Milestones

### Milestone 1 — Data Acquisition

> **Goal:** Gather military data for 140+ countries through automated scraping.

- ✔️ Collect personnel statistics  
- ✔️ Capture equipment data (air, land, sea)  
- ✔️ Retrieve defense spending details  
- 📁 **Output:** `military_raw_data.csv`

---

### Milestone 2 — Data Processing & KPI Development

> **Goal:** Convert raw data into meaningful analytical insights.

| Metric | Description |
|---|---|
| Rank Difference Index | Gap from global average ranking |
| Assets per Population | Military resources per capita |
| Defense Spending Ratio | % of GDP allocated to defense |
| Equipment Capability Score | Overall strength based on assets |

📁 **Output:** `military_final.csv`

---

### Milestone 3 — Dashboard Development

> **Goal:** Design an interactive visualization system.

- 🌐 Worldwide military ranking map  
- 🔎 Country-to-country comparison  
- 🌍 Region-based filters & drilldowns  
- 📉 Visual analysis of assets & manpower  

---

### Milestone 4 — Documentation

> **Goal:** Summarize approach, analysis, and insights.

📄 **Output:** `Final_Project_Report.pdf`

---

## 🧩Tech Stack

| Category | Tools & Technologies |
|---|---|
| Data Extraction | 🐍 Python, 🌐 Requests, 🥣 BeautifulSoup |
| Data Analysis | 🐼 Pandas, 🔢 NumPy |
| Visualization | 📈 Power BI |
| Development | 📒 Jupyter Notebook |
| Documentation | ✍️ Markdown, 🐙 GitHub |

---

## 👥Contributors

**Group 16** — Unified Military Analytics & Comparison Project

*Developed as part of the SpringBoard03 academic initiative.*

---

## 📄License

This project is developed for **academic and research purposes only**.

---

*Built for global defense analytics · UMAC 2025*
