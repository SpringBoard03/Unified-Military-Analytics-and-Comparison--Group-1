# Milestone 02 — KPI Engineering & Tableau Preparation

## Objective

Compute key performance indicators (KPIs) from the cleaned military dataset and prepare the data in a format suitable for interactive visualization in Tableau dashboards.


## Approach

The cleaned dataset from Milestone 01 was used as the base dataset.  
A Python workflow was implemented to engineer additional analytical metrics and enrich the dataset with supporting metadata.

The approach included:

- Creating derived KPI metrics from existing military indicators
- Enriching the dataset with geographical and alliance metadata
- Preparing the dataset structure for Tableau visualization
- Exporting the final dataset in a format ready for dashboard development

This ensures the dataset supports comparative military analysis and interactive dashboards without requiring additional transformations.


## Steps Performed in KPI Engineering & Tableau Preparation

### 1. Dataset Loading

The cleaned dataset generated in Milestone 01 was loaded using the Pandas library.

```
military_updated.csv
```

Basic dataset validation steps were performed to confirm:

- Column structure  
- Data types  
- Row counts  
- Missing values  

### 2. KPI Feature Engineering

New analytical indicators were created using existing military metrics.

The following KPIs were computed:

**Power Index Rank Gap**

Measures the difference between the expected rank and the actual power index rank to highlight comparative military positioning.

**Assets per Capita**

Calculates the distribution of military assets relative to population size.

**Budget-to-GDP Ratio**

Measures defense spending intensity relative to national economic output.

These KPIs enable meaningful cross-country comparisons of military strength and resource allocation.

### 3. Metadata Enrichment

Additional metadata was integrated into the dataset to improve analytical capabilities.

The following metadata fields were added:

- Region  
- Continent  
- NATO alliance flag  

These attributes support regional comparisons and alliance-based analysis in dashboards.

### 4. Data Formatting for Visualization

The dataset was structured to support Tableau dashboard requirements.

Two dataset formats were prepared:

**Wide Format**

Each KPI and metric is stored as a column, making it suitable for statistical analysis and filtering.

**Long Format**

Metrics are transformed into attribute-value pairs to support flexible visualizations in Tableau.

### 5. Final Dataset Export

After KPI computation and data enrichment, the final structured dataset was exported for visualization and dashboard development.


## Generated Output Files

| File | Description |
|------|-------------|
| military_updated_csv | Final dataset containing engineered KPIs and enriched metadata |
