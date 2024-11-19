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
            self.barra_superior, text="Seleccione el grado al cual desea matricular:",
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
            self.barra_superior, text="Matriculados para este grado: 10/30",
            font=("Arial", 16,),
            text_color=COLOR_FONT_BLACK,
        )
        lbl_Numero_matriculados.grid(row=1, column=1, padx=10)
        
        # Fecha de matrícula e inicio del año
        self.label_fecha_Matricula= CTkLabel(
            self.barra_superior,
            font=("Arial", 16, "bold"),
            text="Fecha de matricula:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_fecha_Matricula.grid(
            column=0,
            row=3,
            padx=10,
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
        cal_fecha_Matricula.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        # Fecha de inicio del año
        self.label_Inicio_Año= CTkLabel(
            self.barra_superior,
            font=("Arial", 14, "bold" ),
            text="Fecha de Inicio del año:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Inicio_Año.grid(
            column=1,
            row=3,
            padx=10,
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
        cal_Inicio_año.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        #Datos personales del estudiante
        self.Datos_personales = tk.Frame(self.panel_pricipal, background="white")
        self.Datos_personales.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
        
        # Frame de Imagen
        self.frame_imagen = tk.Frame(
            self.Datos_personales, bg="white", width=100, height=100
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón para cargar imagen
        btn_cargar_imagen = CTkButton(
            self.frame_imagen, text="Cargar Foto",
        )
        btn_cargar_imagen.pack(pady=5)
        
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
            pady=(10,5),
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
            padx=(0,10),
            pady=2,
            sticky="w",
        )
        
        # Nombre de estudiante
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
            pady=(10,5),
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
            padx=(0,10),
            pady=2,
            sticky="w",
        )
        
        # Fecha de nacimiento
        self.Fecha_Nacimiento = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
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
        cal.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        
        # Nombre de estudiante
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
            pady=(10,5),
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
            padx=(0,10),
            pady=2,
            sticky="w",
        )
        # # Datos del estudiante
        # lbl_student_data = CTkLabel(frame_content, text="Datos del estudiante:", font=("Arial", 14, "bold"))
        # lbl_student_data.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

        # fields = ["Nombre completo", "Número de identificación", "Fecha de nacimiento", "Lugar de Nacimiento", "Dirección", "Teléfono"]
        # entries = {}
        # for i, field in enumerate(fields):
        #     lbl = CTkLabel(frame_content, text=field)
        #     lbl.grid(row=5 + i, column=0, padx=10, sticky="w")
        #     entries[field] = CTkEntry(frame_content)
        #     entries[field].grid(row=5 + i, column=1, padx=10, pady=5)

        # # Género
        # lbl_gender = CTkLabel(frame_content, text="Género:")
        # lbl_gender.grid(row=11, column=0, padx=20, sticky="w")
        # gender_var = tk.StringVar(value="Femenino")
        # gender_f = CTkRadioButton(frame_content, text="Femenino", variable=gender_var, value="Femenino")
        # gender_f.grid(row=11, column=1, sticky="w")
        # gender_m = CTkRadioButton(frame_content, text="Masculino", variable=gender_var, value="Masculino")
        # gender_m.grid(row=11, column=1, sticky="e")

        # # Información Académica
        # lbl_academic_info = CTkLabel(frame_content, text="Información Académica:", font=("Arial", 14, "bold"))
        # lbl_academic_info.grid(row=12, column=0, columnspan=2, pady=10, sticky="w")

        # # Tipo de estudiante (Nuevo o Antiguo)
        # student_type = tk.StringVar(value="Nuevo")
        # student_new = CTkRadioButton(frame_content, text="Nuevo", variable=student_type, value="Nuevo")
        # student_new.grid(row=13, column=0, sticky="w", padx=10)
        # student_old = CTkRadioButton(frame_content, text="Antiguo", variable=student_type, value="Antiguo")
        # student_old.grid(row=13, column=1, sticky="w")

        # # Información Médica
        # lbl_medical_info = CTkLabel(frame_content, text="Información Médica:", font=("Arial", 14, "bold"))
        # lbl_medical_info.grid(row=15, column=0, columnspan=2, pady=10, sticky="w")

        # # Alergias y enfermedades crónicas
        # allergies_var = tk.BooleanVar()
        # chk_allergies = CTkCheckBox(frame_content, text="Alergias", variable=allergies_var)
        # chk_allergies.grid(row=16, column=0, sticky="w", padx=10)

        # chronic_var = tk.BooleanVar()
        # chk_chronic = CTkCheckBox(frame_content, text="Enfermedad crónica", variable=chronic_var)
        # chk_chronic.grid(row=17, column=0, sticky="w", padx=10)

        # # Discapacidades físicas y mentales
        # physical_disability_var = tk.BooleanVar()
        # chk_physical = CTkCheckBox(frame_content, text="Discapacidad Física", variable=physical_disability_var)
        # chk_physical.grid(row=16, column=1, sticky="w", padx=10)

        # mental_disability_var = tk.BooleanVar()
        # chk_mental = CTkCheckBox(frame_content, text="Discapacidad Mental", variable=mental_disability_var)
        # chk_mental.grid(row=17, column=1, sticky="w", padx=10)
