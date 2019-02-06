import requests
#import pymongo
#from pymongo import MongoClient
import json
url = ('https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=95465951cbf447369c10a005ded49a0b')
response = requests.get(url)
j = response.json()
#parsed = json.loads(response)
print(j['articles'])

'''
headers={'AccountKey':'RAGHPk3qTNC685iHir8V8w==','accept':'application/json'}
url='http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=91081'
#mycol = mydb["news"]
r=requests.get(url,headers=headers)
#print(r.json())
j = r.json()
print(j[Services])

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['mydatabase']

mycol = mydb["customers"]
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
x = mycol.find_one()
print(x)
'''