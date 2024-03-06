import tkinter as tk

root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x300")

def add_item():
    data = entry.get()  
    list_box.insert(tk.END, data)
    entry.delete(0, tk.END)

def delete_item():
    select_index = list_box.curselection()
    list_box.delete(select_index)

def delete_item_all():
    list_box.delete(0, tk.END)

entry = tk.Entry(root)
entry.grid(row=0, column=0)

bt_add = tk.Button(root, text="Add Item", command=add_item)
bt_add.grid(row=0, column=1)

list_box = tk.Listbox(root, width=20)
list_box.grid(row=1, column=0, columnspan=2)

bt_delete = tk.Button(root, text="Delete Item", command=delete_item)
bt_delete.grid(row=2, column=0)

bt_delete_all = tk.Button(root, text="Delete All Items", command=delete_item_all)  
bt_delete_all.grid(row=2, column=1)  

root.mainloop()