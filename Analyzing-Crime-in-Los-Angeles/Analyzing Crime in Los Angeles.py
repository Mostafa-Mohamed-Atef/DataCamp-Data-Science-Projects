import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)
data = pd.DataFrame(crimes, columns=['DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA NAME',
       'Crm Cd Desc', 'Vict Age', 'Vict Sex', 'Vict Descent', 'Weapon Desc',
       'Status Desc', 'LOCATION', 'HOUR OCC'])
#Finding the frequencies of crimes by the hour of occurrence
sns.countplot(data=data,x="HOUR OCC")
plt.show()
peak_crime_hours = 12 #after seeing the plot and knowing which is the highest
hours_to_retain = [22,23,0,1,2,3,4]
#Identifying the area with the most night crime
bool_data = data[data['HOUR OCC'].isin(hours_to_retain)]
print(bool_data)
grouped = data.groupby("AREA NAME")["HOUR OCC"].value_counts().sort_values(ascending=False)
peak_night_crime_location = grouped.index[0][0]
print(peak_night_crime_location)
#Crimes by age group
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf] 
age_labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']
crimes["Age Bracket"] = pd.cut(crimes['Vict Age'], bins=age_bins,labels=age_labels)
victim_ages = crimes['Age Bracket'].value_counts()
print(victim_ages)


