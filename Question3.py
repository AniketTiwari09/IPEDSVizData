
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'IPEDS_data (1).xlsx' 
data = pd.ExcelFile(file_name)

data_sheet = data.parse('Data')

degree_data = data_sheet[
    ['Highest degree offered', 'Endowment assets (year end) per FTE enrollment (GASB)']
]

degree_data = degree_data.dropna()  
degree_data.columns = ['Highest Degree Offered', 'Endowment per FTE']

sorted_categories = (
    degree_data.groupby('Highest Degree Offered')['Endowment per FTE']
    .median()
    .sort_values()
    .index
)
degree_data['Highest Degree Offered'] = pd.Categorical(
    degree_data['Highest Degree Offered'], 
    categories=sorted_categories, 
    ordered=True
)

sns.set_theme(style="whitegrid", palette="Set2")

plt.figure(figsize=(16, 10))
boxplot = sns.boxplot(
    data=degree_data,
    x='Highest Degree Offered',
    y='Endowment per FTE',
    palette='viridis',  
    showfliers=True, 
    linewidth=2  
)

medians = degree_data.groupby('Highest Degree Offered')['Endowment per FTE'].median()
for xtick, median in enumerate(medians):
    boxplot.text(
        xtick, 
        median + 1000, 
        f'{int(median):,}', 
        horizontalalignment='center',
        fontsize=11,
        color='white',
        bbox=dict(facecolor='black', edgecolor='none', alpha=0.8) 
    )

plt.title('Impact of Degree Type on Endowment Assets per FTE', fontsize=20, fontweight='bold', color='#4a4a4a')
plt.xlabel('Highest Degree Offered', fontsize=16, color='#4a4a4a')
plt.ylabel('Endowment Assets per FTE Enrollment ($)', fontsize=16, color='#4a4a4a')
plt.xticks(rotation=30, fontsize=13, ha='right', color='#4a4a4a')  
plt.yticks(fontsize=13, color='#4a4a4a')
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5, color='#b0b0b0')

plt.tight_layout()

plt.show()
