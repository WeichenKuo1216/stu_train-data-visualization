import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\weiii\\OneDrive\\文件\\大三\\112-2\\政治學的資料探勘與機器學習\\stu-sch-1 - train.csv")

# Print the DataFrame
print(df)

#statistic summary
print(df.describe())

#barplot 
def barplot(variable):
	variable_counts = df[variable].value_counts()
	categories = variable_counts.index
	values = variable_counts.values
	plt.bar(categories, values)

	# Add title and labels
	plt.title('Bar Plot')
	plt.xlabel(variable)
	plt.ylabel('Count')
	# Show plot
	plt.show()
for variables in df.columns:
	barplot(variables)


