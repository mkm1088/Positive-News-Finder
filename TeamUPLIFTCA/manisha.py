import requests
from bs4 import BeautifulSoup as bs
import json
import time
import re
from selenium import webdriver
def scrapping(urls):
    for url in urls:
        html_page=requests.get(url)
        time.sleep(5)
        containers_title=[]
        containerscat_title=[]
        containers_review=[]
        crawled_full=bs(html_page.content,"html.parser")
        containers=crawled_full.findAll('div',{'class':'nav-menu-links'})
        for i in containers:
            containers3=i.find('a',{'class':'nav-menu-links__link'}).get_text()
            containerscat_title.append(containers3)
            print("category:"+containers3)
            for j in containers3:
                containers5=j.find('h1',{'class':'pg-headline'}).get_text()
                containers_title.append(containers5)
                print("Title:"+containers5)
                containers4=j.find('div',{'class':'zn-body__paragraph speakable'}).get_text()
                containers_review.append(containers4)
                print("content:"+containers4)
                print("")
            
def main():
	
    homeurl="https://edition.cnn.com/"
    baseurl=""
    urllist=[]
    homepage=requests.get(homeurl+baseurl)
    time.sleep(2)
    crawled_home=bs(homepage.content,"html.parser")
    urls=crawled_home.findAll('div',{'page':'5'})
    temp=str(urls)
    match=re.findall('href=[\'"]?([^\'" >]+)',temp)
    urllist.append(homeurl+baseurl)
    if match:
        urllist.append(homeurl+str(match[0]))
    print(urllist)
    scrapping(urllist)
	

if __name__== "__main__":
    main()
