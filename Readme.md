# 🛡️ Unified Military Analytics & Comparison (UMAC)

### *Automated global defense intelligence — from raw data to interactive insights.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=flat-square\&logo=powerbi\&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat-square\&logo=pandas\&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)

> **UMAC (Unified Military Analytics & Comparison)** is a data analytics project designed to analyze and compare the military strength of **140+ nations**.
> The project builds a complete pipeline — starting from automated web scraping to advanced KPI analysis and interactive **Power BI dashboards**.

---

# 📑 Table of Contents

* Project Overview
* System Architecture
* Repository Structure
* Setup Guide
* Project Milestones
* Technology Stack
* Troubleshooting
* Contributors

---

# 🌍 Project Overview

**UMAC** provides a data-driven perspective on global defense capabilities by collecting, processing, and visualizing military statistics.

The dataset includes **50+ defense indicators** across **140+ countries**, covering multiple strategic categories.

| Category            | Examples                                          |
| ------------------- | ------------------------------------------------- |
| 👥 Manpower         | Active personnel, reserves, paramilitary forces   |
| ✈️ Air Power        | Fighter aircraft, helicopters, transport aircraft |
| 🚢 Naval Strength   | Warships, submarines, patrol vessels              |
| 🚗 Land Systems     | Tanks, armored vehicles, artillery                |
| 💰 Economic Metrics | Defense spending, GDP ratios                      |
| 🏆 Rankings         | Global power index and rankings                   |

This platform allows analysts to explore military capabilities, compare countries, and discover global strategic trends.

---

# 🏗️ System Architecture

```
Global Firepower Website
        │
        ▼
Python Web Scraper
(Requests + BeautifulSoup)
        │
        ▼
Raw Dataset Generated
military_raw_data.csv
        │
        ▼
Data Cleaning & Transformation
(Pandas Processing)
military_clean_data.csv
        │
        ▼
KPI Engineering & Feature Creation
military_final.csv
        │
        ▼
Interactive Power BI Dashboard
Military Analytics Visualization
```

---

# 📁 Repository Structure

```
Unified-Military-Analytics/

README.md
requirements.txt

Milestone_1/
 ├─ Data_Scraping_and_Cleaning.ipynb
 ├─ README.md
 └─ data/
     ├─ military_raw_data.csv
     └─ military_clean_data.csv

Milestone_2/
 ├─ Exploratory_Data_Analysis.ipynb
 ├─ README.md
 └─ data/
     ├─ military_clean_data.csv
     └─ military_final.csv

Milestone_3/
 ├─ UMAC_Dashboard_2025.pbix
 └─ README.md

Milestone_4/
 └─ Final_Project_Report.pdf
```

---

# 🚀 Setup Guide

## Requirements

Make sure the following tools are installed:

* **Python 3.8 or later**
* **Power BI Desktop**

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SpringBoard03/Unified-Military-Analytics-and-Comparison--Group-1.git
cd Unified-Military-Analytics-and-Comparison--Group-1
```

### 2. Install Required Libraries

```bash
pip install pandas numpy requests beautifulsoup4
```

---

# ▶ Running the Project

## Step 1 — Data Collection

Run the notebook:

```
Milestone_1/Data_Scraping_and_Cleaning.ipynb
```

This step will:

* Scrape military data for multiple countries
* Extract manpower, budget, and equipment statistics
* Produce the dataset:

```
military_raw_data.csv
```

---

## Step 2 — Data Processing & KPI Engineering

Run the notebook:

```
Milestone_2/Exploratory_Data_Analysis.ipynb
```

This stage performs:

* Data cleaning
* Missing value handling
* KPI feature creation

Output dataset:

```
military_final.csv
```

---

## Step 3 — Dashboard Visualization

Open the Power BI file:

```
Milestone_3/UMAC_Dashboard_2025.pbix
```

Import the dataset:

```
military_final.csv
```

The dashboard will generate **interactive military analytics visualizations**.

---

# 📊 Project Milestones

## Milestone 1 — Data Collection

**Goal:** Automate the extraction of military statistics for over 140 countries.

Completed tasks:

* Extract manpower data
* Extract equipment inventories
* Extract defense budget figures

Output:

```
military_raw_data.csv
```

---

## Milestone 2 — KPI Engineering

**Goal:** Convert raw data into meaningful analytical metrics.

Key KPIs created:

| KPI                      | Explanation                                 |
| ------------------------ | ------------------------------------------- |
| Power Index Rank Gap     | Difference from the highest ranked military |
| Assets per Capita        | Equipment availability per population       |
| Budget-to-GDP Ratio      | Defense spending relative to GDP            |
| Equipment Strength Index | Composite hardware strength indicator       |

Output dataset:

```
military_final.csv
```

---

## Milestone 3 — Dashboard Development

Goal: Develop an interactive visualization platform using **Power BI**.

Dashboard features include:

* Global military ranking map
* Country comparison tool
* Regional filters and drill-down
* Equipment and manpower analysis charts

---

## Milestone 4 — Final Documentation

Objective: Compile project findings and methodology into a comprehensive report.

Output file:

```
Final_Project_Report.pdf
```

---

# 🧰 Technology Stack

| Layer           | Tools                           |
| --------------- | ------------------------------- |
| Data Collection | Python, Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy                   |
| Visualization   | Power BI                        |
| Development     | Jupyter Notebook                |
| Documentation   | Markdown, GitHub                |

---

# 🔧 Troubleshooting

### Missing Python Libraries

If you encounter import errors:

```bash
pip install -r requirements.txt
```

### Power BI Dataset Issues

Ensure that:

* `military_final.csv` exists in the correct folder
* Column names remain unchanged
* File encoding is set to **UTF-8**

---

# 👥 Contributors

**Group 1 — Unified Military Analytics & Comparison**

Developed under the **SpringBoard03 academic program**.

---

# 📄 License

This project is intended for **academic and educational purposes only**.

---

*UMAC · Global Military Data Analytics Platform · 2025*
