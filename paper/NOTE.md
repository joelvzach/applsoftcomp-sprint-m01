# Analysis of Child Mortality and GDP per Capita

## 1. Data Cleaning Strategy
To prepare the data for analysis, we unified disparate datasets into a single tidy format.

* **Standardization:** We standardized column names across files (e.g., renaming 'geo' and 'time' to consistent formats) to ensure accurate merging.
* **Tidying:** The raw data was in a "wide" format. We converted it to "long" format so each row represents a single Country-Year observation.
* **Merging:** We merged the Child Mortality dataset with the GDP per Capita dataset using `geo` and `year` as keys, ensuring we only analyzed complete records.

## 2. Visualization Choices
We generated a scatter plot to visualize the relationship between economic output and health outcomes.

* **Chart Type:** Scatter Plot.
* **X-Axis:** GDP per Capita (Logarithmic Scale). Using a log scale prevents clustering of lower-income nations and reveals the trend more clearly.
* **Y-Axis:** Child Mortality Rate.
* **Color Encoding:** We mapped the **Year** to the color hue to visualize the temporal progression of development over time.

## 3. Key Insights
* **Negative Correlation:** The data reveals a strong negative correlation: as GDP per Capita increases, Child Mortality decreases significantly.
* **Global Progress:** The color gradient shows a clear trend where most countries have moved "down and to the right" over time, indicating simultaneous improvements in health and wealth.


