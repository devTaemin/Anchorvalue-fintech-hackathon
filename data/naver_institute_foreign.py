# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:13:01 2020

@author: dhk1349
"""

import requests
from bs4 import BeautifulSoup as soup
#from bs4 import BeautifulSoup as soup
import datetime
import json

url="https://finance.naver.com/item/frgn.nhn?code="
code="006400"
page="2"
url_final=url+code+"&page="+page


def get_ext_amnt_(code,page, amnt):
    from bs4 import BeautifulSoup as soup
    

    url="https://finance.naver.com/item/frgn.nhn?code="
    txt=requests.get(url+code+"&page="+page).text
    soup=soup(txt, "html5lib")
    #print(soup)
    table=soup("body")[0].find("div",{"id":"wrap"}).find("div",{"id":"middle"}).find("div",{"class":"content_wrap"}).find("div", {"class":"section inner_sub"}).find_all("table")[1]
    rows=table.find_all("tr")
    
    
    container=[]

    for i in range(4):
        container.append(rows[i*8+3])
        container.append(rows[i*8+4])
        container.append(rows[i*8+5])
        container.append(rows[i*8+6])
        container.append(rows[i*8+7])
    #print(len(container))
    for i in container:
        date=i.find_all("td")[0].text
        inst_amnt=i.find_all("td")[5].text
        foreign_amnt=i.find_all("td")[6].text
        foreign_total=i.find_all("td")[7].text
        foreign_percent=i.find_all("td")[8].text
        amnt[date]=[inst_amnt, foreign_amnt, foreign_total, foreign_percent]

    return json.dumps(amnt)


def get_ext_amnt(code, idx):
    amnt={}
    for i in range(1,idx):
        #print(i)
        amnt=json.loads(get_ext_amnt_(code, str(i), amnt))
    #print("result")
    #print(pricedict.keys())
    #print(pricedict['2017.03.20'])
    with open(code+".json", 'w', encoding='utf-8-sig') as make_file:
        json.dump(amnt, make_file)
    #print(amnt.keys())
    print(code+" finished")


with open ('..\Kospi-200\Kospi-200.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

json_code = json_data["Code"]

#print(json_code)
#print(type(json_code))
#for i in range(87,len(json_code)):
#    get_ext_amnt(json_code[i], 86)
#    print(i, "\n")
