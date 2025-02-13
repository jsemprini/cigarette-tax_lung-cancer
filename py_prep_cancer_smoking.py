# -*- coding: utf-8 -*-
"""py_prep-Cancer-Smoking.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HSH7KvQxvDdlSieoZgaFb4N14aPRNDa4
"""

import pandas as pd

file_path = 'taxburden_1970-2019.csv'
df = pd.read_csv(file_path)
df.head()

df = df.rename(columns={"Data_Value": "y"})

# Use pandas pivot function to widen the dataframe
df_wide = df.pivot(index=['Year', 'Abbr', 'State'], columns='SubMeasureDesc', values='y')

# Reset the index to make 'Year', 'Abbr', and 'State' normal columns again
df_wide.reset_index(inplace=True)

df = df_wide

df.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a scatter plot with a regression line
sns.regplot(x="Year", y="State_Tax", data=df, scatter_kws={'alpha':0.1}, lowess=True)

# Set the title of the plot
ax.set_title('')
plt.ylabel('State Cigarette Tax ($ per pack)')  # Adding y-axis label

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a scatter plot with a regression line
sns.regplot(x="Year", y="Total_Tax", data=df, scatter_kws={'alpha':0.1}, lowess=True)

# Set the title of the plot
ax.set_title('Loess plot of Total Tax vs Year')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a scatter plot with a regression line
sns.regplot(x="Year", y="Cost_per_pack", data=df, scatter_kws={'alpha':0.1}, lowess=True)

# Set the title of the plot
ax.set_title('Loess plot of Cost_per_pack vs Year')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a scatter plot with a regression line
sns.regplot(x="Year", y="Consumption_per_capita", data=df, scatter_kws={'alpha':0.1}, lowess=True)

# Set the title of the plot
ax.set_title('Loess plot of Consumption_per_capita vs Year')
plt.ylabel('Annual Cigarette Consumption (packs per capita)')  # Adding y-axis label

# Show the plot
plt.show()

import numpy as np
import statsmodels.formula.api as smf

# Create a new DataFrame df for the regression
df = df.copy()

# Convert 'State' and 'Year' to categorical variables for fixed-effects
df['State'] = df['State'].astype('category')
df['Year'] = df['Year'].astype('category')

# Define the regression formula
formula = 'Consumption_per_capita ~ State_Tax + C(State) + C(Year)'

# Run the regression with clustered standard errors at the state level
model = smf.ols(formula, data=df)
results = model.fit(cov_type='cluster', cov_kwds={'groups': df['State']})

# Print only the State_Tax coefficient stats
print(f"State_Tax coefficient: {results.params['State_Tax']}")
print(f"State_Tax standard error: {results.bse['State_Tax']}")
print(f"State_Tax coefficient confidence interval: {results.conf_int().loc['State_Tax']}")

# Compute the marginal effect of State_Tax on Consumption_per_capita
marginal_effect = results.params['State_Tax']
print(f"\nThe marginal effect of State_Tax on Consumption_per_capita is {marginal_effect}.")

# Estimate the elasticity of Consumption_per_capita with respect to State_Tax
elasticity = np.mean(df['State_Tax'] / df['Consumption_per_capita']) * marginal_effect
print(f"The estimated elasticity of Consumption_per_capita with respect to State_Tax is {elasticity}.")

import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Year' column to numeric if it's not already
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

plt.figure(figsize=(10, 6))

# Normalize the year data for the colormap
norm = plt.Normalize(df['Year'].min(), df['Year'].max())

# Create the scatter plot
scatter = plt.scatter(x=df['State_Tax'],
                      y=df['Consumption_per_capita'],
                      c=df['Year'],
                      cmap='viridis',
                      edgecolor='w',
                      s=100,
                      norm=norm)

# Adding a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Year')

# Set labels and title
plt.xlabel('State Cigarette Tax ($ / Pack)')
plt.ylabel('Cigarette Consumption per Capita (Pack Sales)')
plt.title('')
plt.show()

import pandas as pd

# Assuming your DataFrame is named df and has columns 'State', 'Year', and 'State_Tax'

