import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

def change():
    label.configure(text="test2")

label = tk.Label(window,text="test")
label.pack()

button = tk.Button(window, text= "apasa", command= change)
button.pack()

window.mainloop()