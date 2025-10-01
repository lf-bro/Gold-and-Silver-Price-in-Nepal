import json
import requests
from bs4 import BeautifulSoup as bs


def scrap():
    resp = requests.get("https://www.hamropatro.com/gold")
    soup = bs(resp.content, "html.parser")
    list = []
    obj = {}
    items = soup.find_all("ul", class_="gold-silver")
    for item in items:
        li = item.find_all("li")
        # gold = li[0].text.strip()
        goldrate = (
            li[1].text.strip().replace(" ", "").replace("\n", "").replace(",", " ")
        )
        # silver = li[4].text.strip()
        silverate = (
            li[5].text.strip().replace(" ", "").replace("\n", "").replace(",", " ")
        )
        # obj["goldname"] = f"{gold}"
        obj["goldrate"] = f"{goldrate}"
        # obj["silvername"] = f"{silver}"
        obj["silverrate"] = f"{silverate}"
        list.append(obj)
    with open("rate.json", "w", encoding="UTF-8") as f:
        json.dump(list, f, indent=4)


scrap()