# Filter the DataFrame for the years 1970 and 2019
df_filtered = df[df['Year'].isin([1970, 2019])]

# Pivot the DataFrame to get 'State_Tax' for the years 1970 and 2019 in separate columns
df_pivot = df_filtered.pivot(index='State', columns='Year', values='State_Tax')

# Calculate the difference in 'State_Tax' between 2019 and 1970
df_pivot['Tax_Increase'] = df_pivot[2019] - df_pivot[1970]

# Sort the DataFrame by 'Tax_Increase' in ascending order
df_sorted = df_pivot.sort_values(by='Tax_Increase')

# Reset index to convert the 'State' index back to a column
df_sorted.reset_index(inplace=True)

# Display the result
print(df_sorted[['State', 'Tax_Increase']])

import pandas as pd

# Assuming your DataFrame is named df and has columns 'State', 'Year', and 'State_Tax'

# Filter the DataFrame for the years 1970 and 2019
df_filtered = df[df['Year'].isin([1970, 2019])]

# Pivot the DataFrame to get 'State_Tax' for the years 1970 and 2019 in separate columns
df_pivot = df_filtered.pivot(index='State', columns='Year', values='State_Tax')

# Reset index to convert the 'State' index back to a column
df_pivot.reset_index(inplace=True)

# Rename the columns for better readability
df_pivot.columns = ['State', 'State_Tax_1970', 'State_Tax_2019']

# Display the result
print(df_pivot)

import pandas as pd

file_path = 'LC-inc.csv'
dfinc = pd.read_csv(file_path)
dfinc['Raw_Rate'] = dfinc['Rate']

dfinc.head()

import pandas as pd

# Assuming dfinc is already defined and contains your data

# Step 1: Check if 'Rate' column is numeric
dfinc['Rate'] = pd.to_numeric(dfinc['Rate'], errors='coerce')

# Step 2: Identify non-numeric 'Rate' values (they will be converted to NaN)
non_numeric_rate = dfinc[dfinc['Rate'].isna()]

if non_numeric_rate.empty:
    print("All 'Rate' values are numeric.")
else:
    print("There are non-numeric 'Rate' values in the DataFrame.")
    print(non_numeric_rate[['State', 'Year', 'Sex', 'Rate']])

import pandas as pd

# Assuming dfinc is already defined and contains your data

# Step 1: Check if there are any missing 'Rate' values
if dfinc['Rate'].isna().any():
    print("There are missing 'Rate' values in the DataFrame.")
else:
    print("There are no missing 'Rate' values in the DataFrame.")

# Step 2: Count total number of missing 'Rate' values
total_missing_rate = dfinc['Rate'].isna().sum()
print(f"Total number of missing 'Rate' values: {total_missing_rate}")

# Step 3: Tabulate missing 'Rate' values by 'State', 'Year', and 'Sex'
missing_by_state_year_sex = dfinc[dfinc['Rate'].isna()].groupby(['State', 'Year', 'Sex', 'Type']).size().reset_index(name='MissingCount')
print(missing_by_state_year_sex)

import pandas as pd

# Assuming dfinc is already defined and contains your data

# Step 1: Check if 'Rate' column is numeric and handle non-numeric values
dfinc['Rate'] = pd.to_numeric(dfinc['Rate'], errors='coerce')

# Step 2: Sort the DataFrame by 'State', 'Type', 'Sex', and 'Year'
dfinc = dfinc.sort_values(by=['Type', 'State', 'Sex', 'Year'])

# Step 3: Define a function to interpolate missing 'Rate' values within each group
def interpolate_rate(group):
    group['Rate'] = group['Rate'].interpolate(method='linear', limit_direction='both')
    return group

# Step 4: Apply the interpolation function to each group
dfinc = dfinc.groupby(['Type', 'State', 'Sex']).apply(interpolate_rate).reset_index(drop=True)

# Step 5: Verify if there are any remaining missing values in 'Rate'
remaining_missing_rate = dfinc['Rate'].isna().sum()
print(f"Remaining number of missing 'Rate' values: {remaining_missing_rate}")

