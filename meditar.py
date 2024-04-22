import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("App de Meditación")
root.config(bg="#FFFBDA")

# Tamaño de la ventana 
root.geometry("500x200")

# video
def open_meditation_video():
    url = "https://www.youtube.com/watch?v=IShkpOm63gg&ab_channel=CuriosaMente"  # Reemplaza con el enlace del video de meditación deseado
    webbrowser.open(url, new=2)

# Diseño letras 
button_font = ('Helvetica', 12)  # Fuente Helvetica, tamaño 12

# Boton
Boton1 = tk.Button(root, text="Bienvenido, Haz click aqui para comenzar tu momento de relajación", command=open_meditation_video, font=button_font, bg='#FFFBDA', fg='#ED9455')
Boton1.pack(pady=20)

boton2 = tk.Button(root, text="Estamos trabajando en más", font=button_font, bg='#FFFBDA', fg='#ED9455')
boton2.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
