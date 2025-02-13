# -*- coding: utf-8 -*-
"""py-analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RHuDTJWHUZPKpEN2VPNQenlIvLtjz--c
"""

#Begin analysis for PHR
import pandas as pd

file_path = 'analytic_df.csv'
df = pd.read_csv(file_path)
df.head()

import pandas as pd

file_path = 'elastax-group.csv'
elastax_df = pd.read_csv(file_path)
elastax_df.head()

import pandas as pd

# Assuming df is your main DataFrame and elastax_df is the DataFrame you want to merge

# Merge df with elastax_df on the 'State' column
df = pd.merge(df, elastax_df, on='State', how='left')

# Display the merged DataFrame
print(df)

# Printing unique values of 'Sex' column
df['Sex'] = df['Sex'].str.strip()  # Remove leading and trailing whitespace

unique_sex = df['Sex'].unique()
print(unique_sex)

# Rename 'Year' to 'Tax_Year'
df.rename(columns={'Year': 'Tax_Year'}, inplace=True)


# Rename 'Cancer_Year' to 'Year'
df['Year'] = df['Cancer-Year']

df.head()

df.to_csv('for_r.csv', index=False)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting with FacetGrid
g = sns.FacetGrid(df, col='Sex', hue='Group', height=5, aspect=1.5)
g.map_dataframe(sns.lineplot, x='Year', y='Raw_Rate', marker='o')

# Adding titles and labels
g.set_axis_labels('Year', 'Rate')
g.set_titles(col_template="{col_name}")
g.add_legend(title='')

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_xlim(2000, 2019)
        ax.set_xticks(range(1999, 2020, 2))

# Show the plot
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting with FacetGrid
g = sns.FacetGrid(df, col='Sex', hue='Group', height=5, aspect=1.5)
g.map_dataframe(sns.lineplot, x='Year', y='Raw_Rate', marker='o')

# Adding titles and labels
g.set_axis_labels('Year', 'Rate')
g.set_titles(col_template="{col_name}")

# Adjusting the y-axis and x-axis
for ax in g.axes.flat:
    ax.set_ylim(0, 140)
    ax.set_yticks(range(0, 141, 10))
    ax.set_xlim(2000, 2019)
    ax.set_xticks(range(1999, 2020, 2))

# Move the legend to the final subplot
final_ax = g.axes.flat[-1]
final_ax.legend(title='', loc='upper left', bbox_to_anchor=(-2, 1), frameon=False)

# Show the plot
plt.show()

# Get the unique types
types = df['Type'].unique()

# Loop through each type and create a separate plot
for t in types:
    df_subset = df[df['Type'] == t]

    # Create a FacetGrid for the current type, faceted by Sex
    g = sns.FacetGrid(df_subset, col="Sex", height=5, aspect=1.5)
    g.map(sns.lineplot, 'Year', 'Raw_Rate', 'Group', marker='o')

    # Adding titles and labels
    g.set_axis_labels("Year", "Raw_Rate")
    g.set_titles(col_template="{col_name}")
    g.add_legend(title='')
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle(f'Rate Over Years by Group - {t}', fontsize=16)

    # Set y-axis range and ticks
    for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))

    # Set y-axis range and ticks
    for ax in g.axes.flat:
        ax.set_xlim(2000, 2019)
        ax.set_xticks(range(1999, 2020, 2))

    # Show the plot
    plt.show()

df_sex = df[df['Sex'] != 'Male and female']
df_all = df[df['Sex'] == 'Male and female']

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = df_all

# Plotting with FacetGrid
g = sns.FacetGrid(df, col='Sex', hue='Group', height=5, aspect=1.5)
g.map_dataframe(sns.lineplot, x='Year', y='Raw_Rate', marker='o')

# Adding titles and labels
g.set_axis_labels('', 'Rate')
g.set_titles(col_template="{col_name}")

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_xlim(1999, 2020)
        ax.set_xticks(range(2001, 2020, 2))

        # Move the legend to the final subplot
final_ax = g.axes.flat[-1]
final_ax.legend(title='', loc='upper left', bbox_to_anchor=(0, 1), frameon=False)


# Show the plot
plt.show()

# Get unique types
types = df_all['Type'].unique()

# Loop over each type and create a FacetGrid plot
for t in types:
    df_filtered = df_all[df_all['Type'] == t]

    # Plotting with FacetGrid
    g = sns.FacetGrid(df_filtered, col='Sex', hue='Group', height=5, aspect=1.5)
    g.map_dataframe(sns.lineplot, x='Year', y='Raw_Rate', marker='o')

    # Adding titles and labels
    g.set_axis_labels('', 'Rate')
    g.set_titles(col_template="{col_name} - " + t)

    # Set y-axis range and ticks
    for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))
        ax.set_xlim(1999, 2020)
        ax.set_xticks(range(2000, 2021, 2))

    # Move the legend to the final subplot
    final_ax = g.axes.flat[-1]
    final_ax.legend(title='', loc='upper left', bbox_to_anchor=(0, 1), frameon=False)

    # Show the plot
    plt.show()

