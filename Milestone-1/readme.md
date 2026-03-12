📊 Milestone 1: Data Collection & Preparation (Weeks 1–2)
🎯 Objective

The objective of this milestone was to acquire global military capability data from the Global Firepower (GFP) Index and transform the raw information into a structured, high-quality dataset suitable for advanced analytics and dashboard development.

⚙️ Module 1: Data Scraping Setup and Execution

A Python-based automated pipeline was developed to systematically extract military capability metrics for more than 140 countries from the source platform.

🧩 Key Activities

1️⃣ Automated Data Retrieval
Programmatically collected country-specific URLs to enable large-scale extraction of military statistics.

2️⃣ Metric Extraction
Scraped critical indicators including manpower statistics, defense budgets, and military equipment inventories.

3️⃣ Data Structuring
Parsed the HTML structure of the webpages and transformed the extracted information into structured key–value datasets.

4️⃣ Data Storage
Persisted the collected data into a raw CSV file to support subsequent cleaning and transformation processes.

🧰 Technical Stack

Programming Language: Python
Libraries Utilized: requests, BeautifulSoup4, pandas, re, and time

The scraping workflow incorporated controlled request intervals (1-second delay) to maintain stability and prevent potential rate-limiting from the source server.

🧹 Data Cleaning and Standardization

Following data acquisition, the dataset underwent preprocessing to ensure consistency, usability, and analytical readiness.

🔹 Symbol and Unit Removal
Removed formatting characters such as commas, currency symbols (e.g., $), and unit indicators (e.g., ft) from numeric fields.

🔹 Data Type Conversion
Converted textual numerical representations into appropriate numeric formats (integers and floats) to support quantitative analysis.

🔹 Missing Value Management
Identified and handled null or incomplete entries to maintain dataset integrity.

🔹 Column Standardization
Renamed indicators using consistent and machine-readable naming conventions to improve compatibility with analytical tools.

📂 Deliverables
📁 File 📝 Description
Data_Scraping_and_Cleaning.ipynb Python notebook containing the complete scraping and data preprocessing pipeline.
military_raw_data.csv Raw dataset containing the original extracted values from the source platform.
military_cleaned_data.csv Processed dataset with cleaned, standardized, and analysis-ready data.
📈 Evaluation Criteria

✅ URL Retrieval Success Rate: Achieve ≥ 95% successful requests from the source list.

🌍 Data Coverage: Successfully parse metric blocks for 140+ countries.

🎯 Data Accuracy: Ensure proper removal of special characters and accurate conversion into numeric formats.

🏁 Outcome

This milestone successfully produced a comprehensive and standardized dataset capturing global military strength indicators for more than 140 countries. The cleaned dataset serves as the analytical foundation for subsequent project phases, including KPI development and the creation of interactive dashboards using Power BI.

📌 Status: Milestone 1 Successfully Completed — dataset prepared for advanced analytics and visualization in the next phase.
