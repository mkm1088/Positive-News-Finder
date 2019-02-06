import requests
#from urllib3.request import urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import re
def newsFromCNBC():
    main_url = "https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=***************"
    open_cnbc_page = requests.get(main_url).json()
    print(len(open_cnbc_page),"is the length of the json return")
    article = open_cnbc_page["articles"]
    browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
    for ar in article:
        browser.get(ar["url"])
        print(ar["url"])
        #ans=''		
        html = browser.page_source
        soup = BS(html, 'html.parser')
        try:
            title = soup.find('h2',{'class':'intro'}).get_text()
            table1 = soup.find('div',{'class':re.compile('content-body')})
            table = table1.find_all('p')
            #print(soup.find_all('div',{'class':re.compile('content-body')})[1].find_all('p'))
            for k in table:
                if k.string is not None:
                    ans=ans+k.string
            #insertIntoDB(ar['publishedAt'],ar["title"], ans, "The Hindu", ar["url"])
            print(ans)
        except:
            print("removing video articles")

#driver
if __name__ == '__main__':
    # function call
    newsFromCNBC()
