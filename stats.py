import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel sheet into a DataFrame
df = pd.read_excel("data.xlsx")

# Separate data by division
north_data = df[df["Division"] == "North"]["Attendance"]
south_data = df[df["Division"] == "South"]["Attendance"]
west_data = df[df["Division"] == "West"]["Attendance"]

# Calculate statistics
north_mean = north_data.mean()
north_median = north_data.median()
north_std = north_data.std()
north_range = north_data.max() - north_data.min()

south_mean = south_data.mean()
south_median = south_data.median()
south_std = south_data.std()
south_range = south_data.max() - south_data.min()

west_mean = west_data.mean()
west_median = west_data.median()
west_std = west_data.std()
west_range = west_data.max() - west_data.min()

# Print the results
print("North Division:")
print(f"• Mean Attendance: {north_mean}")
print(f"• Median Attendance: {north_median}")
print(f"• Standard Deviation: {north_std}")
print(f"• Range: {north_range}\n")

print("South Division:")
print(f"• Mean Attendance: {south_mean}")
print(f"• Median Attendance: {south_median}")
print(f"• Standard Deviation: {south_std}")
print(f"• Range: {south_range}\n")

print("West Division:")
print(f"• Mean Attendance: {west_mean}")
print(f"• Median Attendance: {west_median}")
print(f"• Standard Deviation: {west_std}")
print(f"• Range: {west_range}")


# Separate data by division
north_data = df[df["Division"] == "North"]["Attendance"]
south_data = df[df["Division"] == "South"]["Attendance"]
west_data = df[df["Division"] == "West"]["Attendance"]

# Perform one-way ANOVA
anova_result = f_oneway(north_data, south_data, west_data)

# Print the ANOVA results
print("One-Way ANOVA Results:")
print(f"F-statistic: {anova_result.statistic}")
print(f"P-value: {anova_result.pvalue}")

# Check for statistical significance (using a significance level of 0.05)
if anova_result.pvalue < 0.05:
    print("The mean attendance differs significantly among the three divisions.")
else:
    print(
        "There is no significant difference in mean attendance among the three divisions."
    )


# Perform Tukey's HSD post-hoc tests
tukey_results = pairwise_tukeyhsd(df["Attendance"], df["Division"], alpha=0.05)

# Check if there are any significant differences
if len(tukey_results.groupsunique) == 0:
    print("No significant differences detected.")
else:
    # Print the Tukey's HSD results
    print("Tukey's HSD Post-hoc Tests:")
    print(tukey_results)

    # Extract and print p-values and conclusions for specific comparisons
    p_value_north_south = tukey_results.pvalues[0]
    p_value_north_west = tukey_results.pvalues[1]
    p_value_south_west = tukey_results.pvalues[2]

    print("\nNorth vs. South:")
    print(f"• p-value: {p_value_north_south}")
    print(
        f"• Conclusion: {'Significant' if p_value_north_south < 0.05 else 'Not Significant'}"
    )

    print("\nNorth vs. West:")
    print(f"• p-value: {p_value_north_west}")
    print(
        f"• Conclusion: {'Significant' if p_value_north_west < 0.05 else 'Not Significant'}"
    )

    print("\nSouth vs. West:")
    print(f"• p-value: {p_value_south_west}")
    print(
        f"• Conclusion: {'Significant' if p_value_south_west < 0.05 else 'Not Significant'}"
    )


# Visualization 1: Boxplot of Attendance by Division
plt.figure(figsize=(12, 8))
sns.boxplot(x="Division", y="Attendance", data=df)
plt.title("Boxplot of Attendance by Division")
plt.xlabel("Division")
plt.ylabel("Attendance")
plt.show()

# Visualization 2: Bar chart of Mean Attendance by Division
plt.figure(figsize=(12, 8))
sns.barplot(x="Division", y="Attendance", data=df, ci=None)
plt.title("Mean Attendance by Division")
plt.xlabel("Division")
plt.ylabel("Mean Attendance")
plt.show()

# Visualization 3: Violin plot of Attendance by Division
plt.figure(figsize=(12, 8))
sns.violinplot(x="Division", y="Attendance", data=df)
plt.title("Violin Plot of Attendance by Division")
plt.xlabel("Division")
plt.ylabel("Attendance")
plt.show()

# Pairwise scatter plots
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue="Division", height=3)
plt.suptitle("Pairwise Scatter Plots of Attendance by Division", y=1.02)
plt.show()
