import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

counted2015 = pd.read_csv("data/2015.csv")
counted2016 = pd.read_csv("data/2016.csv")
popData = pd.read_csv("data/popData.csv")
popData.set_index('Category', inplace=True)

counted2015['gender'].value_counts().plot(kind='bar', title='2015 Police Killings by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

counted2016['gender'].value_counts().plot(kind='bar', title='2016 Police Killings by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

counted2015['raceethnicity'].value_counts().plot(kind='bar', title='2015 Police Killings by Race')
plt.xlabel('Race')
plt.ylabel('Count')
plt.show()

counted2016['raceethnicity'].value_counts().plot(kind='bar', title='2016 Police Killings by Race')
plt.xlabel('Race')
plt.ylabel('Count')
plt.show()

combined = pd.crosstab(counted2015['raceethnicity'],counted2015['gender'])
combined.plot.bar(stacked='true', title='Police Killings by Race/Gender')
plt.show()

gender_counts_2015 = counted2015['gender'].value_counts()
gender_counts_2015.name = '2015'
gender_counts_2016 = counted2016['gender'].value_counts()
gender_counts_2016.name = '2016'
gender_counts_2016.loc['Non-conforming'] = 0
gender_combined = pd.concat([gender_counts_2015,gender_counts_2016], axis=1)
gender_combined = gender_combined.astype('float64')
popData = popData.astype('float64')
gender_combined.loc['Male']['2015'] = (gender_combined.loc['Male']['2015']*1000000) / popData.loc['Male']
gender_combined.loc['Male']['2016'] = (gender_combined.loc['Male']['2016']*1000000) / popData.loc['Male']
gender_combined.loc['Female']['2015'] = (gender_combined.loc['Female']['2015']*1000000) / popData.loc['Female']
gender_combined.loc['Female']['2016'] = (gender_combined.loc['Female']['2016']*1000000) / popData.loc['Female']
gender_combined.loc['Non-conforming']['2015'] = gender_combined.loc['Non-conforming']['2015']*0.0
gender_combined.plot.bar(stacked=False)
plt.xlabel('Gender')
plt.ylabel('Rate per Million')
plt.title('Death Rate by Police by Gender')
plt.show()

race_counts_2015 = counted2015['raceethnicity'].value_counts()
race_counts_2015.name = '2015'
race_counts_2015.astype('float64')
race_counts_2015 = race_counts_2015 * 1000000
race_pop_2015 = pd.Series([popData.loc['White'].values[0],
                           popData.loc['Black'].values[0],
                           popData.loc['Hispanic'].values[0],
                           popData.loc['Asian'].values[0]+popData.loc['Pacific Islander'].values[0],
                           popData.loc['Multiracial'].values[0],
                           popData.loc['American Indian'].values[0],
                           popData.loc['Other'].values[0],
                           popData.loc['Other'].values[0]],
                          index=['White', 'Black', 'Hispanic/Latino', 'Asian/Pacific Islander', 'Unknown',
                                 'Native American', 'Arab-American', 'Other'])
race_counts_2015 = pd.Series.div(race_counts_2015, race_pop_2015)

race_counts_2016 = counted2016['raceethnicity'].value_counts()
race_counts_2016.name = '2016'
race_counts_2016.astype('float64')
race_counts_2016 = race_counts_2016 * 1000000
race_counts_2016 = pd.Series.div(race_counts_2016, race_pop_2015)
race_combined = pd.concat([race_counts_2015, race_counts_2016], axis=1)
race_combined.plot.bar(stacked=False)
plt.title('Death Rate by Police By Race')
plt.xlabel('Race')
plt.ylabel('Rate per Million')
plt.legend(['2015', '2016'])
plt.show()
