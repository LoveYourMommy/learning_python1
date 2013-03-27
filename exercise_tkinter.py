#!/usr/bin/python3.2
#__author__ = 'lym'

import this



from tkinter import *


def Hello():
    print('Hello!')

tk = Tk()
btn = Button(tk, text="Show me tits!", command=Hello)
btn.pack()
btn.mainloop()



