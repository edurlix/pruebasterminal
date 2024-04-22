import os
import tkinter as tk
from tkinter import filedialog, ttk

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        display_folder_contents(folder_path)

def display_folder_contents(folder_path):
    for widget in file_tree.get_children():
        file_tree.delete(widget)

    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isdir(file_path):
            file_tree.insert('', 'end', text=file_name, open=False, values=("Folder", file_path), tags=("folder",))
        else:
            file_tree.insert('', 'end', text=file_name, open=False, values=("File", file_path), tags=("file",))

def open_item(event):
    item = file_tree.selection()[0]
    item_type = file_tree.item(item, "values")[0]
    item_path = file_tree.item(item, "values")[1]
    
    if item_type == "Folder":
        display_folder_contents(item_path)
    else:
        os.startfile(item_path)

root = tk.Tk()
root.title("File System Explorer")
root.geometry("600x400")
root.configure(background="#FFFBDA")

style = ttk.Style(root)
style.configure("Treeview", background="#FFFBDA", fieldbackground="#FFFBDA", foreground="#ED9455")
style.configure("Treeview.Heading", foreground="#ED9455")

file_tree = ttk.Treeview(root)
file_tree['columns'] = ('Type', 'Path')
file_tree.heading('#0', text='Name', anchor='w')
file_tree.heading('Type', text='Type', anchor='w')
file_tree.heading('Path', text='Path', anchor='w')
file_tree.pack(expand=True, fill='both')

scrollbar = ttk.Scrollbar(root, orient='vertical', command=file_tree.yview)
scrollbar.pack(side='right', fill='y')
file_tree.configure(yscrollcommand=scrollbar.set)

browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

file_tree.bind("<Double-1>", open_item)

root.mainloop()
