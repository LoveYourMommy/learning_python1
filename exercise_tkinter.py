__author__ = 'lym'


from tkinter import *


def Hello():
    print('Hello!')

tk = Tk()
btn = Button(tk, text="Show me tits!", command=Hello)
btn.pack()
btn.mainloop()



