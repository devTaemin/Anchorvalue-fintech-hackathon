# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:44:22 2020

@author: dhk1349
"""
import json
"""
url="https://finance.naver.com/item/sise_day.nhn?code=051910&page=1"
code="051910"
page=str(1)

url=url+code+"&page="+page
"""
code="051910"

def _get_price(code, page, pricedict):
    url="https://finance.naver.com/item/sise_day.nhn?code="
    
    import json
    import requests
    from bs4 import BeautifulSoup as soup
     

    url1=url+code+"&page="+page
    #print(url1)
    txt=requests.get(url1).text
    #print(txt)
    soup=soup(txt, "html5lib")
    #print(soup)
    row=soup("tbody")[0].children
    container=[]
    for idx, i in enumerate(row):
        if(idx%2==0):
            container.append(i)
    row=[]
    for idx, i in enumerate(container):
        
        if(idx in [2,3,4,5,6,10,11,12,13,14]):
            row.append(i)
    for i in row:
        #print(type(i))
        #print(i)
        td=i.find_all('td')
        date=td[0].text
        startprice=td[3].text.replace(",","")
        endprice=td[1].text.replace(",","")
        amnt=td[-1].text.replace(",","")
        pricedict[date]=[startprice, endprice, amnt]

    return json.dumps(pricedict)




def get_price(code, idx):
    pricedict={}
    for i in range(1,idx):
        #print(i)
        pricedict=json.loads(_get_price(code, str(i), pricedict))
    #print("result")
    #print(pricedict.keys())
    #print(pricedict['2017.03.20'])
    with open(code+".json", 'w', encoding='utf-8') as make_file:
        json.dump(pricedict, make_file)
    print(code+" finished")
    

with open ('..\Kospi-200\Kospi-200.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

json_code = json_data["Code"]

#for i in range(len(json_code)):
#    get_price(json_code[i], 86)
#    #get_price(code, 86)

get_price("180640", 86)

