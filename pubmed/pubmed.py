# Beautiful Soupのインポート
from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import re # 正規表現操作用


url_pubmed = "https://pubmed.ncbi.nlm.nih.gov/?term=Yamashita+Michiaki&sort=pubdate&sort_order=asc&size=50"
response = req.urlopen(url_pubmed)

columns = ["rank", "writer", "title", "year", "url"]
df = pd.DataFrame(columns=columns) #表の作成
soup =  BeautifulSoup(response, 'html.parser')

tags1 = soup.find_all("span", {"class": "full-authors"}) # writer
tags2 = soup.find_all("a", {"class": "docsum-title"}) # title,URL
tags3 = soup.find_all("span", {"class": "docsum-journal-citation"}) # year

rank = 1
for tag1, tag2, tag3 in zip(tags1, tags2, tags3):
        writer = tag1.text
        writer = writer.replace(" ", "")
        writer = writer.replace("\t", "")
        writer = writer.replace("\n", "")
        title = tag2.string
        title = title.strip()
        url = tag2.get("href")
        year = tag3.string
        year = year.strip()
        se = pd.Series([rank, writer, title, year, url], columns)
        df = df.append(se, columns) # appendで要素を追加
        rank += 1

filename = "pubmed.csv"
df.to_csv(filename, encoding = 'utf-8-sig')
