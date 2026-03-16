# Milestone 1: Data Collection & Preparation (Weeks 1–2)

## 🎯 Objective
The primary goal of this milestone is to gather global military capability data from the **Global Firepower (GFP)** Index and transform the raw information into a well-structured dataset suitable for further analysis and dashboard development.

## ⚙️ Module 1: Scraping Setup and Execution
A Python-based workflow was designed to automate the extraction of military metrics for more than 140 countries.

## Activities Completed
1. **Source Retrieval:** Accessed country-level data pages from the provided list of URLs.

2. **Metric Extraction:** Collected key indicators including manpower strength, defense budgets, aircraft, tanks, and other equipment statistics.

3. **Data Parsing:** Converted webpage HTML elements into structured key–value data.

4. **Data Storage:** Saved the extracted records into a raw CSV dataset.

## Technology Used
* **Python Libraries:** `requests`, `BeautifulSoup4`, `pandas`, `re`, and `time`

* **Scraping Strategy:** Implemented small request delays to ensure stable data collection and avoid rate limiting.

## 🧹 Data Cleaning & Standardization
After collecting the raw dataset, several preprocessing steps were applied to prepare the data for analytical use.

## Processing Steps
* **Formatting Cleanup:** Removed commas, currency symbols, percentage signs, and other special characters.

* **Numeric Conversion:** Converted textual values into numeric formats (integers and floats).

* **Missing Value Handling:** Checked and handled null or incomplete values to maintain dataset consistency.

* **Column Standardization:** Renamed columns using clear and consistent naming conventions.

## 📦 Deliverables
| File | Description |
| :--- | :--- |
| `Data_Collection_and_Preparation.ipynb` | Notebook containing the full scraping and data preparation workflow. |
| `military_raw_data.csv` | Raw dataset generated directly from web scraping. |
| `military_cleaned.csv` | The final processed dataset ready for Milestone 2. |

## 📊 Evaluation Criteria
* **URL Success Rate:** Target ≥ 95% success from the source list.
* **Coverage:** Correctly parsed metric blocks for 140+ countries.
* **Accuracy:** Successful removal of special characters and transformation into numeric formats.

## 🚀 Outcome
Successfully delivered a structured, clean, and comprehensive dataset of global military strength for over 140 countries. This standardized data serves as the critical foundation for KPI engineering and interactive Power BI dashboard development in the upcoming project phases.

---
**Status:** Milestone 1 Completed. Raw data extracted and standardized for downstream analysis.

