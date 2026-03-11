# Unified Military Analytics and Comparison Dashboard

## 🎯 Milestone 1 — Data Collection and Preparation

### Overview

Milestone 1 focuses on **collecting, validating, and structuring global military data** required for building the *Unified Military Analytics and Comparison Dashboard*.
The goal of this milestone is to scrape military capability metrics for **140+ countries** and prepare a clean dataset for further analysis and visualization.

The collected data will later be used for **KPI engineering and dashboard development** in upcoming milestones.

---

### 📌 Objectives

The main objectives of this milestone are:

* Scrape military metrics for **140+ countries**
* Extract structured defense data from **GlobalFirepower**
* Store the raw dataset for processing
* Prepare the data pipeline for cleaning and transformation
* Ensure reliable data extraction with minimal missing values

---

### 🛠 Tasks Performed

#### 1. Data Source Identification

A predefined list of country pages was used as the source for scraping military data.

Each page contains structured information about a country's:

* 👥 Military manpower
* ✈️ Air power
* 🛡 Land systems
* 🚢 Naval strength
* 💰 Defense budget
* 🌐 Logistics and natural resources


#### 2. Web Scraping Implementation

The scraping pipeline was developed using Python with the following libraries:

* **requests** → to fetch webpage content
* **BeautifulSoup** → to parse HTML structures
* **pandas** → to structure the extracted data
* **numpy** → for numerical processing

The script iterates through a list of country URLs and extracts important military indicators.



#### 3. Extracted Metrics

Some of the extracted military metrics include:

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

These metrics form the **core dataset for global military comparison**.



#### 4. Data Storage

The scraped data is stored in a structured format for further processing.

Output files include:

* `military_raw_data.csv` → Raw scraped dataset

Each row represents a **country**, while columns represent **military capability metrics**.

---

### 📈 Output

The output of this milestone is a **structured dataset containing military capability metrics for 140+ countries**(`military_raw_data.csv`).

---

### 🔜 Next Step

The next milestone will focus on data cleaning and feature engineering.


