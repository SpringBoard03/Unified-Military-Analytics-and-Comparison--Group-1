# Unified Military Analytics and Comparison Dashboard

## 🎯 Milestone 1 — Data Collection and Preparation

### Overview

Milestone 1 focuses on building the **data foundation** for the *Unified Military Analytics and Comparison Dashboard*.

In this phase, military capability metrics for **140+ countries** are collected from **GlobalFirepower.com** using automated web scraping. After scraping, the raw data is **cleaned, standardized, and structured** to prepare it for analytics and dashboard development.

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

The scraping script reads URLs from a predefined file and automatically collects military statistics for each country.

##### 🛠 Tasks Performed

* Use **`links_for_military_data.txt`** as the source list of country URLs
* Some of the extracted military metrics include:

  * ✈️ Total Aircraft
  * 🛩 Fighter Aircraft
  * 🚁 Helicopters
  * 🛡 Tanks
  * 🚙 Armored Vehicles
  * 🔫 Self-Propelled Artillery
  * 🎯 Rocket Projectors
  * 🚢 Naval Assets
  * 🐋 Submarines
  * 🚤 Patrol Vessels
  * 💰 Defense Budget
  * 👥 Active Personnel
  * 🪖 Reserve Personnel
* Parse structured metric blocks from each webpage
* Store the extracted information in structured format
* Optionally save **HTML snapshots for debugging**

##### 📦 Deliverables

* Script:
  `scrape_military_metrics.py`

* Output dataset:
  `military_raw_data.csv`

---

#### 2. Module 2 — Data Cleaning and Structuring

The raw scraped dataset contains text formatting, symbols, and inconsistent column structures.
This module focuses on **cleaning and transforming the raw data into a standardized analytical dataset**.

This cleaned dataset will later be used as **input for KPI engineering and dashboard visualization**.

##### 🛠 Tasks Performed

* Remove unnecessary characters such as:

  * commas
  * percentage signs
  * plus symbols
  * special formatting characters

* Convert extracted values into **numeric formats**

* Standardize column names for consistency

Example:

```
Total Aircraft → total_aircraft
Active Personnel → active_personnel
```

* Handle **missing or null values**
* Validate dataset consistency
* Export a cleaned dataset ready for analytics tools

##### 📦 Deliverables

* Clean dataset:
  `military_cleaned.csv`

* Data cleaning notebook:
  `clean_data.ipynb`

---

### 📊 Output of Milestone 1

By the end of this milestone, two datasets are produced:

1. **Raw Dataset**

```
military_raw_data.csv
```

2. **Clean Dataset**

```
military_cleaned.csv
```

These datasets contain **military capability metrics for 140+ countries**, forming the **core dataset for the entire analytics platform**.

---

### 🔜 Next Step

In the next milestone, the cleaned dataset will be used to perform **KPI Feature Engineering**.



