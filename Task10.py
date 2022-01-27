# from Task5 import *
import Task5
import json
f=open("web_task5.json","r")
load_data=json.load(f)
print(load_data)
# f.close()
# print(f)
def analyse_language_and_directors(movies):
    Lang_Direc_dic={}
    for movie in movies:
        for director in movie['director']:
            Lang_Direc_dic[director]={}
        print(Lang_Direc_dic)
    for i in range(len(movies)):
        for director in Lang_Direc_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    Lang_Direc_dic[director][language]=0
    for i in range(len(movies)):
        for director in Lang_Direc_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    Lang_Direc_dic[director][language]+=1
    with open("web_task10.json","w") as file:
        json .dump(Lang_Direc_dic,file,indent=4)
#     return Lang_Direc_dic
# analyse_language_and_directors()