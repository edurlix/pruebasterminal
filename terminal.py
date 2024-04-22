import tkinter as tk
import subprocess
import os
import time
from PIL import Image, ImageTk, ImageSequence
# import pygame
import sys

# Inicializo para le audio
# pygame.mixer.init()
# Informacion del usuario
usuario = "usuario"
directorio = "/home/usuario"

# Iniciamos el menu
root = tk.Tk()
root.title("STUDENT TERMINAL!!!!")
root.resizable(False, False)
root.config(bg="#FFFBDA")

# se crea un grid para la pantalla
pantalla = tk.Frame(root)
pantalla.grid(column=0, row=0)
pantalla.config(bg="#FFFBDA")

# TERMINAL
terminal = tk.LabelFrame(pantalla, text="terminal", border=2, fg="#ED9455", font=("Courier New", 12, "bold"))
terminal.grid(column=1, row=2, columnspan=3 ,padx=10, pady=10)
terminal.config(bg="#FFFBDA")

# se crea el widget de las entradas del prompt
prompt_widget = tk.Entry(terminal, width= 100 ,font=("Courier New", 12, "bold" ), fg="#ED9455", highlightbackground="#ED9455", highlightcolor="#ED9455", highlightthickness=1, border=0)
prompt_widget.grid(column=1, row=2, padx=0, pady=5)
prompt_widget.config(bg="#FFFBDA")

# se crea un widget para tener textos
text_widget = tk.Text(terminal, width=100, height=20, font=("Courier New", 12, "bold"), wrap="word",  fg="#ED9455",border=0)
text_widget.grid(column=1, row=1, padx=12, pady=0)
text_widget.config(bg="#FFFBDA")

# # IMAGEN
# def animacion(ruta_imagen, imagen):
#     try:
#         gif = Image.open(ruta_imagen)
#         frames = []
#         for frame in ImageSequence.Iterator(gif):
#             frames.append(ImageTk.PhotoImage(frame))

#         index = 0
#         animating = True

#         def update_image():
#             nonlocal index, animating
#             if animating:
#                 imagen.config(image=frames[index])
#                 index = (index + 1) % len(frames)
#                 imagen.after(100, update_image)

#         update_image()

#     except (IOError, FileNotFoundError) as e:
#         print(f"Error loading GIF: {e}")

# ruta_imagen = "STIV.gif"  # Replace with your actual GIF path
# imagen = tk.Label(pantalla, width=100, height=10)
# imagen.grid(column=2, row=1, rowspan=1, ipadx=100 , ipady=80)

# # TEMPORIZADOR

# cronometro_widget = tk.LabelFrame(pantalla, text="Temporizador", border=2, fg="#525CEB", font=("Courier New", 12, "bold"))
# cronometro_widget.config(bg="#040D12", padx=50, pady=0)
# cronometro_header = tk.Label(cronometro_widget,font=("Courier New", 16, "bold"), text="Study hard!", bg="#040D12", fg="#525CEB")
# cronometro_label = tk.Label(cronometro_widget, font=("Courier New", 20, "bold"), text="00 : 00 : 00", bg="#040D12", fg="#525CEB")
# cronometro_widget.grid(column=1, row=1, padx=5)
# cronometro_label.grid(column=1, row=2, padx=10, pady=30)
# cronometro_header.grid(column=1, row=1, columnspan=2)

# def play():
#     pygame.mixer.music.load("Audio.mp3")
#     pygame.mixer.music.play(loops=0)


# corriendo = True
# def cronometro(contador):
#     def actualizar_contador():
#         global corriendo
#         nonlocal contador 
#         if corriendo and contador > 0:
#             contador -= 1
#             hora, hora_faltante = divmod(contador, 3600)
#             minutes, seconds = divmod(hora_faltante, 60)
#             time_string = f"{hora:02d} :{minutes:02d} : {seconds:02d}"
#             cronometro_label.config(text=time_string)
#             root.after(1000, actualizar_contador)
#         else:
#             corriendo = False
#             cronometro_label.config(text="Fin del contador")
#             play()
#             root.after(6000, cronometro_label.config(text="00 : 00 : 00"))

