import time
import datetime 
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

secunda=datetime.timedelta(seconds=1)
timp = datetime.timedelta(minutes=0,seconds=5)


def scade():
    global timp,secunda
    timp = timp - secunda
    text.config(text=str(timp))
    if timp==datetime.timedelta(seconds=0):
        print("ai de plm")
    window.after(1000,scade)

text = tk.Label(window,text=str(timp))
text.config(font=25)
text.pack()

but = tk.Button(window,text="start",command=scade)
but.pack()
window.mainloop()