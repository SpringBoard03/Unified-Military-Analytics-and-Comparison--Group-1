# 🌐 UMAC — Unified Military Analytics & Comparison

### 🌍 Global Defense Intelligence — Automated • Analyzed • Visualized

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=flat-square&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Scraping-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)

> **UMAC** is an end-to-end military analytics platform designed to evaluate and compare the defense capabilities of **140+ countries** using recent global defense data.  
It covers the complete pipeline — from automated web scraping and KPI engineering to interactive **Power BI dashboards** for strategic insights.

---

## 📋 Table of Contents

- Overview  
- Architecture  
- Project Structure  
- Getting Started  
- Project Outputs 
- Technology Stack  
- Contributors  

---

## 🌐 Overview

**Unified Military Analytics & Comparison (UMAC)** enables analysts and researchers to explore global military strength, perform country comparisons, and uncover strategic defense trends using structured analytical datasets.

The project dataset includes **50+ military indicators** across major categories:

| Category | Indicators |
|----------|-----------|
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
├── 📂 Milestone_1/              # Data Collection
│   ├── Data_Scraping_and_Cleaning.ipynb
│   ├── README.md
│   └── data/
│       └── military_raw_data.csv
|       └── military_clean_data.csv
│
├── 📂 Milestone_2/              # Data Processing & KPI Engineering
│   ├── Exploratory_Data_Analysis.ipynb
│   ├── README.md
│   └── data/
│       └── military_final.csv
|       └── military_clean_data.csv
│
├── 📂 Milestone_3/              # Power BI Dashboard
│   ├── UMAC_Dashboard_2025.pbix
│   └── README.md
│
└── 📂 Milestone_4/              # Final Report
    └── Final_Project_Report.pdf
```
---

## 🚀 Getting Started

### ✅ Prerequisites
- Python `3.8+`
- Power BI Desktop

---

## 🚀 How to Run the Project

### Step 1 — Generate Raw Dataset
Execute the data scraping notebook to collect military indicators.

### Step 2 — Prepare Analytical Dataset
Run the processing notebook to clean data and engineer KPIs.

### Step 3 — Explore Visual Insights
Open the Power BI dashboard file and load the final dataset.

---

## 📦 Project Outputs

| Stage | Result |
|------|--------|
| Data Collection | Raw military dataset |
| Data Processing | Analytics-ready dataset |
| Visualization | Interactive comparison dashboard |
| Documentation | Final project report |

---

## 👥 Contributors

**Group 1** — Unified Military Analytics & Comparison Project

*Developed as part of the SpringBoard03 academic initiative.*

---

## 📄 License

This project is developed for **academic and research purposes only**.

---

*Built for global defense analytics · UMAC 2025*
