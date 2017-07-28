#! /usr/bin/env python3
#-*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
'''
python 图形界面的第三方库
Tk
wxWidgets
Qt
GTK
Python自带的库是支持Tk的Tkinter
'''
print('jjj')

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.helloLabel= Label(self, text='Hello, world!')
        self.helloLabel.pack() # pack()方法是把widget 加入到父容器，并实现布局
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton =Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口的标题
app.master.title('hello world')
# 主消息循环
app.mainloop()