df = df_sex

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting with FacetGrid
g = sns.FacetGrid(df, col='Sex', hue='Group', height=5, aspect=1.5)
g.map_dataframe(sns.lineplot, x='Year', y='Raw_Rate', marker='o')

# Adding titles and labels
g.set_axis_labels('Year', 'Rate')
g.set_titles(col_template="{col_name}")

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))

    # Set y-axis range and ticks
for ax in g.axes.flat:
        ax.set_xlim(2000, 2019)
        ax.set_xticks(range(1999, 2020, 2))
    # Move the legend to the final subplot
final_ax = g.axes.flat[-1]
final_ax.legend(title='', loc='upper left', bbox_to_anchor=(-1, 1), frameon=False)

# Show the plot
plt.show()

df = df[df['Type'] != 'Adenocarcinoma']
df = df[df['Type'] != 'Other']


# Get the unique types
types = df['Type'].unique()
df = df.sort_values(by=['Group', 'Sex'])

# Loop through each type and create a separate plot
for t in types:
    df_subset = df[df['Type'] == t]

    # Create a FacetGrid for the current type, faceted by Sex
    g = sns.FacetGrid(df_subset, col="Sex", height=5, aspect=1.5)
    g.map(sns.lineplot, 'Year', 'Raw_Rate', 'Group', marker='o')

    # Adding titles and labels
    g.set_axis_labels("", "Incidence")
    g.set_titles(col_template="{col_name}")
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle(f'{t}', fontsize=16)

    # Set y-axis range and ticks
    for ax in g.axes.flat:
        ax.set_ylim(0, 140)
        ax.set_yticks(range(0, 141, 10))

    # Set y-axis range and ticks
    for ax in g.axes.flat:
        ax.set_xlim(1999.5, 2019.5)
        ax.set_xticks(range(2000, 2020, 2))
    # Move the legend to the final subplot
    final_ax = g.axes.flat[-1]
    final_ax.legend(title='', loc='upper left', bbox_to_anchor=(-1, 1), frameon=False)

    # Show the plot
    plt.show()

#Import data


import pandas as pd
from io import StringIO

data = """
State	Elasticity	Lower_CI	Upper_CI	Tax_Change
Alabama	-0.37714	-0.43052	-0.32377	Low
Alaska	-0.36708	-0.3977	-0.33646	High
Arizona	-0.51108	-0.54735	-0.47481	High
Arkansas	-0.39337	-0.43429	-0.35245	Low
California	-0.5986	-0.64516	-0.55204	High
Colorado	-0.4885	-0.54003	-0.43697	Low
Connecticut	-0.45927	-0.48406	-0.43448	High
Delaware	-0.22843	-0.28294	-0.17392	High
District of Columbia	-0.60602	-0.63923	-0.5728	High
Florida	-0.55354	-0.60019	-0.50689	Low
Georgia	-0.6359	-0.71673	-0.55506	Low
Hawaii	-0.32545	-0.35881	-0.29208	High
Idaho	-0.46284	-0.51044	-0.41525	Low
Illinois	-0.49042	-0.51496	-0.46587	High
Indiana	-0.30527	-0.33247	-0.27807	Low
Iowa	-0.37616	-0.40974	-0.34258	Low
Kansas	-0.49773	-0.53665	-0.4588	Low
Kentucky	-0.20091	-0.23312	-0.16871	Low
Louisiana	-0.40118	-0.43568	-0.36668	Low
Maine	-0.38919	-0.41212	-0.36626	High
Maryland	-0.43756	-0.46344	-0.41167	High
Massachusetts	-0.51483	-0.53738	-0.49229	High
Michigan	-0.36588	-0.39055	-0.34121	High
Minnesota	-0.4399	-0.46862	-0.41119	High
Mississippi	-0.32239	-0.36455	-0.28023	Low
Missouri	-0.52601	-0.65787	-0.39414	Low
Montana	-0.32472	-0.35715	-0.29229	High
Nebraska	-0.47259	-0.52742	-0.41775	Low
Nevada	-0.59992	-0.63942	-0.56042	High
New Hampshire	-0.35715	-0.38888	-0.32542	High
New Jersey	-0.51932	-0.54284	-0.49581	High
New Mexico	-0.48869	-0.5187	-0.45868	Low
New York	-0.61077	-0.64494	-0.57661	High
North Carolina	-0.34434	-0.38124	-0.30743	Low
Northakota	-0.35378	-0.39545	-0.31211	Low
Ohio	-0.35576	-0.37831	-0.33321	Low
Oklahoma	-0.30135	-0.34754	-0.25516	High
Oregon	-0.43634	-0.47304	-0.39965	Low
Pennsylvania	-0.34818	-0.37277	-0.32359	High
Rhode Island	-0.43649	-0.46146	-0.41153	High
South Carolina	-0.31836	-0.36505	-0.27167	Low
Southakota	-0.3658	-0.39126	-0.34034	Low
Tennessee	-0.3888	-0.42313	-0.35446	Low
Texas	-0.57516	-0.62112	-0.52919	Low
Utah	-0.4372	-0.46899	-0.40542	High
Vermont	-0.41295	-0.43448	-0.39141	High
Virginia	-0.24075	-0.28038	-0.20113	Low
Washington	-0.54415	-0.58552	-0.50279	High
West Virginia	-0.1068	-0.14111	-0.0725	Low
Wisconsin	-0.36855	-0.3943	-0.34279	High
Wyoming	-0.37552	-0.42536	-0.32568	Low
"""

