import requests
from bs4 import BeautifulSoup as bs

resp = requests.get(
    "https://www.hamropatro.com/gold"
)
soup = bs(resp.content,"html.parser")

items = soup.find_all("ul", class_="gold-silver")
for item in items:
    li = item.find_all("li")
    gold = li[0].text.strip() 
    goldrate = li[1].text.strip()    
    silver = li[4].text.strip()
    silverate = li[5].text.strip()   
with open("rate.csv","w",encoding="utf-8") as f:
    f.writelines(f"{gold},{goldrate},{silver},{silverate}\n")
print("done")