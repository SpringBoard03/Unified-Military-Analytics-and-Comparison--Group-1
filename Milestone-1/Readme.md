# 🚀 Milestone 1: Data Collection & Preparation

---

## 🎯 Objective
- 🌍 Collect country-level military statistics from reliable sources  
- 🔄 Convert unstructured web data into a structured format  
- 🧹 Clean and standardize the dataset for analytics and visualization  

---

## ⚙️ Steps Performed

### 🔗 Data Collection
- Gathered country profile links containing military statistics  
- Prepared a list of URLs for automated scraping  

---

### 🕷️ Web Scraping
Extracted key military metrics such as:
- 👥 Personnel  
- ✈️ Aircraft  
- 🪖 Tanks  
- 🚢 Naval assets  
- 💰 Defense budget  

Stored the extracted data in:  
`military_raw_data.csv`

---

### 🧹 Data Cleaning & Transformation
- Removed special characters (commas, symbols, etc.)  
- Converted values into proper numeric formats  
- Standardized column names for consistency  
- Split combined fields (e.g., stock & readiness) into separate columns  

---

### 📦 Final Dataset Preparation
Generated a clean and structured dataset:  
`military_cleaned.csv`

Dataset is now ready for:
- 📊 Analysis  
- 📈 Dashboard development  

---

## 📁 Deliverables

| File | Description |
|------|------------|
| 🐍 `scrape_military_metrics.py` | Script used for scraping military data |
| 📄 `military_raw_data.csv` | Raw dataset collected from web scraping |
| 📓 `clean_data.ipynb` | Data cleaning & transformation notebook |
| ✅ `military_cleaned.csv` | Final structured dataset ready for analysis |

---

