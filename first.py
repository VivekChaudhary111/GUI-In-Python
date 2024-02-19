# GUI ==>>> GRAPHICAL USER INTERFACE
# from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('400x200')
root.title('First Application')
root.minsize(100, 200)

def my_fun1():
    lb.config(text=lb.cget('text')+1)
def my_fun2():
    if lb.cget('text') !=0:
        lb.config(text=lb.cget('text')-1)
  
lb = tk.Label(root, text=0)
lb.pack()
bt1 = tk.Button(root, text=' Increment ', command=my_fun1)
bt1.pack()
bt2 = tk.Button(root, text=' Decrement ', command=my_fun2)
bt2.pack()
root.mainloop()