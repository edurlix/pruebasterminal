import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.resizable(False, False)
root.config(bg="#FFFBDA")

# se crea un grid para la pantalla
pantalla = tk.Frame(root)
pantalla.grid(column=0, row=0)
pantalla.config(bg="#FFFBDA")


def agregar_dato():
    dato = entry.get()
    if dato:
        c = tk.Checkbutton(listbox, text=dato, bg="#FFFBDA", fg="#ED9455")
        c.grid(sticky="w")
        listbox.insert(tk.END, c)
        entry.delete(0, tk.END)


todo_widget = tk.LabelFrame(pantalla, text="To do list", border=2, fg="#ED9455", font=("Courier New", 12, "bold"))
todo_widget.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
todo_widget.config(padx=60, bg="#FFFBDA")

listbox = tk.Listbox(todo_widget, font=("Courier New", 12, "bold"), bg="#FFFBDA", fg="#ED9455", border=0)
listbox.grid(sticky="nsew")

entry = tk.Entry(todo_widget, bg="#FFFBDA", fg="#ED9455")
entry.grid(row=1, column=0, pady=10, sticky="ew")

boton_agregar = tk.Button(todo_widget, text="Agregar Dato", command=agregar_dato, bg="#FFFBDA", fg="#ED9455")
boton_agregar.grid(row=2, column=0, padx=10, sticky="ew")

todo_widget.grid_columnconfigure(0, weight=1)
todo_widget.grid_rowconfigure(0, weight=1)
todo_widget.grid_rowconfigure(1, weight=1)

pantalla.mainloop()
