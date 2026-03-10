# Milestone 1: Data Collection & Preparation (Weeks 1–2)

## 📌 Objective
The primary objective of this milestone is to collect global military strength data from the **Global Firepower (GFP) Index** and transform the raw information into a clean, structured dataset suitable for advanced analytics and dashboard development.

## 🛠️ Module 1: Scraping Setup and Execution
We implemented a Python-based workflow to automate the systematic extraction of military metrics for over 140 countries.

### **Tasks Performed:**
* **Automated URL Retrieval:** Programmatically extracted country-specific URLs from the Global Firepower listing page.
* **Metric Extraction:** Scraped high-level military indicators including Manpower, Defense Budgets, Aircraft counts, Naval assets, and Land equipment (Tanks/Artillery).
* **Data Structuring:** Parsed HTML content using `BeautifulSoup` and mapped the findings into structured key-value pairs.
* **Raw Storage:** Compiled all extracted data into a structured CSV format.

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
| `Milestone1.ipynb` | The primary script/notebook containing the scraping and cleaning logic. |
| `military_raw_data.csv` | The initial dataset containing original scraped values. |
| `military_cleaned_data.csv` | The final processed dataset ready for Milestone 2. |

## ✅ Evaluation Criteria
* **URL Success Rate:** Target ≥ 95% success from the source list.
* **Coverage:** Correctly parsed metric blocks for 140+ countries.
* **Accuracy:** Successful removal of special characters and transformation into numeric formats.

---
**Status:** Milestone 1 Completed. Raw data extracted and standardized for downstream analysis.