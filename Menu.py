import tkinter as tk
import os
import math
from tkinter import messagebox as MessageBox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def ejecutar_manual():
    ruta_ejecutable = r"C:\CajaMesaControl\CajaManual\CajaManual.exe"
    os.startfile(ruta_ejecutable)
    cerrar()

def ejecutar_automatica():
    valor=MessageBox.askquestion("Salir", "Pulse Sí solo si el CM70 está encendido y listo para comenzar sesión")
    if valor == "yes":
        ruta_ejecutable = r"C:\CajaMesaControl\CajaAutomatica\CajaAutomatica.exe"
        os.startfile(ruta_ejecutable)
        cerrar()

def cerrar():
    ventana.destroy()

def apagar():
    valor=MessageBox.askquestion("Salir", "¿Deseas salir de la aplicación y apagar el equipo?")
    if valor=="yes":
        os.system("shutdown -s")
        ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Modo Caja")

ancho_ventana = 400
alto_ventana = 200

center_window(ventana, ancho_ventana, alto_ventana)

frame = tk.Frame(ventana)
frame.pack(expand=True, fill="both")
frame.config(bg="lightblue")

# Crear etiqueta y botones
etiqueta = tk.Label(frame, text="Selecciona Modo Caja", font=("Times New Roman",12,"bold"))#,bg="#000099", fg ="#F0F8FF"
boton_manual = tk.Button(frame, text="Manual", command=ejecutar_manual, width=10, bg="green", fg="white")
boton_automatico = tk.Button(frame, text="Automática", command=ejecutar_automatica, width=10, bg="green", fg="white")
boton_apagar = tk.Button(frame, text="Apagar", command=apagar, width=10, bg="red", fg="white")

# Ubicar etiqueta y botones en la ventana
etiqueta.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
boton_manual.grid(row=1, column=0, padx=10, pady=10)
boton_automatico.grid(row=1, column=1, padx=10, pady=10)
boton_apagar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Iniciar el bucle de eventos
ventana.mainloop()