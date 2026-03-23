## 🚀 Milestone 1 — Data Collection & Preparation 

### 🎯 Objective
Collect global military capability data from the Global Firepower (GFP) Index and transform raw web data into a structured dataset for analysis and dashboard development.

### ⚙️ Scraping Workflow
- 🤖 Automated extraction of military metrics for **140+ countries** using Python  
- 🔗 Retrieved country data from a predefined URL list  
- 📊 Extracted indicators such as manpower strength, defense budget, aircraft, tanks, and other equipment stats  
- 🧩 Parsed HTML content into structured key–value format  
- 💾 Stored extracted data in a **raw CSV dataset**

### 🛠️ Tech Stack
- 🐍 Python: `requests`, `BeautifulSoup4`, `pandas`, `re`, `time`  
- ⏱️ Implemented request delays to ensure stable scraping and avoid rate limiting  

### 🧹 Data Cleaning & Standardization
- 🧽 Removed commas, currency symbols, percentages, and special characters  
- 🔢 Converted textual values into numeric formats (int / float)  
- ⚠️ Handled missing or null values  
- 🏷️ Standardized column naming conventions  

### 📦 Deliverables

| 📁 File | 📝 Description |
|--------|---------------|
| `Data_Collection_and_Preparation.ipynb` | Complete scraping and preprocessing workflow |
| `military_raw_data.csv` | Raw dataset generated from web scraping |
| `military_cleaned.csv` | Final cleaned dataset prepared for next milestone |

### 📈 Outcome
Generated a **clean and structured military dataset for 140+ countries**, ready for KPI engineering and Power BI dashboard development.

**Status:** ✅ Milestone 1 Completed
