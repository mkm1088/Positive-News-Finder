# importing requests package
import requests
#from urllib3.request import urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import re


def NewsFromCNBC():
    #CNBC news api
    main_url = "https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=cb28b795dd1e469ebbc02ea19535898a"

    # fetching data in json format
    open_cnbc_page = requests.get(main_url).json()
    #print(open_cnbc_page)
    print(len(open_cnbc_page),"is the length of the json return")


    article = open_cnbc_page["articles"]


    results = []
    links = []
    url = []
    answer = []
    title_ret=[]
    time_art=[]
    browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

    for ar in article:
        #print(ar["title"])
        print(ar["url"]) #url
        print(ar["title"]) #title
        print(ar['publishedAt'])#time
        print("cnbc")#source
        browser.get(ar["url"])
        #links.append(ar["url"])
        #title_ret.append(ar["title"])
        #time_art.append(ar['publishedAt'])

        ans=''
		
        html = browser.page_source
        soup = BS(html, 'html.parser')
        #print(soup.find_all('div',{'class':'group-container'}))
        table1 = soup.find('div',{'id':re.compile("content-body-.*-.*")})
        table = table1.find_all('p')
        for k in table:
            if k.string is not None:
                ans=ans+k.string
                print(ans) #article
        #print(answer,links,title_ret,time_art)
		
		

# Driver Code
if __name__ == '__main__':
    # function call
    NewsFromCNBC()
