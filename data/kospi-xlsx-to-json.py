# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:44:53 2020

@author: Taemin
"""

import pandas as pd
import json


# read csv file and convert it to dictionary
df = pd.read_csv(r'C:\Users\Taemin\Desktop\Hackerton-fintech\Kospi-200\Kospi-200.csv')
Code = df["Code"].tolist()    
for i in range(len(Code)):
    if (len(str(Code[i])) == 1):
        Code[i] = "00000" + str(Code[i])
    elif (len(str(Code[i])) == 2):
        Code[i] = "0000" + str(Code[i])
    elif (len(str(Code[i])) == 3):
        Code[i] = "000" + str(Code[i])
    elif (len(str(Code[i])) == 4):
        Code[i] = "00" + str(Code[i])
    elif (len(str(Code[i])) == 5):
        Code[i] = "0" + str(Code[i])
    else:
        Code[i] = str(Code[i])
KOSPI = df["KOSPI"].tolist()
WICS = df["WICS"].tolist()
Stock = df["Stock"].tolist()
temp_dict = {"Code":Code, "KOSPI":KOSPI, "WICS":WICS, "Stock":Stock}



# write dictionary to JSON file
with open(r'C:\Users\Taemin\Desktop\Hackerton-fintech\Kospi-200\Kospi-200.json', 'w', encoding = 'utf-8-sig') as file:
    #json.dump(temp_dict, fp)
    file.write(json.dumps(temp_dict, ensure_ascii = False))