# Use StringIO to convert the string data into a file-like object
data = StringIO(data)

# Read the data into a pandas DataFrame
df = pd.read_csv(data, sep='\t')
print(df.head())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the error margins
df['Error'] = df['Elasticity'] - df['Lower_CI']
df['Error_high'] = df['Upper_CI'] - df['Elasticity']

# Sort the DataFrame by Elasticity
df = df.sort_values(by='Elasticity', ascending=False)

# Create the errorbar plot
plt.figure(figsize=(10, 6))

# Use seaborn pointplot function to include error bars
sns.pointplot(x='State', y='Elasticity', hue='Tax_Change', data=df, dodge=True, join=False, capsize=.1, errwidth=1, ci=None, markers=["o", "s", "D", "^", "v"], scale=.75)

# Get the colors used by seaborn
palette = sns.color_palette()
hue_order = df['Tax_Change'].unique()

# Adding error bars manually for confidence intervals
for i, row in df.iterrows():
    hue_index = list(hue_order).index(row['Tax_Change'])
    plt.errorbar(row['State'], row['Elasticity'], yerr=[[row['Error']], [row['Error_high']]], fmt='none', color=palette[hue_index], capsize=5, alpha=0.7)

# Customize the plot
plt.title('')
plt.xlabel('')
plt.ylabel('Elasticity of Demand')
plt.ylim(-1, 0)
plt.xticks(rotation=90)
plt.legend(title='State Cigarette Tax Change (1970-2019)', loc='upper right', frameon=False)
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)  # Only horizontal grid lines

# Display the plot
plt.tight_layout()
plt.show()

#Import data

import pandas as pd
from io import StringIO

