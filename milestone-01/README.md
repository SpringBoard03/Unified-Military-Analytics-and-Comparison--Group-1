# 📊 Data Collection & Preparation

## 🎯 Objective
Collect global military strength data and transform it into a **clean, structured dataset** for **analysis and visualization**.

## ⚙️ Approach
A **Python-based workflow** was implemented to automate:

- **Scraping military metrics** from the source website  
- **Structuring and cleaning** the data  
- Exporting a **processed dataset** ready for analysis  

This ensures **raw web data is converted into a reliable, structured format** for further project stages.

## 📝 Steps Performed

### 1️⃣ Data Scraping Setup
Imported Python libraries:

- **requests**, **BeautifulSoup**, **csv**, **time**, **re**  

Functions:

- Send **HTTP requests**  
- **Parse HTML content**  
- Store data in **CSV format**  
- Handle **timing and delays**  

### 2️⃣ Data Extraction
- Extracted military indicators such as **manpower, defense budget, aircraft, naval assets, tanks, artillery**  
- Structured data into **key-value pairs per country**

### 3️⃣ Raw Dataset Generation
- Saved collected data into:  
  `data/military_raw_data.csv`  
- **Rows:** countries | **Columns:** military indicators

### 4️⃣ Data Cleaning
Using **Pandas**:

- Removed **commas, currency symbols, special characters**  
- Converted numeric fields to proper **data types**  
- Standardized **column names**  

### 5️⃣ Handling Missing Values
- Identified **missing or invalid entries**  
- Applied replacements to maintain **dataset consistency**

### 6️⃣ Clean Dataset Export
- Final cleaned dataset exported as:  
  `data/military_cleaned_data.csv`   
- Ready for **analysis and dashboard development**

## 📂 Generated Output Files

| **File** | **Description** |
|----------|----------------|
| `data/military_raw_data.csv` | Raw dataset from scraping |
| `data/military_cleaned_data.csv` | Cleaned dataset ready for analysis |
