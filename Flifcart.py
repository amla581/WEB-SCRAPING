import json
import requests
from bs4 import BeautifulSoup

flipcart="https://www.flipkart.com/apple-iphone-12-purple-128-gb/p/itmebc78f1cb26d3?pid=MOBG2EPZK5ZD9KYS&lid=LSTMOBG2EPZK5ZD9KYSDUOOA2&marketplace=FLIPKART&q=phone&store=tyy%2F4io&srno=s_1_17&otracker=search&otracker1=search&fm=organic&iid=f6df7372-6604-4f57-99eb-5a164ecc3232.MOBG2EPZK5ZD9KYS.SEARCH&ppt=None&ppn=None&ssid=j6ne9vhu4g0000001634964891755&qH=f7a42fe7211f98ac"
a=requests.get(flipcart)
soup = BeautifulSoup(a.text,"html.parser")
dict={}

def scrap_link():
    dict={}
    model_name=soup.find("span",class_="B_NuCI").get_text()[:15]
    dict["model_name"]=model_name
    color=soup.find("span",class_="B_NuCI").get_text()[17:23]
    dict["color"]=color
    rating=soup.find("div",class_="_3LWZlK").get_text()
    dict["rating"]=rating
    image="https://www.flipkart.com/apple-iphone-12-white-128-gb/p/itm95393f4c6cc59?pid=MOBFWBYZBTZFGJF9&lid=LSTMOBFWBYZBTZFGJF9K5AZO1&marketplace=FLIPKART&q=apple+phone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=37010cc3-f115-4470-97d2-5d0808f2456d.MOBFWBYZBTZFGJF9.SEARCH&ppt=sp&ppn=sp&ssid=cjnpodrvsg0000001630575702140&qH=900bc469862f62c0"
    dict["image"]=image
    with open ("flifcart.json","w")as file:
        json.dump(dict,file,indent=4)

scrap_link()

