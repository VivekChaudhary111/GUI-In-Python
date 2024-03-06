import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('100x50')
        self.mainwindow.title('To Do List')
        self.mainwindow.minsize(500, 300)
        
        self.entry = tk.Entry(root, font=("Arial", 10, 'bold')).grid(row=0, column=0, padx = 10, pady = 10)
        self.click1 = tk.Button(text = 'Add item', font=("Arial", 10, 'bold'), command=self.add_item).grid(row=0, column=1, padx = 10, pady = 10)

        self.list_box = tk.Listbox(root, width=20, height = 10).grid(row=1, column=0)

        self.click2 = tk.Button(text = 'Delete all items', font=("Arial", 10, 'bold'), command=self.delete_item).grid(row=2, column=1, padx = 10, pady = 10)

        self.click3 = tk.Button(text = 'Undo', font=("Arial", 10, 'bold'), command=self.delete_item_all).grid(row=2, column=2, padx = 10, pady = 10)

        self.click4 = tk.Button(text = 'Delete item', font=("Arial", 10, 'bold'), command=self.undo_item).grid(row=2, column=0, padx = 10, pady = 10)

    def add_item(self):
        data = self.entry.get()
        self.list_box.insert(tk.END, data)
        self.entry.delete(0, tk.END)

    def delete_item(self):
        select_index = self.list_box.curselection()
        self.list_box.delete(select_index)

    def delete_item_all(self):
        self.list_box.delete(0, tk.END)

# Main code
root = tk.Tk()
exc = app(root)
root.mainloop()
