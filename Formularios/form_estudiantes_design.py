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



class FormEstudiantesDesign:
    
    def __init__(self, panel_principal):
        
        # Configuración del panel principal
        self.panel_principal = (
            panel_principal  # Asegúrate de que esté correctamente escrito
        )
        
        self.barra_superior = tk.Frame(self.panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        icon_buscar = tk.PhotoImage(file="./Assets/lupa.png")
        
        # Configurar pesos para distribución uniforme
        self.barra_superior.grid_columnconfigure(0, weight=1)  # Columna del filtro
        self.barra_superior.grid_columnconfigure(1, weight=1)  # Columna del filtro
        self.barra_superior.grid_columnconfigure(2, weight=1)  # Espaciador
        self.barra_superior.grid_columnconfigure(3, weight=2)  # Barra de búsqueda
        self.barra_superior.grid_columnconfigure(4, weight=1)  # Botón "Buscar"
        self.barra_superior.grid_columnconfigure(5, weight=1)  # Botón "Inhabilitados"
                
        # Sección de selección de grado
        self.lbl_grade_select = CTkLabel(
            self.barra_superior,
            text="Filtrar por grado:",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_grade_select.grid(row=0, column=0, columnspan=2, sticky="w", padx=20)

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
        self.filtar_grado.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        
        # Barra de búsqueda
        self.lbl_search = CTkLabel(
            self.barra_superior,
            text="Buscar:",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_search.grid(row=0, column=3, sticky="w", padx=10, pady=5)

        self.search_var = tk.StringVar()
        self.entry_search = CTkEntry(
            self.barra_superior,
            textvariable=self.search_var,
            placeholder_text="Ingrese término de búsqueda",
            width=200,
            font=("Arial", 12),
            fg_color="#f0f0f0",
            text_color=COLOR_FONT_BLACK,
        )
        self.entry_search.grid(row=1, column=3, sticky="we", padx=10, pady=5)

        # Botón "Buscar"
        self.btn_search = CTkButton(
            self.barra_superior,
            text="",
            command=self.realizar_busqueda,  # Define este método más abajo
            fg_color=COLOR_FONT_PURPLE,
            text_color="white",
            width=40,
            image=icon_buscar,
            compound="right",
        )
        self.btn_search.grid(row=1, column=4, sticky="w", padx=(0,10), pady=5)

        # Botón "Inhabilitados"
        self.btn_inhabilitados = CTkButton(
            self.barra_superior,
            text="Inhabilitados",
            command=self.ver_inhabilitados,  # Define este método más abajo
            fg_color="#CDCDCD", 
            text_color="#65558F",
            hover_color= "#B3A6D6"
        )
        self.btn_inhabilitados.grid(row=0, column=5, sticky="e", padx=30, pady=5)
        
        self.cuerpo_estudiantes = tk.Frame(self.panel_principal, background="white")
        self.cuerpo_estudiantes.pack(side=tk.TOP, fill=tk.X, expand=False)
       
        # Boton ver más +
        self.btn_ver_mas = CTkButton(
            self.cuerpo_estudiantes,
            text="Ver más +",
            fg_color="#65558F",  # Color del botón
            text_color="white",
            hover_color="#B3A6D6",  # Color al pasar el mouse
            font=("Arial", 12),
        )
        self.btn_ver_mas.pack(side=tk.RIGHT, padx=10, pady=5)
        
        
        # Método para realizar búsqueda
    def realizar_busqueda(self):
        termino = self.search_var.get().strip()
        if termino:
            print(f"Buscando: {termino}")
            # Agrega aquí la lógica para buscar
        else:
            print("Por favor, ingrese un término para buscar.")

        # Método para manejar inhabilitados
    def ver_inhabilitados(self):
        print("Mostrando elementos inhabilitados.")
        # Agrega aquí la lógica para mostrar elementos inhabilitados
    
    def vista_detallada(self):
        print("Mostrando vista detallada.")
        # Agrega aquí la lógica para mostrar vista detallada del estudiante
    
                
