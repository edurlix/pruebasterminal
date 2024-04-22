import tkinter as tk

# Iniciamos el menu
root = tk.Tk()
root.title("STUDENT TERMINAL!!!!")
root.resizable(False, False)
root.config(bg="#FFFBDA")

# se crea un grid para la pantalla
pantalla = tk.Frame(root)
pantalla.grid(column=0, row=0)
pantalla.config(bg="#FFFBDA")

cronometro_widget = tk.LabelFrame(pantalla, text="Temporizador", border=2, fg="#ED9455", font=("Courier New", 12, "bold"))
cronometro_widget.config(bg="#FFFBDA", padx=50, pady=0)
cronometro_header = tk.Label(cronometro_widget,font=("Courier New", 16, "bold"), text="Study hard!", bg="#FFFBDA", fg="#ED9455")
cronometro_label = tk.Label(cronometro_widget, font=("Courier New", 20, "bold"), text="00 : 00 : 00", bg="#FFFBDA", fg="#ED9455")
cronometro_widget.grid(column=1, row=1, padx=5)
cronometro_label.grid(column=1, row=2, padx=10, pady=30)
cronometro_header.grid(column=1, row=1, columnspan=2)

corriendo = True


prompt_widget = tk.Entry(pantalla, width= 30 ,font=("Courier New", 12, "bold" ), fg="#ED9455", highlightbackground="#ED9455", highlightcolor="#ED9455", highlightthickness=1, border=0)
prompt_widget.grid(column=1, row=3, padx=0, pady=5)
prompt_widget.config(bg="#FFFBDA")

def cronometro(contador):
    def actualizar_contador():
        global corriendo
        nonlocal contador 
        if corriendo and contador > 0:
            contador -= 1
            hora, hora_faltante = divmod(contador, 3600)
            minutes, seconds = divmod(hora_faltante, 60)
            time_string = f"{hora:02d} :{minutes:02d} : {seconds:02d}"
            cronometro_label.config(text=time_string)
            root.after(1000, actualizar_contador)
        else:
            corriendo = False
            cronometro_label.config(text="Fin del contador")
            root.after(6000, cronometro_label.config(text="00 : 00 : 00"))

    actualizar_contador()

def iniciar_cronometro():
    global corriendo
    corriendo = True
    cronometro_widget.grid(column=1, row=1, padx=5)
    cronometro_label.grid(column=1, row=2, padx=10, pady=30)
    cronometro_header.grid(column=1, row=1, columnspan=2)


def parar_cronometro():
    global corriendo
    corriendo = False


def handle_input(event):
    user_input = prompt_widget.get().strip()
    prompt_widget.delete(0, tk.END)  # Limpiar la entrada después de capturarla

    if user_input.isdigit():
        contador = int(user_input)
        iniciar_cronometro()
        cronometro(contador)
    elif user_input.startswith("parar"):
        parar_cronometro()

prompt_widget.bind("<Return>", handle_input)


root.mainloop()