# Milestone 1: Data Collection and Preparation

## Overview

In this milestone, the goal was to build the foundation for the military analytics project by collecting and preparing global military data. The data was scraped from multiple country pages using a list of URLs and then processed to create a structured dataset.

Since the raw scraped data contained formatting inconsistencies such as commas, symbols, and mixed data types, a cleaning process was applied to standardize the data and make it suitable for analysis and visualization in later milestones.

---

## Objective

* Collect country-level military statistics from multiple sources.
* Convert unstructured web data into a structured dataset.
* Clean and standardize the dataset so it can be used for analytics and dashboard development.

---

## Architecture

```
Country URLs
   │
   ▼
Web Scraping
(scrape_military_metrics.py)
   │
   ▼
Raw Dataset
(military_raw_data.csv)
   │
   ▼
Data Cleaning & Transformation
(clean_data.ipynb)
   │
   ▼
Final Dataset
(military_cleaned.csv)
```

---

## Steps Performed

### 1. Accessing Country Military Pages

The process begins by accessing a webpage that lists military strength profiles for multiple countries.
Each country in the list links to a separate page containing detailed military statistics.

These pages act as the primary source for collecting military data.

---

### 2. Extracting Country Profile Links

All country profile links were extracted from the listing page.
Each link corresponds to a specific country and contains detailed military metrics.

These links were converted into complete URLs so that they could be accessed programmatically.

---

### 3. Removing Duplicate Links

After extracting the country URLs, duplicate links were removed to ensure that each country page was processed only once.
The links were also sorted to maintain an organized scraping workflow.

---

### 4. Scraping Military Metrics

Each country page was then accessed and parsed to extract important military statistics such as:

* Active military personnel
* Aircraft inventory
* Tank inventory
* Naval assets
* Defense budget
* Other military capability indicators

The extracted information for each country was stored temporarily before being added to the dataset.

---

### 5. Creating the Raw Dataset

After collecting the data from all country pages, the information was organized into a structured table format and saved as:

**military_raw_data.csv**

Although the dataset was structured, it still contained formatting issues such as commas, symbols, and combined values.

---

### 6. Data Cleaning and Structuring

The raw dataset was then processed to improve its quality and usability.

The cleaning process included:

* Removing commas, percentage symbols, and other special characters
* Converting values into numeric formats
* Standardizing column names
* Handling missing or inconsistent values

---

### 7. Separating Combined Metrics

Some military equipment columns contained two values in the same field, representing total stock and operational readiness.

These values were separated into individual columns so that they could be analyzed independently.

---

### 8. Creating the Final Dataset

After cleaning and restructuring the data, the final dataset was saved as:

**military_cleaned.csv**

This dataset is now structured, standardized, and ready for analysis and visualization.

---

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas
* Jupyter Notebook
* CSV
