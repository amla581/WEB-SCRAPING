import requests
import json
from bs4 import BeautifulSoup
skirt="https://www.boohoo.com/tartan-check-print-jersey-tube-mini-skirt/FZZ37001.html"
req=requests.get(skirt)
soup = BeautifulSoup(req.text,"html.parser")
dict={}
price1=soup.find("span",class_="price-sales").text.split()
print(price1)
dict["price"]=price1

size=soup.find("div",class_="attribute size-attribute").text.split()
m=size[4:-2]
print(m)
dict["size"]=m

color=soup.find("span",class_="selected-value").text.split()
dict["color"]=color
print(dict)
with open("boohoo.json","w") as file:
    json.dump(dict,file,indent=4)

# <span class="attribute-title">
# UK Size:
# </span>
