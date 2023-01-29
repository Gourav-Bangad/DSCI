import pandas as pd
import requests
from bs4 import BeautifulSoup


Product_name = []
Price = []
Description = []

for i in range(2,248):
              url ="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

              r = requests.get(url)

              soup = BeautifulSoup(r.text,"lxml")

              names = soup.find_all("div",class_="_4rR01T")

              prices = soup.find_all("div",class_="_30jeq3 _1_WHN1")

              desc = soup.find_all("ul",class_="_1xgFaf")    

              for i in names:
                    temp = i.text
                    Product_name.append(temp)   
              for i in prices:
                    temp = i.text
                    Price.append(temp)                
              for i in desc:
                    temp = i.text
                    Description.append(temp)

# print(Product_name)
# print(Price)
# print(Description) 

df = pd.DataFrame({"Product Name":Product_name,"Prices":Price,"Description":Description})

df.to_csv("C:/Users/MI/Desktop/Dsci/mobile_data.csv")