# DivisionMetrics: Regional Attendance Analysis & Comparison

A statistical analysis project comparing attendance patterns across North, South, and West divisions using ANOVA, post-hoc tests, and data visualization techniques.

## Project Overview

DivisionMetrics analyzes and compares attendance data across three geographic divisions (North, South, and West) using comprehensive statistical methods and visual representations. The project employs both parametric tests and graphical analysis to identify significant differences between divisions and provide insights for organizational decision-making.

## Key Features

- **Descriptive Statistics**: Calculates means, medians, standard deviations, and ranges for each division
- **Inferential Analysis**: Implements one-way ANOVA to test for significant differences between divisions
- **Post-hoc Testing**: Uses Tukey's HSD test for pairwise comparisons between divisions
- **Data Visualization**: Creates multiple visualization types (boxplots, bar charts, violin plots, pair plots)
- **Statistical Reporting**: Provides detailed statistical outputs with p-values and significance interpretations

## Analysis Components

### Descriptive Statistics
For each division (North, South, West), the analysis calculates:
- Mean attendance
- Median attendance
- Standard deviation
- Range (min to max)

### Statistical Testing
The project implements a structured hypothesis testing approach:

1. **One-way ANOVA**: Tests the null hypothesis that all division means are equal
2. **Tukey's HSD Test**: Performs pairwise post-hoc comparisons to identify which specific divisions differ
3. **Significance Testing**: Reports p-values and draws conclusions about statistical significance

### Visualizations

The project includes four visualization types:

1. **Boxplots**: Show the distribution, central tendency, and potential outliers in each division
2. **Bar Charts**: Display mean attendance values for easy comparison
3. **Violin Plots**: Combine boxplot information with kernel density estimates to show distribution shapes
4. **Pairwise Scatter Plots**: Examine relationships between variables across divisions

## Key Findings

The analysis reveals:

- Clear attendance differences between divisions, with West showing the highest attendance
- South division consistently demonstrates lower attendance compared to North and West
- Statistical significance in the differences between divisions (supported by ANOVA results)
- Specific significant pairwise differences (identified through Tukey's HSD test)
- Distribution shapes and patterns unique to each division (visualized in violin plots)

## File Structure

- `stats.py`: Main Python script containing the complete analysis
- `data.xlsx`: Dataset with attendance information by division
- `boxplot.png`: Boxplot visualization of attendance by division
- `barchart.png`: Bar chart of mean attendance by division
- `violinplot.png`: Violin plot of attendance distribution by division
- `pairplot.png`: Pairwise scatter plots across variables and divisions

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/AdithyaSriramoju/DivisionMetrics.git
   cd DivisionMetrics
   ```

2. Install required packages
   ```
   pip install pandas scipy matplotlib seaborn statsmodels
   ```

3. Run the analysis script
   ```
   python stats.py
   ```

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **SciPy**: Statistical testing and ANOVA implementation
- **Statsmodels**: Post-hoc testing with Tukey's HSD
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Development environment (optional)

## Future Work

- Incorporate time-series analysis to examine attendance trends over time
- Expand dataset to include additional variables that might explain attendance differences
- Implement non-parametric alternatives for robustness
- Develop interactive dashboards for exploring the data
- Add machine learning models to predict future attendance patterns

## Author

Adithya Sriramoju

## Acknowledgments

- Statistical communities for their invaluable resources on ANOVA and post-hoc testing
- The Python data science ecosystem for their excellent tools and libraries
