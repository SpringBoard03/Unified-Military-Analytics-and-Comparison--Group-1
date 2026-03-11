# Milestone 1: Data Collection and Preparation

## Overview

## Overview

In this milestone, military data for 140+ countries was scraped from GlobalFirepower using predefined URLs and stored in a raw dataset. The data was then cleaned by removing formatting symbols, converting values to numeric formats, and handling missing values to create a structured dataset for further analysis.

---

## Objective

* Collect country-level military statistics from multiple sources.
* Convert unstructured web data into a structured dataset.
* Clean and standardize the dataset so it can be used for analytics and dashboard development.

---



## Steps Performed

1. Collected country profile links containing military statistics and prepared a list of URLs for scraping.
2. Scraped key military metrics such as personnel, aircraft, tanks, naval assets, and defense budget for each country and stored them in a raw dataset (**military_raw_data.csv**).
3. Cleaned the raw data by removing special characters, converting values to numeric formats, and standardizing column names.
4. Split combined equipment values (stock and readiness) into separate fields for better analysis.
5. Saved the final structured dataset as **military_cleaned.csv**, making it ready for analysis and dashboard development.

## Deliverables

* **scrape_military_metrics.py** – Script used to scrape military data from country pages
* **military_raw_data.csv** – Raw dataset collected from web scraping
* **clean_data.ipynb** – Notebook used for data cleaning and transformation
* **military_cleaned.csv** – Final structured dataset ready for analysis


