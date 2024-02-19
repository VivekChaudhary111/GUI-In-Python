import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class app:
    def __init__(self, mainwindow, url):
        mainwindow.title = 'Currency Converter'

        mainwindow.configure(background = 'sky blue')
        mainwindow.geometry("500x300")
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

        self.intro_label = tk.Label(text = 'Welcome to Real Time Currency Convertor', fg="Blue",font=("Arial", 10, "bold"), borderwidth = 3)
        self.intro_label.grid(row=0, column=0, columnspan=2, padx = 10, pady = 20, ipadx=2, ipady=2)

        self.label = tk.Label(text = 'Enter the amount to convert : ', font=("Arial", 10, "bold"))
        self.label.grid(row=1, column=0, padx = 10, pady = 20, ipadx=2, ipady=2)

        self.amount_field = tk.Entry(root)
        self.amount_field.grid(row=1, column=1, padx = 10, pady = 10, ipadx=2, ipady=2)
        
        tk.Label(text = 'From(in currency code): ', font=("Arial", 10, "bold")).grid(row=2, column=0, padx = 10, pady = 10, ipadx=2, ipady=2)
        
        self.currency1 = tk.StringVar(root)
        self.from_currency = ttk.Combobox(root, width=12, textvariable=self.currency1, state='readonly')
        self.from_currency['values']  = sorted(list(self.currencies.keys()))     
        # self.from_currency.current(0) 
        self.from_currency.set("INR")
        self.from_currency.grid(row=2, column=1, padx = 10, pady = 10, ipadx=2, ipady=2)

        tk.Label(text = 'To(in currency code): ', font=("Arial", 10, "bold")).grid(row=3, column=0, padx = 10, pady = 10, ipadx=2, ipady=2)

        self.currency2 = tk.StringVar(root)
        self.to_currency = ttk.Combobox(root, width=12, textvariable=self.currency2, state='readonly')
        self.to_currency['values']  = sorted(list(self.currencies.keys()))
        # self.to_currency.current(0)
        self.to_currency.set("USD")
        self.to_currency.grid(row=3, column=1, padx = 10, pady = 10, ipadx=2, ipady=2)
        
        self.click = tk.Button(text = 'Convert', command=self.action, font=("Arial", 10, "bold"))
        self.click.grid(row=4, column=0, columnspan=2, padx = 10, pady = 10, ipadx=2, ipady=2)
    
    def action(self):
        try:
            amount = float(self.amount_field.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            if from_curr != 'USD' : 
                usd_amount = amount / self.currencies[from_curr] 
  
            # limiting the precision to 4 decimal places 
            converted_amount = round(usd_amount * self.currencies[to_curr], 2)

            messagebox.showinfo(title='Converted amount', message=f"{amount} in {from_curr} is equal to{converted_amount} in {to_curr}")
        except ValueError:
            messagebox.showerror(title='Error!', message="Invalid amount! Please enter numbers only.")
    

# Main code
url = 'https://api.exchangerate-api.com/v4/latest/USD'
root = tk.Tk()
exc = app(root, url)
root.mainloop()
