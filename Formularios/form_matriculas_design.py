import tkinter as tk
from util.util_imagenes import leer_imagen
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter import messagebox
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


class FormMatriculasDesign:
    def __init__(self, panel_principal):
        self.panel_pricipal = panel_principal
        self.barra_superior = tk.Frame(self.panel_pricipal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Título
        lbl_title = CTkLabel(
            self.barra_superior,
            text="Nueva Matrícula",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        lbl_title.grid(row=0, column=0, padx=20, pady=10)

        # Sección de selección de grado
        lbl_grade_select = CTkLabel(
            self.barra_superior,
            text="Seleccione el grado al cual desea matricular:",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
        )
        lbl_grade_select.grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

        grades = ["Grado 1°", "Grado 2°", "Grado 3°"]
        grade_var = tk.StringVar(value=grades[0])
        menu_grade = CTkOptionMenu(
            self.barra_superior,
            variable=grade_var,
            values=grades,
            width=200,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        menu_grade.grid(row=2, column=0, padx=30, pady=5)

        lbl_Numero_matriculados = CTkLabel(
            self.barra_superior,
            text="Matriculados para este grado: 10/30",
            font=(
                "Arial",
                16,
            ),
            text_color=COLOR_FONT_BLACK,
        )
        lbl_Numero_matriculados.grid(row=1, column=1, padx=10)

        # Fecha de matrícula e inicio del año
        self.label_fecha_Matricula = CTkLabel(
            self.barra_superior,
            font=("Arial", 16, "bold"),
            text="Fecha de matricula:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_fecha_Matricula.grid(
            column=0,
            row=3,
            padx=15,
            pady=2,
            sticky="w",
        )

        cal_fecha_Matricula = DateEntry(
            self.barra_superior,
            width=18,
            background=COLOR_FONT_WHITE,
            foreground=COLOR_FONT_BLACK,
            borderwidth=0,
            date_pattern="y-mm-dd",
            selectforeground=COLOR_FONT_WHITE,
            selectbackground=COLOR_FONT_PURPLE,
            font=("Arial", 8),
        )
        cal_fecha_Matricula.grid(row=4, column=0, padx=15, pady=10, sticky="w")

        # Fecha de inicio del año
        self.label_Inicio_Año = CTkLabel(
            self.barra_superior,
            font=("Arial", 14, "bold"),
            text="Fecha de Inicio del año:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Inicio_Año.grid(
            column=1,
            row=3,
            padx=15,
            pady=2,
            sticky="w",
        )

        cal_Inicio_año = DateEntry(
            self.barra_superior,
            width=18,
            background=COLOR_FONT_WHITE,
            foreground=COLOR_FONT_BLACK,
            borderwidth=0,
            date_pattern="y-mm-dd",
            selectforeground=COLOR_FONT_WHITE,
            selectbackground=COLOR_FONT_PURPLE,
            font=("Arial", 8),
        )
        cal_Inicio_año.grid(row=4, column=1, padx=15, pady=10, sticky="w")

        # Datos personales del estudiante
        self.Datos_personales = tk.Frame(self.panel_pricipal, background="white")
        self.Datos_personales.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

        # Frame de Imagen
        self.frame_imagen = tk.Frame(
            self.Datos_personales, bg="white", width=100, height=100
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón para cargar imagen
        btn_cargar_imagen = CTkButton(
            self.frame_imagen,
            text="Cargar Foto",
        )
        btn_cargar_imagen.pack(pady=10)

        # Frame para información del texto
        self.texto_frame = CTkFrame(self.Datos_personales, fg_color="white")
        self.texto_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, expand=True)

        # Nombre de estudiante
        self.nombre_label = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Nombre completo:",
            text_color=COLOR_FONT_BLACK,
        )
        self.nombre_label.grid(
            column=0,
            row=0,
            sticky="w",
            pady=(10, 5),
        )

        self.entry_nombre = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_nombre.grid(
            column=0,
            row=1,
            padx=(0, 10),
            pady=2,
            sticky="w",
        )

        # Numero de identificación
        self.numero_identificacion = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Numero de identificación:",
            text_color=COLOR_FONT_BLACK,
        )
        self.numero_identificacion.grid(
            column=1,
            row=0,
            sticky="w",
            padx=10,
            pady=(10, 5),
        )

        self.entry_numero_identificación = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_numero_identificación.grid(
            column=1,
            row=1,
            padx=10,
            pady=2,
            sticky="w",
        )

        # Fecha de nacimiento
        self.Fecha_Nacimiento = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Fecha de nacimiento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Fecha_Nacimiento.grid(column=0, row=2, sticky="w")

        # Crear y colocar el selector de fecha
        cal = DateEntry(
            self.texto_frame,
            width=18,
            background=COLOR_FONT_WHITE,
            foreground=COLOR_FONT_BLACK,
            borderwidth=0,
            date_pattern="y-mm-dd",
            selectforeground=COLOR_FONT_WHITE,
            selectbackground=COLOR_FONT_PURPLE,
            font=("Arial", 10),
        )
        cal.grid(row=3, column=0, padx=5, pady=2, sticky="w")

        # Lugar de nacimiento
        self.Lugar_Nacimiento = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Lugar de nacimiento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Lugar_Nacimiento.grid(
            column=1,
            row=2,
            sticky="w",
            padx=10,
            pady=(10, 5),
        )

        self.entry_Lugar_Nacimiento = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_Lugar_Nacimiento.grid(
            column=1,
            row=3,
            padx=2,
            pady=2,
        )

        # Género
        self.lbl_gender = CTkLabel(
            self.texto_frame,
            text="Género:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_gender.grid(row=4, column=0, pady=(10, 5), sticky="w")

        # Definir la variable de género
        self.gender_var = tk.StringVar(value="Femenino")

        # Botón de radio para "Femenino"
        self.gender_f = CTkRadioButton(
            self.texto_frame,
            text="Femenino",
            variable=self.gender_var,
            value="Femenino",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.gender_f.grid(row=5, column=0, sticky="w")

        # Botón de radio para "Masculino"
        self.gender_m = CTkRadioButton(
            self.texto_frame,
            text="Masculino",
            variable=self.gender_var,
            value="Masculino",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.gender_m.grid(row=5, column=0, padx=(0, 25), sticky="e")

        # Telefono
        self.telefono = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Telefono:",
            text_color=COLOR_FONT_BLACK,
        )

        self.telefono.grid(
            row=4,
            column=1,
            sticky="w",
            padx=10,
            pady=(10, 5),
        )

        self.entry_telefono = CTkEntry(
            self.texto_frame,
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            font=("Arial", 14),
            fg_color="white",
        )

        self.entry_telefono.grid(row=5, column=1, padx=10, pady=2)

        # Dirección
        self.direccion = CTkLabel(
            self.texto_frame,
            font=("Arial", 14, "bold"),
            text="Dirección:",
            text_color=COLOR_FONT_BLACK,
        )
        self.direccion.grid(row=6, column=0, sticky="w")

        self.entry_direccion = CTkEntry(
            self.texto_frame,
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            font=("Arial", 14),
            fg_color="white",
        )

        self.entry_direccion.grid(row=7, column=0, padx=(0, 10), pady=2)

        # <<<<<<<<<<<<<<<<<< INFORMACION ACADEMICA >>>>>>>>>>>>>>>>>>>
        self.Datos_academicos = tk.Frame(self.panel_pricipal, background="white")
        self.Datos_academicos.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

        self.label_Informacion = CTkLabel(
            self.Datos_academicos,
            text="Información Académica",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_Informacion.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.label_tipo_estudiante = CTkLabel(
            self.Datos_academicos,
            font=("Arial", 14, "bold"),
            text="Tipo de estudiante:",
            text_color=COLOR_FONT_BLACK,
        )

        self.label_tipo_estudiante.grid(row=1, column=0, padx=10, sticky="w")

        # Definir la variable de tipo de estudiantes
        self.student_var = tk.StringVar(value="Nuevo")

        # Botón de radio para "Nuevo"
        self.studentN_type = CTkRadioButton(
            self.Datos_academicos,
            text="Nuevo",
            variable=self.student_var,
            value="Femenino",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.studentN_type.grid(row=2, column=0, sticky="w", padx=(10, 25))

        # Botón de radio para "ANTIGUO"
        self.studentA_type = CTkRadioButton(
            self.Datos_academicos,
            text="Antiguo",
            variable=self.student_var,
            value="Masculino",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.studentA_type.grid(row=2, column=0, padx=(0, 25), sticky="e")

        self.label_grado_cursado = CTkLabel(
            self.Datos_academicos,
            text="Ingrese el grado que estaba cursando:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.label_grado_cursado.grid(row=3, column=0, sticky="w", padx=10)
        self.entry_grado_cursado = CTkEntry(
            self.Datos_academicos,
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            font=("Arial", 14),
            fg_color="white",)
        self.entry_grado_cursado.grid(row=4, column=0, padx=10, pady=(10, 5),sticky="w" )