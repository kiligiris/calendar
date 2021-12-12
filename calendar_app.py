#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter as tk
import holiday_get as hdg
import get_calendar_info as gcal

class mycalendar(tk.Frame):
    def __init__(self, master, year , month):
        tk.Frame.__init__(self,master)
        #週の日にちの数
        self.wenum = 7

        self.dow = [ # [表記, 表記の色]
            ["月", "black"],
            ["火", "black"],
            ["水", "black"],
            ["木", "black"],
            ["金", "black"],
            ["土", "blue"],
            ["日", "red"]
        ]

        #週の開始を日曜日に設定
        self.weekst = 6
        for i in range((self.wenum - self.weekst) % self.wenum):
            self.dow.insert(0, self.dow.pop())
        
        # top部分を作成するメソッドの呼び出し
        self.create_top(year,month)
        
        # 曜日部分を作成するメソッドの呼び出し
        self.create_week()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(year,month)
        

    def create_top(self,year,month):
        # frame_top部分の作成
        self.frame_top = tk.Frame(self)
        self.frame_top.pack(pady=5)

        self.previous_month = tk.Label(self.frame_top, text = "<", font = ("",14))
        self.previous_month.pack(side = "left", padx = 10)
        self.current_year = tk.Label(self.frame_top, text = year, font = ("",18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(self.frame_top, text = month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(self.frame_top, text = ">", font = ("",14))
        self.next_month.pack(side = "left", padx = 10)

        

    def create_week(self):
        # 曜日部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        
        self.bdow = []
        for i in range(len(self.dow)):
            self.bdow.append(d_button(frame_week, text = self.dow[i][0], fg = self.dow[i][1]))
            self.bdow[i].grid(column=i,row=0)

    def create_calendar(self,year,month):
        # 指定した年(year),月(month)のカレンダーウィジェットを作成する
        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        cal_info = gcal.calendar_info()
        # 指定した年月のカレンダーをリストで返す
        days = cal_info.get_calendar(year,month)
        # 祝日情報を取得
        hd = hdg.holiday_get(year)
        if hd:
            mhd = hdg.month_holiday(hd,month)
            print(mhd)
        else:
            mhd = {}

        
        self.day = [[None] * 7] * len(days)
        for i in range(len(days)):
            for j in range(len(self.dow)):

                day = days[i][j]
                c = "red" if day in mhd else self.dow[j][1]

                if day != 0:
                    self.day[i][j] = d_button(self.frame_calendar,text = day, fg = c)
                    self.day[i][j].grid(column=j,row=i)
        
    def change_month(self,year,month):
        self.frame_top.destroy()
        self.create_top(year,month)

        self.frame_calendar.destroy()
        self.create_calendar(year,month)



# デフォルトのボタンクラス
class d_button(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",16),height=2, width=4, relief="flat")
            
if __name__ == "__main__":
    from datetime import datetime
    
    root = tk.Tk()
    root.title("Calendar")
    # 現在の日付を取得
    now = datetime.now()
    mycal = mycalendar(root, now.year, now.month)
    mycal.pack()
    #mycal.change_month(2021,1)
    mycal.destroy()
    mycal = mycalendar(root, 2021, 1)
    mycal.pack()
    root.mainloop()