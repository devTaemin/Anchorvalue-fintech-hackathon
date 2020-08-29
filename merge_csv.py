import pandas as pd
from pandas import DataFrame

df_0 = pd.read_csv('2019.csv', delimiter=',', encoding='utf-8-sig')
df_1 = pd.read_csv('2020.csv', delimiter=',', encoding='utf-8-sig')
#df_2 = pd.read_csv('2020_news_summary.csv', delimiter=',')

df_merge = pd.concat([df_0, df_1]) # row bind : axis = 0, default
data = {"Date": [],
        "Title": [],
        "Summary": [],
        "Url": [],
        "Label": []}

new_df = DataFrame(data)
new_df["Date"] = df_merge["Date"]
new_df["Title"] = df_merge["Title"]
new_df["Summary"] = df_merge["Summary"]
new_df["Url"] = df_merge["Url"]
new_df["Label"] = df_merge["Label"]

result = new_df.dropna(axis=0)
print(len(result))
new_df.to_csv('news_label.csv', sep=',', encoding='utf-8-sig')