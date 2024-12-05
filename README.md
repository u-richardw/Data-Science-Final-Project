# E-commerce Growth Analysis
**COMP3125 Individual Project**  
**Author**: Richard Wu

## Abstract
Over the past few years, e-commerce has expanded quickly, altering how consumers browse and engage with brick-and-mortar stores. This project analyzes how e-commerce is growing as a percentage of total retail, examines the rise of worldwide e-commerce sales, and identifies which regions are driving this increase. Using data from Statista, this research highlights important trends and insights about the future of e-commerce and the factors that contribute to its success.

**Keywords**:
- E-commerce
- Retail growth
- Global trends
- Market analysis

---

## Introduction
Thanks to the internet, new technology, and changes in consumer behavior, e-commerce has revolutionized how people shop. The COVID-19 pandemic significantly accelerated the global adoption of e-commerce. This study examines how e-commerce has expanded globally, which nations and regions are driving this trend, and what the data indicates about its future prospects.

### Key Research Questions:
1. How have global e-commerce sales grown in the last five years?
2. What percentage of total retail sales does e-commerce represent worldwide, and how has this share evolved?
3. Which countries have shown the highest revenue growth in e-commerce over the past few years?

The findings provide stakeholders with insights into the dynamics of the e-commerce market, offering opportunities for future growth.

---

## Datasets

### A. Sources of Data
1. **Worldwide Retail E-Commerce Sales**
   - **Source**: Statista
   - **Description**: Global sales data tracking the growth of e-commerce over time.

2. **E-Commerce Share of Retail Sales Worldwide**
   - **Source**: Statista
   - **Description**: Data showing e-commerce's share of total retail sales globally.

3. **Revenue Growth in E-Commerce for Selected Countries**
   - **Source**: Statista
   - **Description**: Regional and country-specific revenue growth trends for e-commerce.

### B. Characteristics of the Dataset
- **Format**: Tabular datasets (.csv) containing annual sales, percentages, and revenue growth metrics.
- **Features**:
  - Year (time series)
  - Global sales ($ billions)
  - Share of total retail (%)
  - Country/Region-specific revenue growth (%)

- **Preparation**:
  - Data Cleaning: Handling missing values and standardizing units.
  - Feature Engineering: Calculating yearly growth rates and aggregating regional data.

---

## Methodology

### Tools and Techniques
- **Python Libraries**:
  - Pandas for data manipulation.
  - Matplotlib and Seaborn for visualizations.

### Calculations
- Year-over-year growth rates.
- Regional comparisons for e-commerce penetration.

### Models
1. **Time Series Forecasting**:
   - Prophet to predict future trends.
2. **Clustering**:
   - K-Means to group countries based on growth and adoption rates.

---

## Results

### A. Global E-Commerce Sales (2017–2027)
- **Observation**:
  From $1.5 trillion in 2015 to an estimated $8 trillion by 2027, e-commerce revenues have increased steadily. This illustrates the sector's explosive growth, representing a five-fold increase over 12 years.

### B. E-Commerce as a Percentage of Total Retail Sales (2021–2027)
- **Observation**:
  E-commerce's percentage share of overall retail sales increased from 18.8% in 2021 to a predicted 22.6% by 2027, demonstrating the growing global adoption of online sales in the retail industry.

### C. Leading Countries in Retail E-Commerce Growth (2023)
- **Key Insights**:
  - Mexico leads with a growth rate of 25.1%, followed by the Philippines (24.1%) and Malaysia (18%).
  - Significant increase is seen in emerging markets such as Argentina, Brazil, and India, indicating unrealized potential in these areas.
  - Despite attaining growth of 11.4%, China's market is maturing in contrast to its previous double-digit expansion rates.

---

## Visualizations

1. **Global E-Commerce Sales Trend (2017–2027)**
   - Line graph depicting sales growth from 2017 to 2027.
   
2. **E-Commerce Share of Retail Sales (2021–2027)**
   - Bar chart showcasing the rise in e-commerce as a percentage of total retail sales.

3. **Top 10 Countries for E-Commerce Growth in 2023**
   - Horizontal bar chart comparing growth rates for leading countries.

---

## References
1. [Statista: Worldwide Retail E-Commerce Sales](https://www-statista-com.ezproxywit.flo.org/statistics/379046/worldwide-retail-e-commerce-sales/)
2. [Statista: E-Commerce Share of Retail Sales Worldwide](https://www-statista-com.ezproxywit.flo.org/statistics/534123/e-commerce-share-of-retail-sales-worldwide/)
3. [Statista: Revenue Growth in E-Commerce for Selected Countries](https://www-statista-com.ezproxywit.flo.org/statistics/266064/revenue-growth-in-e-commerce-for-selected-countries/)

