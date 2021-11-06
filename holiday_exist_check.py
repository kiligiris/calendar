import json
import os
import requests
import datetime


class holiday_check():
    def __init__(self,year):
        url = f"holiday/{year}.json"
        if os.path.isfile(url):
            with open(url, 'r') as hd:
                self.holidays = json.load(hd)
        else:
            self.holidays = self.holiday_get(year)

            if self.holidays:
                with open(url, 'w') as hd:
                    json.dump(self.holidays, hd, ensure_ascii=False, indent=4)
    
    def holiday_get(self,year):
        if year > datetime.date.today().year + 1 or year < 2015:
            return False
        url = f"https://holidays-jp.github.io/api/v1/{year}/date.json"

        response = requests.get(url)

        jsonData = response.json()
        
        return jsonData


for i in range(2015,2025):
    holiday = holiday_check(i)
    print(holiday.holidays)