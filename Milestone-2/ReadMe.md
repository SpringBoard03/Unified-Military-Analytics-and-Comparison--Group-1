# Milestone 2: KPI Engineering and Dashboard Preparation

## Overview

The second milestone focuses on transforming the cleaned military dataset into a more analytical format by creating key performance indicators (KPIs) and preparing the data for visualization.

In this stage, new metrics are derived from the cleaned dataset to help analyze and compare military capabilities across countries. The dataset is also enriched with additional metadata and structured in a way that allows it to be easily used in visualization tools.

This milestone also includes planning the structure and interactions of the dashboards that will be built in the next stage of the project.

---

# Objective

The main goals of this milestone are:

* Generate analytical KPIs from the cleaned military dataset
* Enrich the dataset with geographic and alliance information
* Prepare the dataset for visualization tools such as Power BI
* Design and prototype the structure of the dashboards

---

# Architecture

```
Clean Dataset
(military_cleaned.csv)
        │
        ▼
KPI Feature Engineering
(generate_kpis.ipynb)
        │
        ▼
Enriched Dataset
(military_final.xlsx)
        │
        ▼
Dashboard Planning
(Layout Sketches & Wireframes)
        │
        ▼
Prototype Dashboard
```

---

# KPI Engineering

To enable deeper analysis of global military power, several new indicators are calculated from the cleaned dataset.

### Power Index Rank Gap

This metric measures the difference between a country's ranking and other countries in the dataset.
It helps highlight how far a country is from the leading military powers.

### Assets per Capita

This indicator evaluates how many military resources are available relative to the population size.
It provides insight into how concentrated military assets are within a country.

### Budget-to-GDP Ratio

This metric measures the proportion of a country's economic output that is allocated to defense spending.
It helps understand the priority a nation places on military expenditure.

---

# Metadata Enrichment

To make the dataset more useful for analysis and filtering in dashboards, additional contextual fields are added, including:

* Region
* Continent
* Alliance membership indicators (for example NATO)

These attributes allow users to group and compare countries based on geography or alliances.

---

# Data Preparation for Visualization

The enriched dataset is structured so it can be directly imported into visualization tools without additional transformations.

The dataset is organized to support:

* country comparisons
* regional filtering
* KPI-based analysis
* interactive dashboards

The final dataset generated in this stage is saved as:

**military_final.xlsx**

---

# Dashboard Planning

Before building the final dashboards, the overall structure and layout of the visualization system are planned. The dashboard suite consists of four major sections:

**Quick Stats**
Provides a global overview of military rankings, trends, and summary indicators.

**Nation Overview**
Displays a detailed profile of a selected country including manpower, air power, land forces, and naval capabilities.

**Compare Powers**
Allows side-by-side comparison between two countries using key military and economic metrics.

**Coalition Builder**
Simulates the combined military strength of multiple countries to analyze alliance capabilities.

Wireframes and layout sketches are created to define how these dashboards will interact with each other.

---

# Deliverables

* **generate_kpis.ipynb** – script used to generate KPIs
* **military_final.xlsx** – final dataset containing engineered metrics
* **dashboard_storyboard.md** – dashboard layout and design plan


---

# Output

The primary output of this milestone is an **analysis-ready dataset enriched with KPIs** that can be directly used for dashboard development.

The dashboard design blueprint created in this stage ensures that the full dashboard suite can be implemented efficiently in the next milestone.

