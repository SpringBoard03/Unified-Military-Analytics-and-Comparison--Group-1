# Unified Military Analytics and Comparison Dashboard

## 🎯 Milestone 1 — Data Collection and Preparation

### Overview

Milestone 1 focuses on building the **data foundation** for the *Unified Military Analytics and Comparison Dashboard*.

In this phase, military capability metrics for **140+ countries** are collected from [Global Firepower website](https://www.globalfirepower.com/) using automated web scraping. After scraping, the raw data is **cleaned, standardized, and structured** to prepare it for analytics and dashboard development.

This milestone ensures that the dataset is **accurate, consistent, and ready for KPI engineering in the next stage**. 

---

### 🎯 Objectives

The main objectives of this milestone are:

* Scrape military metrics for **140+ countries**
* Extract structured defense data from **GlobalFirepower**
* Store the raw dataset for processing
* Prepare the data pipeline for cleaning and transformation
* Ensure reliable data extraction with minimal missing values

---

### 🧩 Modules in Milestone 1

Milestone 1 consists of **two key modules**.


#### 1. Module 1 — Scraping Setup and Execution

This module focuses on building the **web scraping pipeline** to extract military metrics from GlobalFirepower country pages.
Builds the pipeline to extract military metrics from country pages.

**🛠 Tasks**
- Use `links_for_military_data.txt` for URLs  
- Extract key metrics (aircraft, tanks, naval assets, budget, personnel)  
- Parse structured data from webpages  
- Store data in tabular format  
- Save HTML (optional for debugging)  

**📦 Deliverables**
- `scrape_military_metrics.py`  
- `military_raw_data.csv` 

---

#### 2. Module 2 — Data Cleaning and Structuring

Transforms raw data into a **clean analytical dataset**.

**🛠 Tasks**
- Remove symbols (commas, %, +, etc.)  
- Convert values to numeric format  
- Standardize column names (e.g., `total_aircraft`)  
- Handle missing values  
- Validate and export cleaned dataset  

**📦 Deliverables**
- `military_cleaned.csv`  
- `clean_data.ipynb` 

---

### 📊 Output 

By the end of this milestone, two datasets are produced:

| **File** | **Description** |
|------|-------------|
| **data/military_raw_data.csv** | Raw dataset generated from the scraping process |
| **data/military_cleaned_data.csv** | Cleaned dataset prepared for analysis |

---

### 🔜 Next Step

In the next milestone, the cleaned dataset will be used to perform **KPI Feature Engineering**.








