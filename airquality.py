import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the file
file_path = '/Users/saurabhkankekar/Downloads/air+quality/Question1.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Clean the data to remove invalid or placeholder values
cleaned_data = data[(data['Avg_CO'] > -200) & (data['Avg_NOx'] > -200)]

# Generate the scatter plot with a trendline
sns.regplot(x='Avg_CO', y='Avg_NOx', data=cleaned_data, line_kws={"color": "red"})
plt.title('Correlation between Average CO and NOx Levels')
plt.xlabel('Average CO (mg/m³)')
plt.ylabel('Average NOx (ppb)')

# Show the plot
plt.show()

# Calculate the correlation matrix
correlation_coefficient = cleaned_data[['Avg_CO', 'Avg_NOx']].corr().iloc[0, 1]

print(f"The correlation coefficient (r) is: {correlation_coefficient}")


print(data['Avg_CO'])  # Replace 'Avg_CO' with your column name

#Test

