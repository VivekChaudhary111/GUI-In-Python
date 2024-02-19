import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('400x200')
        self.mainwindow.title('Greeting App')
        self.mainwindow.minsize(100, 200)

        tk.Label(mainwindow, text="Enter your name: ").pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow, text="Enter", command=self.action)
        self.click.pack()
        self.outlabel = tk.Label(mainwindow, text="")
        self.outlabel.pack()
    def action(self):
        data = self.name_entry.get()
        self.outlabel.config(text='Hello, '+data)
        self.name_entry.delete(0,tk.END)
# Main code 
root = tk.Tk()
exc = app(root)
root.mainloop()


