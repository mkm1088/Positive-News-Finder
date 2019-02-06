from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='*****************')
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
sources = newsapi.get_sources()
