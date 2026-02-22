import requests;
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
print(r)
print(r.text)
soup=BeautifulSoup(r.text,"lxml")
# finding table
tables=soup.find("table")
print(tables)

# finding headers
head=soup.table.find_all("th")
print(head)

# extracting text 
headers=[ i.get_text(strip=True) for i in head]
print(headers)


#add rows of tables:
rows=[]
for tr in soup.table.find_all("tr")[1:]:
    cells=[td.get_text(strip=True) for td in tr.find_all("td")]
    if cells:
        rows.append(cells)
print(rows)

df=pd.DataFrame(rows,columns=headers)
print(df)

df.to_csv("auctionstats.csv")
# top players table
table1= soup.find_all("table")[1]
print(table1)
header1=[th.get_text(strip=True) for th in table1.find_all("th")]
print(header1)

# extracting rows from the table 
row1=[]
for tr in table1.find_all("tr")[1:]:
    data=[td.get_text(strip=True) for td in tr.find_all('td')]
    row1.append(data)   
print(row1)
df=pd.DataFrame(row1,columns=header1)

df.to_csv('top_buys_2022.csv')

pd.read_csv("top_buys+2022")