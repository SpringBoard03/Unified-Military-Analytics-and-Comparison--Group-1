# Milestone 1: Data Collection & Preparation (Weeks 1–2)

## 📌 Objective
The primary objective of this milestone is to collect global military strength data from the **Global Firepower (GFP) Index** and transform the raw information into a clean, structured dataset suitable for advanced analytics and dashboard development.

## 🛠️ Module 1: Scraping Setup and Execution
We implemented a Python-based workflow to automate the systematic extraction of military metrics for over 140 countries.

### **Tasks Performed:**
1. **Automated Data Retrieval:** Fetched URLs for 140+ countries.
2. **Metric Extraction:** Scraped manpower, budgets, and hardware counts.
3. **Data Structuring:** Parsed HTML into structured key-value pairs.
4. **Data Storage:** Saved extracted data into a raw CSV file.

### **Technical Stack:**
* **Python Libraries:** `requests`, `BeautifulSoup4`, `pandas`, `re`, and `time`.
* **Workflow:** Implemented request delays (1s) to ensure stable scraping and avoid IP rate-limiting.

## 📊 Data Cleaning & Standardization
Once the raw data was secured, we performed the following processing steps:
1.  **Symbol Removal:** Stripped commas, currency symbols (e.g., "$"), and units (e.g., "ft") from numeric strings.
2.  **Type Conversion:** Converted raw text fields into appropriate numeric data types (integers/floats) for analysis.
3.  **Missing Value Handling:** Identified and handled null entries to maintain structural integrity.
4.  **Column Standardization:** Renamed indicators to consistent, machine-readable formats.

## 📂 Deliverables
| File | Description |
| :--- | :--- |
| `Data_Scraping_and_Cleaning.ipynb` | The primary script/notebook containing the scraping and cleaning logic. |
| `military_raw_data.csv` | The initial dataset containing original scraped values. |
| `military_cleaned_data.csv` | The final processed dataset ready for Milestone 2. |

## ✅ Evaluation Criteria
* **URL Success Rate:** Target ≥ 95% success from the source list.
* **Coverage:** Correctly parsed metric blocks for 140+ countries.
* **Accuracy:** Successful removal of special characters and transformation into numeric formats.

## 🎯 Outcome
Successfully delivered a structured, clean, and comprehensive dataset of global military strength for over 140 countries. This standardized data serves as the critical foundation for KPI engineering and interactive Power BI dashboard development in the upcoming project phases.

---
**Status:** Milestone 1 Completed. Raw data extracted and standardized for downstream analysis.


