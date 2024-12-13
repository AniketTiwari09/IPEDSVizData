import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

file_name = 'IPEDS_data (1).xlsx'  
data = pd.ExcelFile(file_name)

data_sheet = data.parse('Data')

location_data = data_sheet[
    ['Latitude location of institution', 
     'Longitude location of institution', 
     'Percent of freshmen receiving state/local grant aid']
]

location_data = location_data.dropna()  
location_data.columns = ['Latitude', 'Longitude', 'State/Local Grant Aid (%)']

plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.STATES, linestyle='--')

scatter = plt.scatter(
    location_data['Longitude'], 
    location_data['Latitude'], 
    c=location_data['State/Local Grant Aid (%)'], 
    cmap='YlOrRd', 
    s=50, 
    alpha=0.7, 
    transform=ccrs.PlateCarree()
)

cbar = plt.colorbar(scatter, orientation='vertical', pad=0.05)
cbar.set_label('State/Local Grant Aid (%)')

plt.title('Geographical Distribution of State/Local Grant Aid', fontsize=16)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.tight_layout()

plt.show()
