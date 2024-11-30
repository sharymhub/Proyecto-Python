import tkinter as tk
from util.util_imagenes import leer_imagen
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter import messagebox
from tkinter import StringVar
import re
from PIL import Image, ImageTk
from config import (
    COLOR_CUERPO_PRINCIPAL,
    COLOR_MENU_LATERAL,
    COLOR_FONT_PURPLE,
    COLOR_FONT_BLACK,
    COLOR_BARRA_SUPERIOR,
    COLOR_FONT_WHITE,
    COLOR_MENU_CURSOR_ENCIMA,
)
from customtkinter import (
    CTk,
    CTkFrame,
    CTkEntry,
    CTkButton,
    CTkLabel,
    CTkCheckBox,
    CTkOptionMenu,
    CTkImage,
    CTkRadioButton,
)

class FormularioHorariosVista:
    def __init__(self, panel_principal):
        # Configuración del panel principal
        self.panel_principal = (
            panel_principal  # Asegúrate de que esté correctamente escrito
        )
        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")
        
        #Colores materias
        self.colores_materias = {
            "Matemáticas": "#F4DD9F",  # Amarillo dorado
            "Inglés": "#A0D4F9",       # Azul
            "Lenguaje": "#F6AACF",  #Rosado
            "C.Naturales": "#C9F49F", #Verde
            "C.Sociales" : "#FD9D85", #Rojo
            "E.Fisica" : "#F9EDE1", #Crema
  
        }
        
        self.barra_superior = tk.Frame(self.panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        # Configuración del grid
        self.barra_superior.grid_columnconfigure(0, weight=1)  # Columna para etiqueta
        self.barra_superior.grid_columnconfigure(1, weight=1)  # Columna para menú
        self.barra_superior.grid_columnconfigure(2, weight=1)  # Columna para botón
                
        # Sección de selección de grado
        self.lbl_grade_select = CTkLabel(
            self.barra_superior,
            text="Filtrar por grado:",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_grade_select.grid(row=0, column=0, sticky="w", padx=20, pady=5)

        self.grades = ["Grado 1°", "Grado 2°", "Grado 3°"]
        self.grade_var = tk.StringVar(value=self.grades[0])
        self.filtar_grado = CTkOptionMenu(
            self.barra_superior,
            variable=self.grade_var,
            values=self.grades,
            width=200,
            fg_color="#cdcdcd",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.filtar_grado.grid(row=1, column=0, sticky="we", padx=20, pady=5)
        
        #<<<<<<<<<<<<<< HORARIO >>>>>>>>>><
        # Frame del horario
        self.horario_frame = CTkFrame(
            self.panel_principal,
            fg_color="white",
            corner_radius=15,
        )
        self.horario_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Almacena las celdas del horario
        self.celdas_horario = {}
        self._crear_horario()

    def _crear_horario(self):
        # Días y horas
        dias = ["Hora", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horas = [f"{h}:00 - {h + 1}:00" for h in range(6, 9)] + ["9:00 - 10:00 (Descanso)"] + [f"{h}:00 - {h + 1}:00" for h in range(10, 12)]

        # Crear la cuadrícula
        for i, dia in enumerate(dias):
            header = CTkLabel(
                self.horario_frame,
                text=dia,
                font=("Arial", 14, "bold"),
                text_color="white",
                fg_color=COLOR_FONT_PURPLE,
                corner_radius=10,
            )
            header.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

        for i, hora in enumerate(horas):
            hora_label = CTkLabel(
                self.horario_frame,
                text=hora,
                font=("Arial", 12),
                text_color="black",
                fg_color="#e1e1e1",
                corner_radius=5,
            )
            hora_label.grid(row=i + 1, column=0, sticky="nsew", padx=5, pady=5)

        # Agregar celdas para actividades
        for row in range(1, len(horas) + 1):
            for col in range(1, len(dias)):
                actividad_celda = CTkLabel(
                    self.horario_frame,
                    text="",
                    font=("Arial", 12),
                    text_color="black",
                    fg_color="white",
                    corner_radius=5,
                )
                actividad_celda.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                self.celdas_horario[(row, col)] = actividad_celda
                
        # Ajustar pesos para distribuir el espacio
        for i in range(len(dias)):
            self.horario_frame.columnconfigure(i, weight=1)
        for i in range(len(horas) + 1):
            self.horario_frame.rowconfigure(i, weight=1)
    