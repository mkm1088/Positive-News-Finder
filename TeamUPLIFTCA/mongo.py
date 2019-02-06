import pymongo
from pymongo import MongoClient
import requests
#from urllib3.request import urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import re

c = MongoClient()
db=c["mydatabase"]
article = db.articles

def insertIntoDB(date,title, content, source, url):
	post_Data ={'date': date, 'title':title,'content':content,'source':source,'url':url,'score':'NA'}
	result = article.insert_one(post_Data)
	
def updateScore():
	article.find({'score':'NA'})
	
#insertIntoDB('18/8/2018','Hi','Gen','Hello','bbc','www')
#updateScore()


# newsFromGuardian()
# NewsFromCNBC()
