from bs4 import BeautifulSoup
import requests
import pandas as pd



url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
soup = BeautifulSoup(data,'html5lib')
tables = soup.find_all('table')
print(len(tables))
for index,table in enumerate(tables):
    if("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

dataframe_list = pd.read_html(url, flavor='bs4')
total = len(dataframe_list)
print(len(dataframe_list))
pd.read_html(url, flavor='bs4')[0:total]
df1 = pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
df2 = pd.read_html(url, match="Population by region", flavor='bs4')[0]
print(df2)






