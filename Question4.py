import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'IPEDS_data (1).xlsx'
data = pd.ExcelFile(file_path)

data_sheet = data.parse('Data')

religion_data = data_sheet[
    ['Religious affiliation', 'Percent of freshmen receiving Pell grants']
]

religion_data = religion_data.dropna()  
religion_data.columns = ['Religious Affiliation', 'Pell Grant (%)']

avg_religion = religion_data.groupby('Religious Affiliation')['Pell Grant (%)'].mean().sort_values()

sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 8))
bar = sns.barplot(
    x=avg_religion.index, 
    y=avg_religion.values, 
    palette='coolwarm'
)

for xtick, avg in enumerate(avg_religion.values):
    bar.text(xtick, avg + 2, f'{int(avg):,}', 
             horizontalalignment='center', fontsize=10, color='black')

plt.title('Average Pell Grants by Religious Affiliation', fontsize=18, fontweight='bold')
plt.xlabel('Religious Affiliation', fontsize=14)
plt.ylabel('Average Percent of Freshmen Receiving Pell Grants', fontsize=14)
plt.xticks(rotation=45, fontsize=12, ha='right') 
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
