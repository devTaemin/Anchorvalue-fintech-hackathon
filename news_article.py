from gensim.summarization import summarize
from newspaper import Article
import tqdm
import pandas as pd
import re

data = pd.read_csv("2018_news_url.csv", encoding='utf-8-sig')
title = data["Title"].to_list()
modified_title = []
  
for content in title:
    content = re.sub(r'\([^)]*\)', '', content)
    content = re.sub(r'\[[^)]*\]', '', content)
    modified_title.append(content)

url_lst = data["Url"].to_list()
article_lst = []

for i in tqdm.tqdm(range(len(url_lst))):
  news = Article(url_lst[i], language="ko")
  news.download()
  news.parse()

  article = news.text
  article = re.sub(r'\([^)]*\)', '', article)
  article = re.sub(r'\[[^)]*\]', '', article)
  article_lst.append(article)

print(len(article_lst))
data["Article"] = article_lst
data.to_csv("2018_news_article.csv", encoding='utf-8-sig')
