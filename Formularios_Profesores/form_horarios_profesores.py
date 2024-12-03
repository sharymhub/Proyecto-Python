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
        self.panel_principal = panel_principal
        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

        # Colores materias(editar idmateria IDUS)
        self.colores_materias = {
            "Matemáticas": "#F4DD9F",  # Amarillo dorado
            "Inglés": "#A0D4F9",       # Azul
            "Lenguaje": "#F6AACF",      # Rosado
            "C.Naturales": "#C9F49F",   # Verde
            "C.Sociales": "#FD9D85",    # Rojo
            "E.Fisica": "#F9EDE1",      # Crema
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
            text_color="black",
        )
        self.lbl_grade_select.grid(row=0, column=0, sticky="w", padx=20, pady=5)

        self.grades = ["Grado 1°", "Grado 2°", "Grado 3°"]
        self.grade_var = tk.StringVar(value=self.grades[0])
        self.grade_var.trace_add("write", self._actualizar_horario)
        self.filtar_grado = CTkOptionMenu(
            self.barra_superior,
            variable=self.grade_var,
            values=self.grades,
            width=200,
            fg_color="#cdcdcd",
            button_color="white",
            button_hover_color="#5A5A5A",
            dropdown_fg_color="white",
            dropdown_hover_color="#5A5A5A",
            text_color="black",
            dropdown_text_color="black",
        )
        self.filtar_grado.grid(row=1, column=0, sticky="we", padx=20, pady=5)


        
        #<<<<<<<<<<<<<<<<<<<<< HORARIO >>>>>>>>>>>>>>><
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
                fg_color="#7D3FA6",
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
                    text="AAAA",
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

        # Horarios precargados
        self.horarios_precargados = {
            "Grado 1°": {
                "Lunes": ["Matemáticas", "Inglés", "Lenguaje","Descanso", "C.Naturales", "E.Fisica"],
                "Martes": ["Lenguaje", "Matemáticas", "Inglés","Descanso", "C.Sociales", "E.Fisica"],
                "Miércoles": ["Inglés", "Lenguaje", "C.Naturales","Descanso", "Matemáticas", "C.Sociales"],
                "Jueves": ["C.Sociales", "Matemáticas", "Inglés","Descanso", "Lenguaje", "C.Naturales"],
                "Viernes": ["E.Fisica", "Lenguaje", "C.Naturales","Descanso", "Matemáticas", "C.Sociales"],
            },
            "Grado 2°": {
                "Lunes": ["Matemáticas", "C.Sociales", "Lenguaje","Descanso", "Inglés", "E.Fisica"],
                "Martes": ["Inglés", "C.Naturales", "Matemáticas","Descanso", "Lenguaje", "E.Fisica"],
                "Miércoles": ["Lenguaje", "Matemáticas", "Inglés","Descanso", "C.Sociales", "C.Naturales"],
                "Jueves": ["Inglés", "Lenguaje", "Matemáticas","Descanso", "C.Naturales", "E.Fisica"],
                "Viernes": ["C.Sociales", "C.Naturales", "Inglés","Descanso", "Lenguaje", "E.Fisica"],
            },
            "Grado 3°": {
                "Lunes": ["Inglés", "Matemáticas", "Lenguaje","Descanso", "C.Naturales", "C.Sociales"],
                "Martes": ["C.Sociales", "Inglés", "Lenguaje","Descanso", "C.Naturales", "E.Fisica"],
                "Miércoles": ["Lenguaje", "C.Naturales", "Matemáticas","Descanso", "Inglés", "C.Sociales"],
                "Jueves": ["Matemáticas", "Inglés", "Lenguaje","Descanso", "C.Naturales", "C.Sociales"],
                "Viernes": ["E.Fisica", "Lenguaje", "Matemáticas","Descanso", "C.Sociales", "Inglés"],
            }
        }

        self._precargar_horarios()

    def _precargar_horarios(self):
        grado = self.grade_var.get()
        if grado == "Grado 3°": 
            # Dejar el horario en blanco
            for (row, col), celda in self.celdas_horario.items():
                celda.configure(text="", fg_color="white", text_color="black")
            return
        
        horarios_grado = self.horarios_precargados.get(grado)

        # Recorrer los días y las horas para cargar las materias
        for dia, materias in horarios_grado.items():
            dia_columna = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"].index(dia) + 1
            for i, materia in enumerate(materias):
                fila = i + 1
                celda = self.horario_frame.grid_slaves(row=fila, column=dia_columna)
                if celda:
                    celda[0].configure(text=materia, fg_color=self.colores_materias.get(materia, "white"), text_color="black")

    def _actualizar_horario(self, *args):
        self._precargar_horarios()
        
        
    def _toggle_horario(self, horario):
        if horario in self.horarios_seleccionados:
            self.horarios_seleccionados.remove(horario)
        elif len(self.horarios_seleccionados) < 2:
            self.horarios_seleccionados.append(horario)
        else:
            messagebox.showerror(
                "Error",
                "No puede seleccionar más de dos horarios para la misma materia."
            )
    def _guardar_horario(self, ventana):
        grado = self.grado_seleccionado.get()
        dia = self.dia_seleccionado.get()
        materia = self.materia_seleccionada.get()
        horarios = self.horarios_seleccionados
        if not horarios:
            messagebox.showerror("Error", "Debe seleccionar al menos un horario.")
            return
        # Mapea los días a columnas
        dias_indices = {"Lunes": 1, "Martes": 2, "Miércoles": 3, "Jueves": 4, "Viernes": 5}
        if dia not in dias_indices:
            messagebox.showerror("Error", "El día seleccionado no es válido.")
            return
        columna = dias_indices[dia]
        for horario in horarios:
            # Mapea los horarios a filas
            filas_indices = {
                "6:00 - 7:00": 1,
                "7:00 - 8:00": 2,
                "8:00 - 9:00": 3,
                "9:00 - 10:00": 4,
                "10:00 - 11:00": 5,
                "11:00 - 12:00": 6,
            }
            if horario not in filas_indices:
                messagebox.showerror("Error", f"El horario {horario} no es válido.")
                continue
            fila = filas_indices[horario]
            # Actualiza el texto de la celda correspondiente
            celda = self.horario_frame.grid_slaves(row=fila, column=columna)
            if celda:
                celda[0].configure(text=f"{materia}\n({grado})", fg_color=self.colores_materias.get(materia,"white"),text_color="black")
        # Mensaje de confirmación
        messagebox.showinfo("Horario actualizado", "Los datos han sido guardados correctamente.")
        ventana.destroy()

    