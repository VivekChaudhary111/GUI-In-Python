import tkinter as tk
from tkinter import messagebox

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('300x200')
        self.mainwindow.title('BMI calculator')
        self.mainwindow.minsize(100, 100)
        
        tk.Label(text = 'Weight(in kg): ', font=("Arial", 10)).grid(row=1, column=0, padx = 10, pady = 10, ipadx=2, ipady=2)
        self.weight = tk.Entry(root, font=("Arial", 10, 'bold'))
        self.weight.grid(row=1, column=1, padx = 10, pady = 10, ipadx=2, ipady=2)

        tk.Label(text = 'Height(in cm): ', font=("Arial", 10)).grid(row=2, column=0, padx = 10, pady = 10, ipadx=2, ipady=2)
        
        self.height = tk.Entry(root, font=("Arial", 10, 'bold'))
        self.height.grid(row=2, column=1, padx = 10, pady = 10, ipadx=2, ipady=2)

        self.click = tk.Button(text = 'Calculate', command=self.action)
        self.click.grid(row=3, column=0, columnspan=2, padx = 10, pady = 10, ipadx=2, ipady=2)
    
    def action(self):
        weight = self.weight.get()
        height = self.height.get()
        self.bmi = float(weight)*10000/float(height)**2
        messagebox.showinfo(title='Calculated BMI', message=f'BMI of given data is : {round(self.bmi, 2)}')

# Main code
root = tk.Tk()
exc = app(root)
root.mainloop()