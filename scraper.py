import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone"
response=requests.get(url)
print(response.text) #here .text means we are only geeting the text excluding the image 
soup=BeautifulSoup(response.text,"lxml")
# print(soup) #printing entire beautiful soup object

# here if i want to find out the tags here finding div
print(soup.div)
print(soup.div.p) #p tag
tag=soup.div # div tag 
print(tag.attrs) #attributes inside div tag
tag1=soup.header #finding attributes for headers
attb=tag1.attrs

# for headers we have key value pairs, printing values
print(attb['class'])
print(soup.h3.string)
print(soup.h2.string)
# so i want to print a paragraph using find
paragraph=soup.find("p",{'class':'lead'})
print(paragraph)
# findall - to find all the price

prices=soup.find_all("h4",class_="price float-end card-title pull-right")
for i in prices:
    print(i.text.strip())

description=soup.find_all("p",class_="description card-text")
# print(description)
for des in description:
    print(des.text)

reviews=soup.find_all("p",class_="review-count float-end")
print(reviews)
for rev in reviews:
    print(rev.text)
