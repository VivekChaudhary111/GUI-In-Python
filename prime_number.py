import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('400x200')
        self.mainwindow.title('Prime number checker')
        self.mainwindow.minsize(100, 200)

        tk.Label(mainwindow, text="Enter a number: ").pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow, text="Check", command=self.action)
        self.click.pack()
        self.outlabel = tk.Label(mainwindow, text="")
        self.outlabel.pack()
    def action(self):
        data = int(self.name_entry.get())
        count = 0
        for i in range(1, int(data/2)):
            if data%i == 0:
                count += 1
        if count > 1:
            self.outlabel.config(text=str(data)+' is not a prime number.')
            self.name_entry.delete(0,tk.END)
        else:
            self.outlabel.config(text=str(data)+' is a prime number.')
            self.name_entry.delete(0,tk.END)
            
# Main code
root = tk.Tk()
exc = app(root)
root.mainloop()