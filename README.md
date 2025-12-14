# Project Structure Overview

This repository contains the data, code, and analysis outputs used for the user review analysis.

## data

Raw and processed datasets used in the analysis.

### 1094591345_us.csv (Pokemon Go)
### 1437969979_us.csv  (Shimano E-TUBE)
### 1484302191_us.csv  (Segway Mobility)
### 1536111825_us.csv  (Giant RideControl)
### 1609966547_us.csv  (Trek Central)

---

## notebooks

Jupyter notebooks used for exploratory data analysis and modeling.

### analyze_phrase.ipynb
- Visualization of phrese frequency via word clouds and bar charts

### analyze_review.ipynb
- Converts reviews into semantic embeddings  
- Performs clustering for different sentiment groups  
- Automatically labels clusters using keywords  

### statistics.ipynb
- Verifies sentiment distribution  
- Generates sentiment distribution plots  


---

## figures

Exported figures used in the report and presentation.

### image_NLP
word cloud and bar chart images based on word frequency for different apps

### image_stats
Sentiment distribution plots

---

## cluster results

### cluster_result.txt
Cluster results text for different sentiment groups of five apps

---

## How to Run the Project

1. Install dependencies
2. Run the crawler to collect reviews:
   ```bash
   python crawler.py
3. Check the jupyter notebooks