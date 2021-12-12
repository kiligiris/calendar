DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class calendar_info():
    def __init__(self):
        # dow = day of week
        self.dows = [
            "Sun",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat"
        ]
        self.start_dow = "Sun"
        self.week_len = 7

    # 始まりの曜日を変更
    def change_start_dow(self,dow):
        for d in self.dows:
            if d == dow:
                self.start_dow = dow
                self.change_dows()
                return True
        return False

    # dows配列をstart_dowに合わせて変更
    def change_dows(self):
        if self.start_dow == self.dows[0]:
            return
        for _ in range(self.week_len):
            self.dows.insert(0,self.dows.pop())
            if self.start_dow == self.dows[0]:
                return

    # 指定された日付の曜日番号を返す
    def get_dow(self,year,month,day):
        if month <= 2 :
            year -= 1
            month += 12
        y = year % 100
        h = (day + 26 * (month + 1) // 10 + y + y // 4 - 2 * year // 100 + year // 400) % 7
        return (h + self.dows.index("Sat")) % self.week_len
        

    # 指定された月の始まりの曜日を返す
    def get_first_day_dow(self,year,month):
        return self.get_dow(year,month,1)

    # 閏年かどうか True or False
    def check_leap_year(self,year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # 指定された月の日数を返す
    def get_days(self,year,month):
        if month == 2 and self.check_leap_year(year): # 二月で閏年だったら
            return DAYS[month - 1] + 1
        return DAYS[month - 1]

    # 指定した年月のカレンダーをリストで返す
    def get_calendar(self,year,month):
        days = self.get_days(year,month)
        fday = self.get_first_day_dow(year,month)
        calendar = []
        week = [0] * fday
        self.change_dows()
        for day in range(1,days + 1):
            week.append(day)
            if len(week) == self.week_len:
                calendar.append(week)
                week = []
        if week:
            week += [0] * (self.week_len - len(week))
            calendar.append(week)
        
        return calendar



if __name__ == "__main__":
    year = 2021
    month = 1
    day = 12
    cal_info = calendar_info()
    isLeapYear = cal_info.check_leap_year(year)
    print(isLeapYear)
    days = cal_info.get_days(year,month)
    print(days)
    
    down = ["日","月","火","水","木","金","土"]
    dowi = cal_info.get_dow(year,month,day)
    print(down[dowi])
    dowi = cal_info.get_first_day_dow(year,month)
    print(down[dowi])
    print(cal_info.get_calendar(year,month))
    dowi = cal_info.get_dow(2021,12,14)
    print(down[dowi])


    cal_info.change_start_dow("Fri")
    down = ["金","土","日","月","火","水","木"]
    dowi = cal_info.get_dow(year,month,day)
    print(down[dowi])
    dowi = cal_info.get_first_day_dow(year,month)
    print(down[dowi])
    print(cal_info.get_calendar(year,month))
