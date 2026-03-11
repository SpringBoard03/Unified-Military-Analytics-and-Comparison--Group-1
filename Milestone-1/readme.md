
# Global Military Power Data Scraping & Cleaning Pipeline

## 1. Project Overview
This project builds a structured global military dataset by scraping multiple pages from the Global Firepower website. The notebook collects military, demographic, economic, and geographic indicators for countries and consolidates them into a clean dataset ready for analysis or dashboard creation.

---

## 2. Objective
The objective of this notebook is to scrape Global Firepower data, combine multiple metrics into a unified dataset, clean the scraped values, and produce a dataset ready for analytics and visualization.

---

## 3. Technologies Used
- Python
- Pandas
- Requests
- BeautifulSoup
- Regex
- Jupyter Notebook

---

## 4. Project Architecture

Global Firepower Website  
        ↓  
Web Scraping Layer (Requests + BeautifulSoup)  
        ↓  
Raw Data Extraction  
        ↓  
Data Aggregation (Pandas)  
        ↓  
Data Cleaning & Standardization  
        ↓  
Final Structured Dataset  

---

## 5. Workflow

### Step 1 – Import Libraries
Import pandas, requests, BeautifulSoup, and regex for scraping and data manipulation.

### Step 2 – URL Mapping
A dictionary stores URLs of each metric page so the scraper can automatically iterate across them.

### Step 3 – Base Country Dataset
The base ranking page is scraped to collect country names and power index.

### Step 4 – Reusable Scraping Function
A modular function retrieves and parses metric pages.

### Step 5 – Data Aggregation
All metrics are merged into a single dataframe.

### Step 6 – Data Cleaning
Numeric values are cleaned using regex and converted into proper numeric types.

---

## 6. Output
A cleaned dataframe containing country military statistics that can be used for dashboards and analytics.

---

## 7. Conclusion
The notebook demonstrates a scalable web scraping pipeline that extracts and standardizes global military capability metrics.