#     actualizar_contador()

# def iniciar_cronometro():
#     global corriendo
#     corriendo = True
#     cronometro_widget.grid(column=1, row=1, padx=5)
#     cronometro_label.grid(column=1, row=2, padx=10, pady=30)
#     cronometro_header.grid(column=1, row=1, columnspan=2)


# def parar_cronometro():
#     global corriendo
#     corriendo = False

# # TO DO LIST
# todo_widget = tk.LabelFrame(pantalla, text="To do list", border=2, fg="#525CEB", font=("Courier New", 12, "bold") )
# todo_widget.grid(column=3, row=1, padx=5)
# todo_widget.config(padx=60, bg="#040D12")
# listbox = tk.Listbox(todo_widget, font=("Courier New", 12, "bold"), bg="#040D12", fg="#525CEB", border=0)
# listbox.grid()

# def agregar_dato():
#     dato = entry.get()
#     if dato:
#         c = tk.Checkbutton(listbox, text=dato,  bg="#040D12", fg="#525CEB")
#         c.grid()
#         c.config(padx=10)
#         listbox.insert(tk.END, c)
#         entry.delete(0, tk.END)

# entry = tk.Entry(todo_widget, bg="#040D12", fg="#525CEB")
# entry.grid(pady=10)

# boton_agregar = tk.Button(todo_widget, text="Agregar Dato", command=agregar_dato,  bg="#040D12", fg="#525CEB")
# boton_agregar.grid(padx=10)


# Funcion para actualizar el display
def actualizar_display(text):
    text_to_insert = f"{usuario}@{directorio} $: {text}\n"
    text_widget.insert("end", text_to_insert)
    text_widget.see("end")

# Creamos nuestros propios comandos
def instrucciones():
    output = """
            las instrucciones son:
            - 1. Puedes usar la mayoria de los comandos de shell, a excepcion de (cd, clear, etc...)
"""
    actualizar_display(output)

def clear():
    text_widget.delete('1.0', tk.END)
    text_to_insert = f"{usuario}@{directorio} $:\n"
    text_widget.insert("end", text_to_insert)
    text_widget.see("end")


# Funcion para capturar lo que el usuario ingrese y simule los comandos
def handle_input(event):
    user_input = prompt_widget.get().strip()
    prompt_widget.delete(0, tk.END)  # Limpiar la entrada después de capturarla

    if user_input == "instrucciones":
        instrucciones()
    elif user_input == "clear":
        clear()
    # elif user_input.startswith("temporizador"):
    #     contador = int(user_input.split()[1])
    #     output = f"Temporizador {contador}"
    #     iniciar_cronometro()
    #     cronometro(contador)
    # elif user_input == "pid":
    #     pid()
    # elif user_input.startswith("parar"):
    #     output = "parar"
    #     parar_cronometro()
    #     actualizar_display(output)
    else:
        try:
            if os.name == "nt":
                proceso = subprocess.run(user_input, capture_output=True, text=True, shell=True)
            else:
                proceso = subprocess.run(user_input.split(), capture_output=True, text=True)
                
            if proceso.returncode == 0:
                output = proceso.stdout
            else:
                output = proceso.stderr
            actualizar_display(output)
        except Exception as e:
            error_message = f"Error al ejecutar el comando: {str(e)}"
            actualizar_display(error_message)


# Redirige la salida estándar a la función actualizar_display
sys.stdout = text_widget

# Enlaza la funcion al boton de enter cuando se presiona
prompt_widget.bind("<Return>", handle_input)
# animacion(ruta_imagen, imagen)
actualizar_display(" ")

# Main loop 
root.mainloop()
