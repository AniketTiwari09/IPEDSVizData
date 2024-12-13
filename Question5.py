import pandas as pd
import matplotlib.pyplot as plt

file_name = 'IPEDS_data (1).xlsx'  
data = pd.ExcelFile(file_name)

data_sheet = data.parse('Data')

financial_data = data_sheet[
    ['Percent of freshmen receiving student loan aid',
     'Percent of freshmen receiving institutional grant aid',
     'Endowment assets (year end) per FTE enrollment (GASB)']
]

financial_data = financial_data.dropna()  
financial_data.columns = ['Student Loan Aid (%)', 'Institutional Grant Aid (%)', 'Endowment per FTE']

bins = [0, 5000, 20000, 50000, 100000, financial_data['Endowment per FTE'].max()]
labels = ['< $5K', '$5K - $20K', '$20K - $50K', '$50K - $100K', '> $100K']
financial_data['Endowment Level'] = pd.cut(financial_data['Endowment per FTE'], bins=bins, labels=labels)

grouped_data = financial_data.groupby('Endowment Level').mean()

grouped_data[['Student Loan Aid (%)', 'Institutional Grant Aid (%)']].plot(
    kind='bar',
    figsize=(12, 8),
    color=['#1f77b4', '#ff7f0e'],
    width=0.7
)

plt.title('Comparison of Financial Aid by Endowment Level', fontsize=18, fontweight='bold')
plt.xlabel('Endowment Level (per FTE)', fontsize=14)
plt.ylabel('Percentage of Freshmen', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title='Type of Aid', fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
