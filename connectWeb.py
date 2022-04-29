# 連線網路

# 公開資料查詢
# 確認資料格式 json.csv


import urllib.request as request
import json

src="https://industry.tms.gov.tw/opendata/tmsind.json"

with request.urlopen(src) as response:
    data =json.load(response) #取得原始碼(html.css.js)
# print(data)

print(data[0]["CompanyName1"])
print(data[0]["Tel"])
print(data[0]["Email"])

with open("connentTest.txt","w",encoding="utf-8") as file:
    for company in data:
        print(company["CompanyName1"])
        file.write(company["CompanyName1"]+"\n")
