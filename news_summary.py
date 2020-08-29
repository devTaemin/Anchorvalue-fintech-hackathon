from gensim.summarization import summarize
from newspaper import Article
import tqdm
import pandas as pd
import re

data_2 = pd.read_csv("SK_news_data.csv", encoding='euc-kr')

title = data_2["Title"].to_list()
article = data_2["Article"].to_list()

title_lst = []
article_lst = []
summary_lst = []

# 뉴스 헤드라인 정규화
for content in title:
    content = re.sub(r'\([^)]*\)', '', content)
    content = re.sub(r'\[[^)]*\]', '', content)
    title_lst.append(content)

# 뉴스 기사 정규화
for content in article:
    content = str(content)
    content = content.replace("\n", "")
    content = content.replace("  ", "")
    content = re.sub(r"http\\S+", "", content)
    content = re.sub('((www\\.[^\\s]+)|(https?://[^\\s]+))', '', content)
    content = re.sub('@[^\\s]+', '', content)
    article_lst.append(content)

# 뉴스 요약
for i in tqdm.tqdm(range(len(article_lst))):
    num_word = 50
    if len(article_lst[i]) < 50:
        summary_lst.append(article_lst[i])
    else:
        try:
            summary = summarize(article_lst[i], word_count=num_word)
            if summary == "":
                summary_lst.append(article_lst[i])
            else:
                summary_lst.append(summary)
        except:
            summary_lst.append(article_lst[i])

data_2["Article"] = article_lst
data_2["Title"] = title_lst
data_2["Summary"] = summary_lst
data_2.to_csv("SK_news_summary.csv", encoding='utf-8-sig')
