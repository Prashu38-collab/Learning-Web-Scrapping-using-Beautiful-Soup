# extract dtaa from a table 
import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://ticker.finology.in/market/52-week-high"
r=requests.get(url)
print(r)
soup=BeautifulSoup(r.text,"lxml")
# extracting headers
headers=[th.get_text(strip=True) for th in soup.table.find_all("th")]
print(headers)

# extracting rows:
rows=[]
for tr in soup.table.find_all("tr")[1:]:
    data=[td.get_text(strip=True) for td in tr.find_all("td")]
    if data:
        rows.append(data)
print(rows)
print(len(rows))

# creating a dataframe
df=pd.DataFrame(rows,columns=headers)
print(df)

df.to_excel('ipo_share.xlsx')
print("done")