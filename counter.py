import tkinter as tk

root = tk.Tk()
root.geometry('400x200')
root.title('Counter App')
root.minsize(200, 100)
# global initilisation
var = tk.IntVar(value=0)

def Increment():
    lb.config(text=lb.cget('text')+1, fg='green')
    if lb.cget('text') >= 10:
            lb.config(fg='blue')
def Decrement():
    if lb.cget('text') != 0:
        lb.config(text=lb.cget('text')-1, fg='red')

        if lb.cget('text') <= 10:
            lb.config(fg='orange')

lb = tk.Label(root, text=0, font=('bold', 30), fg='green')
lb.pack()
bt1 = tk.Button(text='Increment', bg='green', command=Increment)
bt1.pack(side='left',ipadx=20, ipady=20, padx=20, pady=20)
bt2 = tk.Button(text='Decrement', bg='red', command=Decrement)
bt2.pack(side='right',ipadx=20, ipady=20, padx=20, pady=20)

root.mainloop()