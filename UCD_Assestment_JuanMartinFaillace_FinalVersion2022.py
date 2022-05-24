import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

Investments = pd.read_csv(r'C:\Users\juan.faillace\OneDrive - Accenture\Desktop\Curso UCD\Assestment\UCD_Final Assestment\Direct Investment Flows.csv')
Investments


Investments_Value = Investments.sort_values(by = 'VALUE', ascending=False)
Investments_Value

Investments_Value.isna()

Investments_Value['Impact'] = np.where(Investments_Value['VALUE'] > 0, 'Positive', 'Negative')
Investments_Value.dropna(inplace = True)
Investments_Value

Continent = pd.read_csv(r'C:\Users\juan.faillace\OneDrive - Accenture\Desktop\Curso UCD\Assestment\UCD_Final Assestment\Country-Continent.csv')
Continent

Investment_Continent=Investments_Value.merge(Continent,on='Geographic Location')
Investment_Continent


Investment_Continent.columns

Investment_Continent_2= Investment_Continent[['Year','Continent','Type of Investment','VALUE']]
Investment_Continent_2


Investment_Continent_2_Year=Investment_Continent_2.set_index('Year')


Investment_Continent_Year_Group = Investment_Continent_2_Year.groupby(['Year','Continent'])['VALUE'].sum().to_frame()
Investment_Continent_Year_Group

Investment_Continent_Year_Group_DF = Investment_Continent_Year_Group.unstack().T
Investment_Continent_Year_Group_DF.head()

Investment_Continent_Year_Group_DF.reset_index(inplace = True)
Investment_Continent_Year_Group_DF = Investment_Continent_Year_Group_DF.drop(['level_0'], axis=1)
Investment_Continent_Year_Group_DF.set_index('Continent', inplace=True)
Investment_Continent_Year_Group_DF

Investment_Continent_Year_Group_DF = Investment_Continent_Year_Group_DF[[2018,2019,2020]]
Investment_Continent_Year_Group_DF

x = np.arange(8)
for i in range(3):
    y1 = Investment_Continent_Year_Group_DF[2018].to_list()
    y2 = Investment_Continent_Year_Group_DF[2019].to_list()
    y3 = Investment_Continent_Year_Group_DF[2020].to_list()

width = 0.2

plt.rcParams["figure.figsize"] = [15, 15]
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x,  ['Africa', 'Asia', 'Central America', 'Europe', 'North America','Oceania', 'Other', 'South America'])
plt.xlabel("Continents")
plt.ylabel("EUR Millions")
plt.legend(Investment_Continent_Year_Group_DF.columns.to_list())
plt.show();


from bs4 import BeautifulSoup 
import requests 

r = requests.get('https://www.rte.ie/news/business/2022/0512/1297579-cso-inflation-figures/')
type(r)


from bs4 import BeautifulSoup as bs

News_Inflation = bs(r.content, 'lxml')

News_Inflation.title

News_Inflation.title.text
