from bs4 import BeautifulSoup   
import requests
import json
def scrape_movie_details():
    details_dict = {}
    url="https://www.imdb.com/title/tt0066763/"
    page= requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    poster=soup.find("div",class_="ipc-poster").a["href"]
    poster1="https://www.imdb.com"+poster
    details_dict["poster_image_url"]=poster1
    
    biodata=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
    details_dict["bio"]=biodata
    movie_name=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    details_dict["Movie_name"]=movie_name
    data= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    print(data) 
    for i in data:
        f=i.findAll('li',class_="ipc-metadata-list__item")
        for fi in f:
            if "Country" in fi.text:
                country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
            elif "Language" in fi.text:
                language=fi.findAll('a')
                for l in language: 
                    details_dict["language"]=l.text
                    details_dict["country"]=country
                # print(details_dict)

    Genres=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
    runtime=soup.find("span",class_="ipc-metadata-list--item__content-container")

    print(runtime)
    details_dict["runtime"]=runtime
    details_dict["Genres"]=Genres

    director=soup.find("li",class_="ipc-metadata-list__item").a.text
    details_dict["director"]=director

    with open("web_task4.json","w")as file:

        json.dump(details_dict,file,indent=4) 

scrape_movie_details()
