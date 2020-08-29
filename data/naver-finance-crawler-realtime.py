# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:00:47 2020

@author: Taemin
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re

# 저장 포맷
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def replacer(data):
    result = data
    result = result.replace("?", " ")
    result = result.replace("\\", " ")
    result = result.replace("/", " ")
    result = result.replace("*", " ")
    result = result.replace("\"", " ")
    result = result.replace("<", " ")
    result = result.replace(">", " ")
    result = result.replace("|", " ")
    result = result.replace(":", " ")
    result = result.replace("\t","")
    result = result.replace("\n","")
    return result
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# 네이버 금융 실시간 속보 크롤러
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#URL 예시: https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&date=20200828&page=1
def naver_finance_realtime(URL):
    date = ""
    page = ""
    url = URL + "&date=" + date + "&page=" + page
    
    source = urlopen(url)
    obj = soup(source, "html.parser")
    
    
    cursor1 = obj.find('li',{"class":"newsList top"}).find("dl").children
    cursor2 = obj.findAll('li',{"class":"newsList"})
    container=[]
    for idx, i in enumerate(cursor1):
        if(idx%2==1):
            container.append(i)
    
    
    
    title = None
    body = None
    article = None
    time = None
    split = None
    ref = None
    
    for idx, i in enumerate(container):
        
        if (i.attrs == {'class':['articleSubject']}):
            title = i.text
            ref = i.find("a").attrs['href']
            
        elif (i.attrs == {'class':['articleSummary']}):
            body = i.text
            article_idx = 1
            article = body.split("\n")[article_idx].strip("\t")
            while (len(article) == 0):
                article_idx += 1
                article = body.split("\n")[article_idx].strip("\t")
            split = body.split("\n")[-3]
            time = body.split("\n")[-2]
            
            route = "database\\"
            if (title != None and article != None):
                EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
                title_refine = EMOJI.sub(r'',title)
                article_refine = EMOJI.sub(r'',article)
                
                f=open(route + replacer(time.replace("\n", "\t").strip('\t').replace(":", "."))+"_"+replacer(title.replace("\n", "\t").strip('\t'))+".txt", 'w', encoding="utf-8")
                f.write(title_refine.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n\n")
                f.write(article_refine.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n")
                f.write(split.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n")
                f.write(time.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n\n")
                f.write(ref.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n")
            
                title == None
                article == None
                f.close()
            
         
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
naver_finance_realtime("https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258")