# 🛡️ Unified Military Analytics and Comparison Dashboard

## 📑 Contents

* Overview
* Objective
* Project Architecture
* Dataset Description
* Project Milestones
* Tech Stack
* Outputs
* Repository Structure

---

## 🌍 Overview

This project develops an interactive analytics platform for analyzing and comparing global military capabilities in 2026. Military data for more than 140 countries is scraped from GlobalFirepower and processed using a Python-based data pipeline. The dataset is cleaned, enriched with key performance indicators, and prepared for analysis. Interactive dashboards are then built to explore military strength, compare countries, and evaluate potential coalitions.

---

## 🎯 Objective

The primary objectives of this project are:

* Collect global military data from publicly available sources
* Build an automated data pipeline for scraping and processing defense statistics
* Create derived indicators that allow meaningful comparison between countries
* Develop interactive dashboards for exploring global military capabilities
* Enable country comparisons and coalition analysis using visual analytics

---

## 🏗️ Project Architecture

```
Data Source (GlobalFirepower)
        │
        ▼
Web Scraping
(Python + BeautifulSoup)
        │
        ▼
Raw Dataset
(military_raw_data.csv)
        │
        ▼
Data Cleaning & Structuring
(Pandas Processing)
        │
        ▼
Clean Dataset
(military_cleaned.csv)
        │
        ▼
KPI Feature Engineering
(generate_kpis.py)
        │
        ▼
Final Dataset
(military_final.xlsx)
        │
        ▼
Interactive Dashboards
(Tableau / Power BI / Streamlit / Dash)
```

---

## 📊 Dataset Description

The dataset used in this project contains military statistics collected for more than **140 countries**. It includes over **50 defense and economic indicators**, such as:

* Active military personnel
* Reserve forces
* Aircraft inventory
* Tank inventory
* Naval assets
* Defense budget
* Economic indicators like GDP and external debt

These metrics are used to build analytical indicators and comparative dashboards.

---

## 🚀 Project Milestones

### 📦 Milestone 1 — Data Collection and Preparation

This stage focuses on building the data pipeline required to collect and clean military statistics.

**Web Scraping**

A Python script is used to access a list of predefined URLs containing military statistics for each country. The script retrieves country-level data such as aircraft counts, tank inventories, personnel numbers, and defense budgets.

The extracted data is stored in a structured CSV dataset.

**Data Cleaning and Structuring**

The raw dataset contains formatting inconsistencies such as commas, special characters, and mixed data types. A cleaning process standardizes the dataset by converting values into numeric formats, handling missing values, and organizing the dataset into a consistent structure.

---

### 📈 Milestone 2 — KPI Engineering and Dashboard Planning

In this stage, additional analytical indicators are generated from the cleaned dataset.

Examples of derived metrics include:

* Power Index Rank Gap
* Assets per Capita
* Defense Budget to GDP Ratio

Metadata such as region, continent, and alliance membership are also added to support filtering and comparisons within dashboards.

---

### 📊 Milestone 3 — Dashboard Development

This milestone focuses on building the interactive dashboards used to explore the dataset.

Four main dashboard modules are developed:

* **Quick Stats** – Overview of global rankings and highlights
* **Nation Overview** – Detailed country-level military profile
* **Compare Powers** – Side-by-side comparison of countries
* **Coalition Builder** – Combined military power simulation

---

### 🧪 Milestone 4 — Final Integration and Delivery

This milestone focuses on testing, debugging, and preparing the project for final release.

This includes:

* verifying dashboard accuracy
* testing filters and interactions
* correcting layout or labeling issues
* organizing project files and documentation

---

## 🛠️ Tech Stack

| Area            | Tools / Libraries               |
| --------------- | ------------------------------- |
| Data Collection | Python, Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy                   |
| Visualization   | Power BI                        |
| Dashboard Apps  | Streamlit, Dash                 |
| Data Storage    | CSV, Excel                      |
| Documentation   | Markdown, GitHub                |

---

## 📦 Outputs

The project generates several outputs during different stages of the pipeline:

* **military_raw_data.csv** – Raw dataset collected from web scraping
* **military_cleaned.csv** – Cleaned and structured dataset
* **military_final.csv** – Final dataset with calculated KPIs
* **global_military_firepower_2026.ipbx** – Dashboard workbook

---

## 📁 Repository Structure

```
global-military-analytics
│
├── data
│   ├── military_raw_data.csv
│   ├── military_cleaned.csv
│   └── military_final.csv
│
├── scripts
│   ├── scrape_military_metrics.py
│   ├── clean_data.ipynb
│   └── generate_kpis.ipynb
│
├── dashboards
│   └── global_military_firepower_2026.ipbx
│
├── docs
│   └── dashboard_storyboard.md
│
└── README.md
```

This repository demonstrates a complete data analytics workflow, starting from web scraping and data processing to interactive dashboard development for global military analysis.
