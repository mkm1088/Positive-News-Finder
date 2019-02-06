def NewsFromCNN():
    main_url = "https://newsapi.org/v2/everything?language=en&sources=cnn&apiKey=cb28b795dd1e469ebbc02ea19535898a"
    open_cnbc_page = requests.get(main_url).json()
    article = open_cnbc_page["articles"]
    browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
    for ar in article:
        browser.get(ar["url"])
        ans=''
        html = browser.page_source
        soup = BS(html, 'html.parser')
        try:
            table1 = soup.find('div',{'class':'zn-body__read-all'})
            table = table1.find_all('div',{'class':'zn-body__paragraph'})
            for k in table:
                if k.string is not None:
                    ans=ans+k.string
                    insertIntoDB(ar['publishedAt'],ar["title"], ans, "The Hindu", ar["url"])
        except:
            print("exception")

NewsFromCNN()
