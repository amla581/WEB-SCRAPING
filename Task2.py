import json
def group_by_year():

    first_tast=open("web_task1.json","r")
    data=json.load(first_tast)
    # print(data)
    list=[]
    dict={}
    for i in data:
        if int(i["year"]) not in dict:
            list.append (int(i["year"]))
    # print(list)

    list.sort()
    # print(list)

    for j in list:
        store=[]
        for k in data:
            if j== int(k["year"]):
                store.append(k)
        dict[j]=store
    return dict

data=group_by_year()
    # print(dict)
file=open("web_task2.json","w")
file_data=json.dump(data,file,indent=4)
print(file_data)



