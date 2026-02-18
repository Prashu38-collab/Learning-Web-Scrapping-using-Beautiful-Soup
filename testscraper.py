import pandas as pd
import requests 
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")

names= soup.find_all("a",class_="title")
print(names)

product_name=[]
for i in names:
    name=i.text.strip()
    product_name.append(name)
print(product_name)

prices=soup.find_all("h4",class_="price float-end card-title pull-right")
print(prices)

product_price=[]
for i in prices:
    price=i.text.strip()
    product_price.append(price)
print(product_price)

descriptions= soup.find_all('p',class_="description card-text")
print(descriptions)
product_descriptions=[]
for i in descriptions:
    descr=i.text.strip()
    product_descriptions.append(descr)
print(product_descriptions)

reviews=soup.find_all("p",class_="review-count float-end")
print(reviews)
product_reviews=[]
for i in reviews:
    review=i.text.strip()
    product_reviews.append(review)
print(product_reviews)

df=pd.DataFrame({"Product Name":product_name,"Prices":product_price,"Description":product_descriptions,"Reviews":product_reviews})
print(df)
# converting to csv
df.to_csv("products_details.csv")
print("sucess")

