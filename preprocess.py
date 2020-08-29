import pandas as pd
import numpy as np

df = pd.read_csv("news_label.csv", encoding='utf-8-sig')
print("전처리 전 열 개수: {}".format(len(df)))

# Title 열에서 중복인 내용이 있다면 중복 제거
df.drop_duplicates(subset=['Title'], inplace=True)
df['Title'] = df['Title'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
df['Title'] = df['Title'].str.strip()
df['Title'].replace('  ', ' ', inplace=True)
df['Title'].replace('', np.nan, inplace=True)

df.drop_duplicates(subset=['Summary'], inplace=True)
df['Summary'] = df['Summary'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
df['Summary'] = df['Summary'].str.strip()
df['Summary'].replace('  ', ' ', inplace=True)
df['Summary'].replace('', np.nan, inplace=True)

# Null값 확인하기
if df.isnull().values.any():
    print(df.isnull().sum())

    # Null 값 제거하기
    df = df.dropna(how="any")

    # Null 값 있는지 다시 한 번 확인
    print(df.isnull().sum())

df.drop_duplicates(subset=['Title'], inplace=True)

print("전처리 후 열 개수: {}".format(len(df)))
print(df.head())

df.to_csv("news_label_preprocess.csv", encoding='utf-8-sig')
