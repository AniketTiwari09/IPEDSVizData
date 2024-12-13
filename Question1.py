import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'IPEDS_data (1).xlsx'  
data = pd.ExcelFile(file_name)

data_sheet = data.parse('Data')

financial_data = data_sheet[
    ['Percent of freshmen  receiving federal grant aid', 'Percent of freshmen receiving federal student loans']
]

financial_data = financial_data.dropna()  
financial_data.columns = ['Federal Grant Aid (%)', 'Federal Student Loans (%)']

plt.figure(figsize=(10, 6))
sns.regplot(
    data=financial_data, 
    x='Federal Grant Aid (%)', 
    y='Federal Student Loans (%)', 
    scatter_kws={'alpha': 0.5}, 
    line_kws={'color': 'red'}
)

plt.title('Relationship Between Federal Grants and Student Loans', fontsize=16)
plt.xlabel('Percent of Freshmen Receiving Federal Grant Aid', fontsize=14)
plt.ylabel('Percent of Freshmen Receiving Federal Student Loans', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.tight_layout()

plt.show()
