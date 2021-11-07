#!/usr/bin/env python
# -*- coding: utf8 -*-
from datetime import datetime
import tkinter as tk
import holiday_get as hdg

class mycalendar(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        "初期化メソッド"
        tk.Frame.__init__(self,master,cnf,**kw)
        
        # 現在の日付を取得
        now = datetime.now()
        # 現在の年と月を属性に追加
        self.year = now.year
        self.month = now.month

        # frame_top部分の作成
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)
        self.previous_month = tk.Label(frame_top, text = "<", font = ("",14))
        self.previous_month.pack(side = "left", padx = 10)
        self.current_year = tk.Label(frame_top, text = self.year, font = ("",18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(frame_top, text = self.month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(frame_top, text = ">", font = ("",14))
        self.next_month.pack(side = "left", padx = 10)

        # frame_week部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        self.dow ={
            "日" : "red",
            "月" : "black",
            "火" : "black",
            "水" : "black",
            "木" : "black",
            "金" : "black",
            "土" : "blue"
        }
        
        self.bdow = []
        for i, dw in enumerate(self.dow):
            self.bdow.append(d_button(frame_week, text = dw, fg = self.dow[dw]))
            self.bdow[i].grid(column=i,row=0)
       
        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year,self.month)

    def create_calendar(self,year,month):
        "指定した年(year),月(month)のカレンダーウィジェットを作成する"
        
        # calendarモジュールのインスタンスを作成
        import calendar
        #週の開始を日曜日に設定
        calendar.setfirstweekday(calendar.SUNDAY)
        # 指定した年月のカレンダーをリストで返す
        days = calendar.monthcalendar(year,month)
        
        # 日付ボタンを格納する変数をdict型で作成
        #self.day = {}
        # for文を用いて、日付ボタンを生成
        hd = hdg.holiday_get(year)

        mhd = hdg.month_holiday(hd,month)
        print(mhd)
        

        self.day = [[None] * 7] * len(days)
        for i in range(len(days)):
            for j, dw in enumerate(self.dow):

                day = days[i][j]
                c = "red" if day in mhd else self.dow[dw]

                if day != 0:
                    self.day[i][j] = d_button(self.frame_calendar,text = day, fg = c)
                    self.day[i][j].grid(column=j,row=i)
        
        
# デフォルトのボタンクラス
class d_button(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",16),height=2, width=4, relief="flat")
            
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calendar App")
    mycal = mycalendar(root)
    mycal.pack()
    root.mainloop()