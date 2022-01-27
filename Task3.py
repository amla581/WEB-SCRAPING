import json,os

file=open("web_task1.json","r")
task2=json.load(file)
# print(task2)

def group_by_decade():
    list1=[]
    dict={}
    for i in task2:
        if i["year"] not in list1:
            list1.append (i["year"])
    list1.sort()
    # print(list1)  
    list=[]
    for i in list1:
        mod=int(i)%10
        dec=int(i)-mod
        if dec not in list:
            list.append(dec)
            dict[i]=[]
    # print(list)
    # print(dict)
    for x in dict:
        for i in task2:
            a=str(x)
            b=str(i['year'])
            if a[-2]==b[-2]:
                dict[x].append(i)
    return dict
f=group_by_decade()
file=open("web_task3.json","w")
file_data=json.dump(f,file,indent=4)
print(file_data)