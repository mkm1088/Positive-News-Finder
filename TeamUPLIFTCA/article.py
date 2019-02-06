import re
from selenium import webdriver
from bs4 import BeautifulSoup as BS

url = 'https://www.straitstimes.com/singapore/transport/mps-raise-questions-about-unusual-bidding-patterns-for-motorbike-coes'
#pjs = r'E:/ISBA/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/'
# pjs = 'C:\Python36-32\phantomjs-2.1.1-windows\bin\phantomjs.exe' #desktop
#webdriver.add_argument("--headless")
browser = webdriver.PhantomJS() 
browser.get(url)
html = browser.page_source 
soup = BS(html,'html.parser') #note that it is not html.content
table = soup.find_all('div',{'class':'odd field-item'})[0].find_all('p')
j=0
k=''
#print(table)
for i in table:
	if i.string!=None and not 'TO READ THE FULL ARTICLE' in i.string:
		k = k+str(i.string)
	else:
		j=j+1
print(k)
if j>0:
	print("artcile requires login")
else:
	print("artcils is okay")
	
# for element in table:
        # article_text += '\n' + ''.join(element.findAll(text = True))
# print(article_text)
# for element in table:
	# element_text += '\n'+ ''.join(element.content)
# #print(table.content)
# print(element_text)
# browser.quit()