# Display the updated DataFrame
print(dfinc)

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Assuming dfinc is already defined and contains your data

# Step 1: Check if 'Rate' column is numeric and handle non-numeric values
dfinc['Rate'] = pd.to_numeric(dfinc['Rate'], errors='coerce')

# Step 2: Define the X and Y variables
X = dfinc['Year']
Y = dfinc['Rate']

# Step 3: Perform LOWESS smoothing
lowess = sm.nonparametric.lowess(Y, X, frac=0.2)  # frac is the smoothing parameter

# Step 4: Extract the smoothed values
lowess_X = lowess[:, 0]
lowess_Y = lowess[:, 1]

# Step 5: Create the scatter plot and LOWESS line
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, alpha=0.5, label='Data')
plt.plot(lowess_X, lowess_Y, color='red', label='LOWESS', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Rate')
plt.title('LOWESS Smoothing of Rate over Year')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Assuming dfinc is already defined and contains your data

# Step 1: Check if 'Rate' column is numeric and handle non-numeric values
dfinc['Raw_Rate'] = pd.to_numeric(dfinc['Raw_Rate'], errors='coerce')

# Step 2: Define the X and Y variables
X = dfinc['Year']
Y = dfinc['Raw_Rate']

# Step 3: Perform LOWESS smoothing
lowess = sm.nonparametric.lowess(Y, X, frac=0.2)  # frac is the smoothing parameter

# Step 4: Extract the smoothed values
lowess_X = lowess[:, 0]
lowess_Y = lowess[:, 1]

# Step 5: Create the scatter plot and LOWESS line
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, alpha=0.5, label='Data')
plt.plot(lowess_X, lowess_Y, color='red', label='LOWESS', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Rate')
plt.title('LOWESS Smoothing of Rate over Year')
plt.legend()
plt.show()

import pandas as pd

# Assuming df and dfinc are already defined and contain your data

# Step 1: Perform the merge operation on 'Year' and 'State'
merged_df = pd.merge(df, dfinc, on=['Year', 'State'], how='left')

# Step 2: Display the resulting DataFrame
print(merged_df)

import pandas as pd

file_path = 'state-ue.csv'
dfue = pd.read_csv(file_path)
dfue.head()

# Reshape from wide to long format
dfue_long = pd.melt(dfue, id_vars=['State'], var_name='Year', value_name='UE')

# Convert 'Year' column to numeric (if needed)
dfue_long['Year'] = pd.to_numeric(dfue_long['Year'])

# Sort by 'State' and 'Year' if needed
dfue_long = dfue_long.sort_values(by=['State', 'Year'])

# Display the resulting dataframe
print(dfue_long)

data_count_by_state = dfue_long.groupby('State').size().reset_index(name='Count')

# Display the counts
print(data_count_by_state)

dfue_long_filtered = dfue_long[dfue_long['Year'] >= 2000]
dfue_long_filtered.head()

# Select columns 'State' and '1980' to '1999'
columns_to_keep = ['State'] + [str(year) for year in range(1980, 2000)]
dfue_filtered = dfue[columns_to_keep]

# Display the filtered dataframe
print(dfue_filtered)

dfue_filtered = dfue_filtered.dropna()

# Display the dataframe after dropping NA values
print(dfue_filtered)

final_dfue = pd.merge(dfue_filtered, dfue_long_filtered, on='State')
print(final_dfue)

final_dfue = final_dfue.rename(columns={'Year': 'Cancer-Year'})

analytic_df = pd.merge(merged_df, final_dfue, on=['State', 'Cancer-Year'])

# Display the merged dataframe
print(analytic_df)

# Filter rows where Rate is NaN
na_rows = analytic_df[analytic_df['Rate'].isna()]

# Count NaN values by State and Year
na_counts = na_rows.groupby(['State', 'Year']).size().reset_index(name='NA Count')

# Display the counts where Rate is NaN
print(na_counts)

# Export dataframe to CSV
analytic_df.to_csv('analytic_df.csv', index=False)

print("DataFrame exported successfully to 'analytic_df.csv'")