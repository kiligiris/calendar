import json
import os
from typing import Dict
import requests
import datetime


def holiday_get(year):
    url = f"holiday/{year}.json"
    if os.path.isfile(url):
        with open(url, 'r') as hd:
            holidays = json.load(hd)
    else:
        holidays = holiday_bring_up(year)

        if holidays:
            with open(url, 'w') as hd:
                json.dump(holidays, hd, ensure_ascii=False, indent=4)
    
    return holidays

def holiday_bring_up(year):
    if year > datetime.date.today().year + 1 or year < 2015:
        return
    url = f"https://holidays-jp.github.io/api/v1/{year}/date.json"

    response = requests.get(url)

    jsonData = response.json()
    
    return jsonData

def month_holiday(hd: Dict,month):
    hd = {datetime.datetime.strptime(k,'%Y-%m-%d'): i for k, i in hd.items()}
    hd = {k.day: i for k, i in hd.items() if k.month == month}
    return hd

if __name__ == "__main__":
    for i in range(2015,2025):
        hd = holiday_get(i)
        holidays = hd
        print(holidays)