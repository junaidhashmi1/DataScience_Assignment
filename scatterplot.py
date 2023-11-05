import pandas as pd

# Read the data from the CSV file with 'ISO-8859-1' encoding
data = pd.read_csv('Global_education.csv', encoding='ISO-8859-1')
# Display the first few rows of the data
print(data.head())
# Check data types and missing values
print(data.info())
import matplotlib.pyplot as plt

# Set the size of the figure
plt.figure(figsize=(12, 8))

# Define the variables for the scatter plot
x = data['Longitude']
y = data['Latitude ']
c = data['Completion_Rate_Primary_Male']  # Use a third variable for the colormap
cmap = 'viridis'  # Choose a colormap (you can change it to other colormaps)

# Create the scatter plot with a colormap
plt.scatter(x, y, c=c, cmap=cmap, s=50, alpha=0.7)

# Add colorbar for the third variable
cbar = plt.colorbar()
cbar.set_label('Completion Rate Primary Male')

# Set labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Scatter Plot: Latitude vs. Longitude with Completion Rate')

plt.show()

# Bar Plot

primary_male_column = 'OOSR_Primary_Age_Male'
primary_female_column = 'OOSR_Primary_Age_Female'

# Create a figure and axis
plt.figure(figsize=(12, 6))
ax = plt.subplot(111)

# Number of country names to skip between labels
skip = 10

# Calculate the x-axis values (positions for bars)
x = range(len(data))

# Plot the bar for 'OOSR_Primary_Age_Male'
bar_width = 0.4  # Adjust the width of the bars
plt.bar(x, data[primary_male_column], label=primary_male_column, width=bar_width, align='center')

# Plot the bar for 'OOSR_Primary_Age_Female' next to 'OOSR_Primary_Age_Male'
plt.bar([pos + bar_width for pos in x], data[primary_female_column], label=primary_female_column, width=bar_width, align='center')

# Customize the plot
plt.xlabel('Countries and areas')
plt.ylabel('Counts')
plt.title('Bar Plot: OOSR Primary Age (Male vs. Female)')

# Set x-axis labels for every 'skip' data points
x_labels = data['Countries and areas'][::skip]
plt.xticks(x[::skip], x_labels, rotation=45, ha='right')

plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
# Line Plot

import matplotlib.pyplot as plt

# Select the columns for the completion rates
completion_columns = ['Completion_Rate_Primary_Male', 'Completion_Rate_Primary_Female',
                      'Completion_Rate_Lower_Secondary_Male', 'Completion_Rate_Lower_Secondary_Female',
                      'Completion_Rate_Upper_Secondary_Male', 'Completion_Rate_Upper_Secondary_Female']

# Create a figure and axis
plt.figure(figsize=(12, 6))
ax = plt.subplot(111)

# Number of country names to skip between labels
skip = 10

# Loop through each completion column and plot it
for column in completion_columns:
    plt.plot(data.index, data[column], label=column)

# Customize the plot
plt.xlabel('Countries and areas')
plt.ylabel('Completion Rate')
plt.title('Completion Rates Over Different Education Levels')

# Set x-axis labels for every 'skip' data points
x_labels = data['Countries and areas'][::skip]
plt.xticks(data.index[::skip], x_labels, rotation=45, ha='right')

plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
