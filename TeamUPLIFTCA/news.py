from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='c44af03c330046fdb4c405c27ceefa95')
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
sources = newsapi.get_sources()