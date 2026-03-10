# **Milestone 01 — Data Collection & Preparation**

## **Objective**

Collect global military strength data from the source website and transform the raw information into a **clean and structured dataset** suitable for further **analysis and visualization**.

## **Approach**

A **Python-based workflow** was implemented to automate the **data collection and preparation process**.

The approach involved:

- **Scraping military metrics** from the source website  
- Structuring the extracted data into a **dataset**  
- **Cleaning and standardizing** the values  
- Generating a **processed dataset** ready for analysis and dashboard development  

The workflow ensures that **raw web data is converted into a structured format** that can be reliably used for further stages of the project.

## **Steps Performed in Data Collection & Preparation**

### **1. Data Scraping Setup**

Required **Python libraries** were imported to support the scraping and data processing workflow.

Libraries used include:

- **requests**  
- **BeautifulSoup**  
- **csv**  
- **time**  
- **re**

These libraries were used to:

- Send **HTTP requests** to the website  
- **Parse HTML content**  
- Store extracted data in **CSV format**  
- Manage **request timing and delays**

### **2. Data Extraction**

HTTP requests were sent to the **source website** to access **country-specific military information pages**.

The HTML content was parsed using **BeautifulSoup** to extract military indicators such as:

- **Manpower**
- **Defense Budget**
- **Aircraft Counts**
- **Naval Assets**
- **Tanks**
- **Artillery**

The extracted information was structured into **key-value pairs for each country**.

### **3. Raw Dataset Generation**

The collected information was written into a **structured CSV file** where:

- Each **row represents a country**
- Each **column represents a military indicator**

The raw dataset generated during this step is saved as:

data/military_raw_data.csv

This file contains the **original scraped values directly from the website**.

### **4. Data Cleaning**

The raw dataset was loaded using the **Pandas library** and processed to improve **data quality and consistency**.

The following transformations were applied:

- **Removal of commas, currency symbols, and special characters**
- **Conversion of numeric fields into appropriate numeric data types**
- **Standardization of column names**

These steps ensure the dataset can be **easily used for analysis and further processing**.

### **5. Handling Missing Values**

Missing or invalid entries were **identified within the dataset**.

Appropriate replacements were applied to:

- Maintain **dataset consistency**
- **Minimize missing values**

This step ensures the dataset remains **structurally reliable for downstream analysis**.

### **6. Clean Dataset Export**

After completing the **cleaning and standardization steps**, the processed dataset was exported as:

data/military_cleaned_data.csv

This dataset serves as the **final structured dataset generated during this milestone** and is prepared for **further analysis and dashboard development**.

## **Generated Output Files**

| **File** | **Description** |
|------|-------------|
| **data/military_raw_data.csv** | Raw dataset generated from the scraping process |
| **data/military_cleaned_data.csv** | Cleaned dataset prepared for analysis |
