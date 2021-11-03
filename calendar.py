#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter as tk

class mycalendar(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        "初期化メソッド"
        import datetime
        tk.Frame.__init__(self,master,cnf,**kw)
        
        # 現在の日付を取得
        now = datetime.datetime.now()
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
        
        self.day = [[None] * 7] * len(days)
        for i in range(len(days)):
            for j, dw in enumerate(self.dow):
                if days[i][j] != 0:
                    self.day[i][j] = d_button(self.frame_calendar,text = days[i][j], fg = self.dow[dw])
                    self.day[i][j].grid(column=j,row=i)
        
        '''
        for i in range(len(days) * 7):
            c = i - (7 * int(i/7))
            r = int(i/7)
        
            # 日付が0でなかったら、ボタン作成
            if days[r][c] != 0:
                if c == 0:
                    self.day[i] = d_button(self.frame_calendar,text = days[r][c], fg = "red")
                elif c == 6:
                    self.day[i] = d_button(self.frame_calendar,text = days[r][c], fg = "blue")
                else:
                    self.day[i] = d_button(self.frame_calendar,text = days[r][c])
                self.day[i].grid(column=c,row=r)
        '''
        
# デフォルトのボタンクラス
class d_button(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",16),height=2, width=4, relief="flat")
            
# ルートフレームの定義      
root = tk.Tk()
root.title("Calendar App")
mycal = mycalendar(root)
mycal.pack()
root.mainloop()