data = """
Group	Period	Elasticity	Lower_CI	Upper_CI
High E-Low D	1970-1974	1.19122E-01	7.37583E-03	2.30869E-01
High E-Low D	1975-1979	-2.05934E-01	-4.62576E-01	5.07082E-02
High E-Low D	1980-1984	-1.79907E-01	-2.50673E-01	-1.0914E-01
High E-Low D	1985-1989	-3.71777E-01	-5.43678E-01	-1.99875E-01
High E-Low D	1990-1994	-7.69681E-02	-1.55298E-01	1.36129E-03
High E-Low D	1995-1999	-2.24425E-01	-3.14111E-01	-1.34739E-01
High E-Low D	2000-2004	-7.50351E-02	-1.50681E-01	6.10479E-04
High E-Low D	2005-2009	-3.09202E-01	-3.96374E-01	-2.22029E-01
High E-Low D	2010-2014	-1.193900806	-1.861166487	-5.26635E-01
High E-Low D	2015-2019	-5.11876E-01	-6.40982E-01	-3.8277E-01
Low E-Low D	1970-1974	1.27605E-01	-2.84873E-02	2.83697E-01
Low E-Low D	1975-1979	-1.38469E-01	-2.26267E-01	-5.06716E-02
Low E-Low D	1980-1984	-2.55346E-01	-3.88097E-01	-1.22595E-01
Low E-Low D	1985-1989	-2.05941E-01	-3.00336E-01	-1.11546E-01
Low E-Low D	1990-1994	-5.95529E-02	-1.20414E-01	1.30868E-03
Low E-Low D	1995-1999	-2.60563E-01	-4.4372E-01	-7.74054E-02
Low E-Low D	2000-2004	-1.88397E-01	-2.44146E-01	-1.32648E-01
Low E-Low D	2005-2009	-1.91235E-01	-2.36877E-01	-1.45593E-01
Low E-Low D	2010-2014	-1.39648E-01	-1.99471E-01	-7.98248E-02
Low E-Low D	2015-2019	-2.63964E-01	-3.42797E-01	-1.85132E-01
High E-High D	1970-1974	-1.26946E-01	-2.48181E-01	-5.71137E-03
High E-High D	1975-1979	-3.75471E-01	-4.5897E-01	-2.91972E-01
High E-High D	1980-1984	-2.65199E-01	-3.53038E-01	-1.7736E-01
High E-High D	1985-1989	-1.70136E-01	-2.26113E-01	-1.14158E-01
High E-High D	1990-1994	-2.60928E-01	-3.18076E-01	-2.03781E-01
High E-High D	1995-1999	-2.04571E-01	-2.59819E-01	-1.49323E-01
High E-High D	2000-2004	-2.92262E-01	-3.50808E-01	-2.33717E-01
High E-High D	2005-2009	-2.98785E-01	-3.70953E-01	-2.26617E-01
High E-High D	2010-2014	-4.58318E-01	-5.68115E-01	-3.48521E-01
High E-High D	2015-2019	-3.33694E-01	-4.41574E-01	-2.25814E-01
Low E-High D	1970-1974	4.3731E-02	-2.7796E-02	1.15258E-01
Low E-High D	1975-1979	-1.26979E-02	-1.05843E-01	8.04475E-02
Low E-High D	1980-1984	-1.79976E-01	-2.47835E-01	-1.12117E-01
Low E-High D	1985-1989	-3.0363E-01	-3.89563E-01	-2.17697E-01
Low E-High D	1990-1994	-1.52511E-01	-2.39783E-01	-6.52395E-02
Low E-High D	1995-1999	-1.73903E-01	-2.60982E-01	-8.68228E-02
Low E-High D	2000-2004	-2.27902E-01	-2.73667E-01	-1.82138E-01
Low E-High D	2005-2009	-1.58958E-01	-2.37227E-01	-8.06893E-02
Low E-High D	2010-2014	-2.55715E-01	-4.44192E-01	-6.72386E-02
Low E-High D	2015-2019	-3.15729E-01	-5.81954E-01	-4.95049E-02

"""

# Use StringIO to convert the string data into a file-like object
data = StringIO(data)

# Read the data into a pandas DataFrame
df = pd.read_csv(data, sep='\t')
print(df.head())

# Subset the data to exclude specific periods
df = df[~df['Period'].isin(['2010-2014', '2015-2019'])]

# Check the resulting DataFrame
print(df)

#Import data

import pandas as pd
from io import StringIO

data = """
State	Group	Increase
Arizona	High	1.9
California	High	2.77
Connecticut	High	4.19
District of Columbia	High	4.9
Illinois	High	1.86
Maryland	High	1.94
Massachusetts	High	3.39
Minnesota	High	3.498
Nevada	High	1.7
New Jersey	High	2.56
New York	High	4.23
Rhode Island	High	4.12
Utah	High	1.62
Vermont	High	2.96
Washington	High	2.915
Colorado	High	0.79
Florida	High	1.189
Georgia	High	0.29
Idaho	High	0.5
Kansas	High	1.21
Missouri	High	0.08
Nebraska	High	0.56
New Mexico	High	1.54
Oregon	High	1.29
Texas	High	1.255
Alaska	Low	1.92
Delaware	Low	1.99
Hawaii	Low	3.12
Maine	Low	1.88
Michigan	Low	1.89
Montana	Low	1.62
New Hampshire	Low	1.71
Oklahoma	Low	1.9
Pennsylvania	Low	2.42
Wisconsin	Low	2.38
Alabama	Low	0.555
Arkansas	Low	1.0275
Indiana	Low	0.935
Iowa	Low	1.26
Kentucky	Low	1.075
Louisiana	Low	1
Mississippi	Low	0.59
North Carolina	Low	0.43
North Dakota	Low	0.33
Ohio	Low	1.5
South Carolina	Low	0.51
South Dakota	Low	1.41
Tennessee	Low	0.49
Virginia	Low	0.275
West Virginia	Low	1.13
Wyoming	Low	0.54
"""

# Use StringIO to convert the string data into a file-like object
data = StringIO(data)

# Read the data into a pandas DataFrame
df = pd.read_csv(data, sep='\t')
print(df.head())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sort the DataFrame by Elasticity
df = df.sort_values(by='Increase', ascending=False)

hue_order = ['Low', 'High']  # Flipping the order of 'A' and 'B'

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='State', y='Increase', hue='Group', data=df, hue_order=hue_order)

# Set labels and title
plt.xlabel("")
plt.ylabel("Cigarette Tax Increase (1970-2019) ($)")
plt.title("")
plt.xticks(rotation=90, fontsize=8)
plt.legend(title="Elasticity Group", frameon=False)

# Show the plot
plt.show()