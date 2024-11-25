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


class FormMatriculasDesign:

    def __init__(self, panel_principal):
        # Configuración del panel principal
        self.panel_principal = (
            panel_principal  # Asegúrate de que esté correctamente escrito
        )

        # Crear un contenedor principal con Canvas y Scrollbar
        self.canvas_frame = tk.Frame(self.panel_principal, bg="white")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(
            self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame interior que contendrá todo el contenido
        self.content_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Vincular el evento para redimensionar y ajustar el Canvas
        self.content_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # <<<<<<<Funciones de validacion>>>>>>><<<<
        def validar_nombre(texto):
            """Permite solo letras y espacios en el nombre."""
            return texto.replace(" ", "").isalpha() or texto == ""

        def validar_telefono(texto):
            """Permite solo números y restringe a 10 dígitos."""
            return texto.isdigit() and (len(texto) <= 10) or texto == ""

        def validar_direccion(texto):
            """Permite letras, números, espacios y algunos caracteres especiales para direcciones."""
            caracteres_validos = (
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,/-"
            )
            return all(c in caracteres_validos for c in texto) or texto == ""

        def validar_entrada_numerica(texto):
            return texto.isdigit() or texto == ""
        
        # Función para validar correo electrónico
        def validar_correo(texto):
            patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return bool(re.match(patron, texto)) or texto == ""
        
        def asociar_validacion(entry_widget, tipo):
            """
            Vincula la validación al evento <KeyRelease> del Entry.
            """
            def validar_texto(event):
                texto = entry_widget.get()
                if tipo == "correo":
                    if not validar_correo(texto):
                        entry_widget.configure(border_color="red")
                    else:
                        entry_widget.configure(border_color="green")

            entry_widget.bind("<KeyRelease>", validar_texto)

        # Registrar funciones de validación
        validacion_nombre = self.content_frame.register(validar_nombre)
        validacion_telefono = self.content_frame.register(validar_telefono)
        validacion_direccion = self.content_frame.register(validar_direccion)
        validacion_numerica = self.content_frame.register(validar_entrada_numerica)

        # Barra superior
        self.barra_superior = tk.Frame(self.content_frame, background="white")
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
            fg_color="#cdcdcd",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        menu_grade.grid(row=2, column=0, padx=50, pady=5)

        lbl_Numero_matriculados = CTkLabel(
            self.barra_superior,
            text="Matriculados para este grado: 10/30",
            font=(
                "Arial",
                16,
            ),
            text_color=COLOR_FONT_BLACK,
        )
        lbl_Numero_matriculados.grid(row=1, column=1, padx=30, sticky="e")

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
            state="readonly",
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
            state="readonly",
        )
        cal_Inicio_año.grid(row=4, column=1, padx=15, pady=10, sticky="w")

        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCION DATOS PERSONALES DEL ESTUDIANTE>>>>>>>>>>>>>>><<<<
        # Datos personales del estudiante
        self.Datos_personales = tk.Frame(self.content_frame, background="white")
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
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=35,
            width=180,
            command=self.cargar_imagen,
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
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_nombre, "%P"),
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
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_numerica, "%P"),  # Llamar a la validación
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
            state="readonly",
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
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_telefono, "%P"),
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
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_direccion, "%P"),
        )

        self.entry_direccion.grid(row=7, column=0, padx=(0, 10), pady=2)

        # <<<<<<<<<<<<<<<<<< INFORMACION ACADEMICA >>>>>>>>>>>>>>>>>>>
        self.Datos_academicos = tk.Frame(self.content_frame, background="white")
        self.Datos_academicos.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

        self.label_Informacion = CTkLabel(
            self.Datos_academicos,
            text="Información Académica",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_Informacion.grid(row=0, column=0, padx=10, pady=5)

        self.label_tipo_estudiante = CTkLabel(
            self.Datos_academicos,
            font=("Arial", 14, "bold"),
            text="Tipo de estudiante:",
            text_color=COLOR_FONT_BLACK,
        )

        self.label_tipo_estudiante.grid(row=1, column=0, padx=10, sticky="w")

        # Definir la variable de tipo de estudiantes

        def actualizar_widgets_nombre_colegio(*args):
            if self.student_var.get() == "Nuevo":
                self.label_Nombre_Colegio_anterior.grid(
                    row=3, column=1, sticky="w", padx=10
                )
                self.entry_Nombre_colegio.grid(
                    row=4, column=1, padx=10, pady=(10, 5), sticky="w"
                )
            else:
                self.label_Nombre_Colegio_anterior.grid_forget()
                self.entry_Nombre_colegio.grid_forget()

        # Crear la variable y vincularla al método
        self.student_var = tk.StringVar(value="Antiguo")
        self.student_var.trace("w", actualizar_widgets_nombre_colegio)

        # Botón de radio para "Nuevo"
        self.studentN_type = CTkRadioButton(
            self.Datos_academicos,
            text="Nuevo",
            variable=self.student_var,
            value="Nuevo",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.studentN_type.grid(row=2, column=0, sticky="w", padx=(10, 25))

        # Botón de radio para "Antiguo"
        self.studentA_type = CTkRadioButton(
            self.Datos_academicos,
            text="Antiguo",
            variable=self.student_var,
            value="Antiguo",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
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
        self.grades = ["Grado 1°", "Grado 2°", "Grado 3°", "Grado 4°", "Grado 5"]
        self.grado_cursado_var = tk.StringVar(value=grades[0])
        self.menu_grado_cursado = CTkOptionMenu(
            self.Datos_academicos,
            variable=self.grado_cursado_var,
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
        self.menu_grado_cursado.grid(row=4, column=0, padx=5, pady=5)

        # Widgets para "Nombre Colegio"
        self.label_Nombre_Colegio_anterior = CTkLabel(
            self.Datos_academicos,
            text="Ingrese el nombre del colegio anterior:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.entry_Nombre_colegio = CTkEntry(
            self.Datos_academicos,
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            font=("Arial", 14),
            fg_color="white",
        )

        # Llamar al método para establecer el estado inicial
        actualizar_widgets_nombre_colegio()

        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCION INFORMACION MEDICA  >>>>>>>>>>>>>><<<<
        self.Datos_medicos = tk.Frame(self.content_frame, background="white")
        self.Datos_medicos.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

        self.label_Informacion = CTkLabel(
            self.Datos_medicos,
            text="Información Medica",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_Informacion.grid(row=0, column=0, padx=10, pady=5)

        self.frame_izquierda = tk.Frame(self.Datos_medicos, background="white")
        self.frame_izquierda.grid(padx=5, pady=(5, 5), sticky="w", row=1, column=0)

        # --- Alergias ---
        self.alergias_label = CTkLabel(
            self.frame_izquierda,
            text="Alergias:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.alergias_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Variable para almacenar la selección de los Checkbuttons
        self.alergia_var = StringVar(value="No")

        # Checkbuttons para "Sí" y "No"
        self.check_si = CTkRadioButton(
            self.frame_izquierda,
            text="Sí",
            variable=self.alergia_var,
            value="Sí",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.check_si.grid(row=0, column=1, padx=(10, 2), pady=10, sticky="w")

        self.check_no = CTkRadioButton(
            self.frame_izquierda,
            text="No",
            variable=self.alergia_var,
            value="No",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,  # Color del texto
            hover_color=COLOR_MENU_CURSOR_ENCIMA,  # Color cuando el cursor pasa sobre el botón
            fg_color=COLOR_FONT_PURPLE,  # Color de fondo del radio button
            border_color=COLOR_FONT_BLACK,  # Color del borde
            corner_radius=10,
        )
        self.check_no.grid(row=0, column=2, padx=(2, 10), pady=10, sticky="w")

        # Etiqueta para "¿Cuál?" que aparece solo si se selecciona "Sí"
        self.cual_label = CTkLabel(
            self.frame_izquierda,
            text="¿Cuál?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.cual_label.grid(row=0, column=3, padx=(10, 10), pady=10, sticky="w")

        # Entry para ingresar el nombre de la alergia (si la respuesta es "Sí")
        self.alergia_entry = CTkEntry(
            self.frame_izquierda,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.alergia_entry.grid(row=0, column=4, padx=0, pady=10, sticky="w")

        # Función para habilitar o deshabilitar el Entry y el Label "¿Cuál?" según la selección
        def toggle_entry():
            if self.alergia_var.get() == "Sí":
                self.cual_label.configure(state="normal")
                self.alergia_entry.configure(state="normal")
            else:
                self.cual_label.configure(state="disabled")
                self.alergia_entry.configure(state="disabled")

        # Asignar la función a los botones de opción
        self.check_si.configure(command=toggle_entry)
        self.check_no.configure(command=toggle_entry)

        # --- Enfermedades Crónicas ---
        self.enfermedades_label = CTkLabel(
            self.frame_izquierda,
            text="Enfermedades Crónicas:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.enfermedades_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.enfermedades_var = StringVar(value="No")

        self.check_si_enfermedad = CTkRadioButton(
            self.frame_izquierda,
            text="Sí",
            variable=self.enfermedades_var,
            value="Sí",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_si_enfermedad.grid(
            row=1, column=1, padx=(10, 2), pady=10, sticky="w"
        )

        self.check_no_enfermedad = CTkRadioButton(
            self.frame_izquierda,
            text="No",
            variable=self.enfermedades_var,
            value="No",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_no_enfermedad.grid(
            row=1, column=2, padx=(2, 10), pady=10, sticky="w"
        )

        self.cual_label_enfermedad = CTkLabel(
            self.frame_izquierda,
            text="¿Cuál?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.cual_label_enfermedad.grid(
            row=1, column=3, padx=(10, 10), pady=10, sticky="w"
        )

        self.enfermedad_entry = CTkEntry(
            self.frame_izquierda,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.enfermedad_entry.grid(row=1, column=4, padx=0, pady=10, sticky="w")

        def toggle_entry_enfermedad():
            if self.enfermedades_var.get() == "Sí":
                self.cual_label_enfermedad.configure(state="normal")
                self.enfermedad_entry.configure(state="normal")
            else:
                self.cual_label_enfermedad.configure(state="disabled")
                self.enfermedad_entry.configure(state="disabled")

        self.check_si_enfermedad.configure(command=toggle_entry_enfermedad)
        self.check_no_enfermedad.configure(command=toggle_entry_enfermedad)

        # --- Toma Medicamentos ---
        self.medicamentos_label = CTkLabel(
            self.frame_izquierda,
            text="Toma Medicamentos?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.medicamentos_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.medicamentos_var = StringVar(value="No")

        self.check_si_medicamento = CTkRadioButton(
            self.frame_izquierda,
            text="Sí",
            variable=self.medicamentos_var,
            value="Sí",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_si_medicamento.grid(
            row=2, column=1, padx=(10, 2), pady=10, sticky="w"
        )

        self.check_no_medicamento = CTkRadioButton(
            self.frame_izquierda,
            text="No",
            variable=self.medicamentos_var,
            value="No",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_no_medicamento.grid(
            row=2, column=2, padx=(2, 10), pady=10, sticky="w"
        )

        self.cual_label_medicamento = CTkLabel(
            self.frame_izquierda,
            text="¿Cuál?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.cual_label_medicamento.grid(
            row=2, column=3, padx=(10, 10), pady=10, sticky="w"
        )

        self.medicamento_entry = CTkEntry(
            self.frame_izquierda,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.medicamento_entry.grid(row=2, column=4, padx=0, pady=10, sticky="w")

        def toggle_entry_medicamento():
            if self.medicamentos_var.get() == "Sí":
                self.cual_label_medicamento.configure(state="normal")
                self.medicamento_entry.configure(state="normal")
            else:
                self.cual_label_medicamento.configure(state="disabled")
                self.medicamento_entry.configure(state="disabled")

        self.check_si_medicamento.configure(command=toggle_entry_medicamento)
        self.check_no_medicamento.configure(command=toggle_entry_medicamento)

        # --- Discapacidad Física ---
        self.discapacidad_fisica_label = CTkLabel(
            self.frame_izquierda,
            text="Discapacidad Física:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.discapacidad_fisica_label.grid(
            row=3, column=0, padx=10, pady=10, sticky="w"
        )

        self.discapacidad_fisica_var = StringVar(value="No")

        self.check_si_fisica = CTkRadioButton(
            self.frame_izquierda,
            text="Sí",
            variable=self.discapacidad_fisica_var,
            value="Sí",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_si_fisica.grid(row=3, column=1, padx=(10, 2), pady=10, sticky="w")

        self.check_no_fisica = CTkRadioButton(
            self.frame_izquierda,
            text="No",
            variable=self.discapacidad_fisica_var,
            value="No",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_no_fisica.grid(row=3, column=2, padx=(2, 10), pady=10, sticky="w")

        self.cual_label_fisica = CTkLabel(
            self.frame_izquierda,
            text="¿Cuál?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.cual_label_fisica.grid(row=3, column=3, padx=(10, 10), pady=10, sticky="w")

        self.fisica_entry = CTkEntry(
            self.frame_izquierda,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.fisica_entry.grid(row=3, column=4, padx=0, pady=10, sticky="w")

        def toggle_entry_fisica():
            if self.discapacidad_fisica_var.get() == "Sí":
                self.cual_label_fisica.configure(state="normal")
                self.fisica_entry.configure(state="normal")
            else:
                self.cual_label_fisica.configure(state="disabled")
                self.fisica_entry.configure(state="disabled")

        self.check_si_fisica.configure(command=toggle_entry_fisica)
        self.check_no_fisica.configure(command=toggle_entry_fisica)

        # --- Discapacidad Mental ---
        self.discapacidad_mental_label = CTkLabel(
            self.frame_izquierda,
            text="Discapacidad Mental:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.discapacidad_mental_label.grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )

        self.discapacidad_mental_var = StringVar(value="No")

        self.check_si_mental = CTkRadioButton(
            self.frame_izquierda,
            text="Sí",
            variable=self.discapacidad_mental_var,
            value="Sí",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_si_mental.grid(row=4, column=1, padx=(10, 2), pady=10, sticky="w")

        self.check_no_mental = CTkRadioButton(
            self.frame_izquierda,
            text="No",
            variable=self.discapacidad_mental_var,
            value="No",
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_no_mental.grid(row=4, column=2, padx=(2, 10), pady=10, sticky="w")

        self.cual_label_mental = CTkLabel(
            self.frame_izquierda,
            text="¿Cuál?",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.cual_label_mental.grid(row=4, column=3, padx=(10, 10), pady=10, sticky="w")

        self.mental_entry = CTkEntry(
            self.frame_izquierda,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.mental_entry.grid(row=4, column=4, padx=0, pady=10, sticky="w")

        def toggle_entry_mental():
            if self.discapacidad_mental_var.get() == "Sí":
                self.cual_label_mental.configure(state="normal")
                self.mental_entry.configure(state="normal")
            else:
                self.cual_label_mental.configure(state="disabled")
                self.mental_entry.configure(state="disabled")

        self.check_si_mental.configure(command=toggle_entry_mental)
        self.check_no_mental.configure(command=toggle_entry_mental)

        # --- Grupo Sanguíneo ---
        self.grupo_sanguineo_label = CTkLabel(
            self.frame_izquierda,
            text="Grupo Sanguíneo:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.grupo_sanguineo_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Lista de tipos de sangre
        tipos_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        # Variable para almacenar el tipo de sangre seleccionado
        self.grupo_sanguineo_var = StringVar(value=tipos_sangre[0])  # Por defecto "A+"

        # Opción de menú (OptionMenu) para seleccionar el grupo sanguíneo
        self.grupo_sanguineo_menu = CTkOptionMenu(
            self.frame_izquierda,
            variable=self.grupo_sanguineo_var,
            values=tipos_sangre,
            font=("Arial", 12),
            width=80,
            text_color=COLOR_FONT_BLACK,
            fg_color="#cdcdcd",
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.grupo_sanguineo_menu.grid(
            row=5, column=1, padx=(10, 2), pady=10, sticky="w"
        )

        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCION INFORMACION DE LOS PADRES >>>>>>>>>>>>>>
        # --- Información de los Padres ---
        self.info_padres_label = CTkLabel(
            self.content_frame,
            text="Información de los Padres",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.info_padres_label.pack(
            padx=10,
            pady=(10, 5),
            fill=tk.BOTH,
            expand=True,
        )

        # --- Información de la Madre ---
        self.info_madre_label = CTkLabel(
            self.content_frame,
            text="Información de la Madre",
            font=("Arial", 18, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.info_madre_label.pack(padx=10, pady=(10, 5), anchor="w")

        # Frame para los campos de la madre
        self.frame_madre = tk.Frame(self.content_frame, background="white")
        self.frame_madre.pack(padx=10, pady=(5, 10), fill=tk.BOTH, expand=True)

        # Etiquetas y Entrys para la Madre
        self.madre_nombre_label = CTkLabel(
            self.frame_madre,
            text="Nombre Completo:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.madre_nombre_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.madre_nombre_entry = CTkEntry(
            self.frame_madre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_nombre, "%P"),
        )
        self.madre_nombre_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.madre_telefono_label = CTkLabel(
            self.frame_madre,
            text="Teléfono:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.madre_telefono_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.madre_telefono_entry = CTkEntry(
            self.frame_madre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_telefono, "%P"),
        )
        self.madre_telefono_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.madre_correo_label = CTkLabel(
            self.frame_madre,
            text="Correo Electrónico:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.madre_correo_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.madre_correo_entry = CTkEntry(
            self.frame_madre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.madre_correo_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        asociar_validacion(self.madre_correo_entry, tipo="correo")
        
        self.madre_profesion_label = CTkLabel(
            self.frame_madre,
            text="Profesión u Ocupación:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.madre_profesion_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.madre_profesion_entry = CTkEntry(
            self.frame_madre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.madre_profesion_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.madre_direccion_label = CTkLabel(
            self.frame_madre,
            text="Dirección:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.madre_direccion_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.madre_direccion_entry = CTkEntry(
            self.frame_madre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",
            validatecommand=(validacion_direccion, "%P"),
        )
        self.madre_direccion_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # --- Información del Padre ---
        self.info_padre_label = CTkLabel(
            self.content_frame,
            text="Información del Padre",
            font=("Arial", 18, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.info_padre_label.pack(padx=10, pady=(10, 5), anchor="w")

        # Frame para los campos del padre
        self.frame_padre = tk.Frame(self.content_frame, background="white")
        self.frame_padre.pack(padx=10, pady=(5, 10), fill=tk.BOTH, expand=True)

        # Etiquetas y Entrys para el Padre
        self.padre_nombre_label = CTkLabel(
            self.frame_padre,
            text="Nombre Completo:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.padre_nombre_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.padre_nombre_entry = CTkEntry(
            self.frame_padre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_nombre, "%P"),
        )
        self.padre_nombre_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.padre_telefono_label = CTkLabel(
            self.frame_padre,
            text="Teléfono:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.padre_telefono_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.padre_telefono_entry = CTkEntry(
            self.frame_padre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_telefono, "%P"),
        )
        self.padre_telefono_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.padre_correo_label = CTkLabel(
            self.frame_padre,
            text="Correo Electrónico:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.padre_correo_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.padre_correo_entry = CTkEntry(
            self.frame_padre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.padre_correo_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        asociar_validacion(self.padre_correo_entry, tipo="correo")
        
        self.padre_profesion_label = CTkLabel(
            self.frame_padre,
            text="Profesión u Ocupación:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,

        )
        self.padre_profesion_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.padre_profesion_entry = CTkEntry(
            self.frame_padre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
        )
        self.padre_profesion_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.padre_direccion_label = CTkLabel(
            self.frame_padre,
            text="Dirección:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.padre_direccion_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.padre_direccion_entry = CTkEntry(
            self.frame_padre,
            font=("Arial", 12),
            width=250,
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            validate="key",
            validatecommand=(validacion_direccion, "%P"),
        )
        self.padre_direccion_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<< SECCIÓN ACUDIENTE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Sección de Información del Acudiente
        self.info_acudiente_label = CTkLabel(
            self.content_frame,
            text="Información del Acudiente",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.info_acudiente_label.pack(
            padx=10, pady=(10, 5), fill=tk.BOTH, expand=True, anchor="w"
        )

        # Frame para los datos del acudiente
        self.frame_acudiente = tk.Frame(self.content_frame, background="white")
        self.frame_acudiente.pack(padx=10, pady=(5, 5), fill=tk.BOTH, expand=True)

        # Relación con el niño
        self.relacion_label = CTkLabel(
            self.frame_acudiente,
            text="Relación con el niño:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.relacion_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Variable para almacenar la selección de la relación
        self.relacion_var = StringVar(value="")  # Predeterminado a "madre"

        # Checkbuttons para "madre", "padre", "otro"
        self.check_madre = CTkRadioButton(
            self.frame_acudiente,
            text="Madre",
            variable=self.relacion_var,
            value="madre",
            font=(
                "Arial",
                14,
            ),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_madre.grid(row=0, column=1, padx=(10, 2), pady=10, sticky="w")

        self.check_padre = CTkRadioButton(
            self.frame_acudiente,
            text="Padre",
            variable=self.relacion_var,
            value="padre",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_padre.grid(row=0, column=2, padx=(10, 2), pady=10, sticky="w")

        self.check_otro = CTkRadioButton(
            self.frame_acudiente,
            text="Otro",
            variable=self.relacion_var,
            value="otro",
            font=("Arial", 14),
            text_color=COLOR_FONT_BLACK,
            hover_color=COLOR_MENU_CURSOR_ENCIMA,
            fg_color=COLOR_FONT_PURPLE,
            border_color=COLOR_FONT_BLACK,
            corner_radius=10,
        )
        self.check_otro.grid(row=0, column=3, padx=(10, 2), pady=10, sticky="w")

        # Entrys para la información del acudiente
        self.nombre_acudiente_label = CTkLabel(
            self.frame_acudiente,
            text="Nombre Completo:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.nombre_acudiente_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.nombre_acudiente_entry = CTkEntry(
            self.frame_acudiente,
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            state="disabled",
            width=250,
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_nombre, "%P"),
        )  # Inicializado en deshabilitado
        self.nombre_acudiente_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.telefono_acudiente_label = CTkLabel(
            self.frame_acudiente,
            text="Teléfono:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.telefono_acudiente_label.grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        self.telefono_acudiente_entry = CTkEntry(
            self.frame_acudiente,
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            state="disabled",
            width=250,
            validate="key",  # Activar validación al escribir
            validatecommand=(validacion_telefono, "%P"),
        )  # Inicializado en deshabilitado
        self.telefono_acudiente_entry.grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )

        self.correo_acudiente_label = CTkLabel(
            self.frame_acudiente,
            text="Correo Electrónico:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.correo_acudiente_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.correo_acudiente_entry = CTkEntry(
            self.frame_acudiente,
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            state="disabled",
            width=250,
        )  # Inicializado en deshabilitado
        self.correo_acudiente_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        asociar_validacion(self.correo_acudiente_entry, tipo="correo")
        
        self.direccion_acudiente_label = CTkLabel(
            self.frame_acudiente,
            text="Dirección:",
            font=("Arial", 14, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.direccion_acudiente_label.grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )
        self.direccion_acudiente_entry = CTkEntry(
            self.frame_acudiente,
            font=("Arial", 12),
            text_color=COLOR_FONT_BLACK,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            state="disabled",
            width=250,
            validate="key",
            validatecommand=(validacion_direccion, "%P"),
        )  # Inicializado en deshabilitado
        self.direccion_acudiente_entry.grid(
            row=4, column=1, padx=10, pady=10, sticky="w"
        )

        # Función para habilitar los campos de texto de acuerdo con la relación seleccionada
        def actualizar_campos_acudiente():
            if self.relacion_var.get() == "madre":
                # Si la relación es madre, deshabilitamos los campos de entrada
                self.nombre_acudiente_entry.configure(state="disabled")
                self.telefono_acudiente_entry.configure(state="disabled")
                self.correo_acudiente_entry.configure(state="disabled")
                self.direccion_acudiente_entry.configure(state="disabled")
                # Copiamos los datos de la madre a los campos de entrada si es necesario
                self.nombre_acudiente_entry.delete(0, tk.END)
                self.telefono_acudiente_entry.delete(0, tk.END)
                self.correo_acudiente_entry.delete(0, tk.END)
                self.direccion_acudiente_entry.delete(0, tk.END)
                self.nombre_acudiente_entry.insert(0, self.madre_nombre_entry.get())
                self.telefono_acudiente_entry.insert(0, self.madre_telefono_entry.get())
                self.correo_acudiente_entry.insert(0, self.madre_correo_entry.get())
                self.direccion_acudiente_entry.insert(
                    0, self.madre_direccion_entry.get()
                )

            elif self.relacion_var.get() == "padre":
                # Si la relación es padre, deshabilitamos los campos de entrada
                self.nombre_acudiente_entry.configure(state="disabled")
                self.telefono_acudiente_entry.configure(state="disabled")
                self.correo_acudiente_entry.configure(state="disabled")
                self.direccion_acudiente_entry.configure(state="disabled")
                # Copiamos los datos del padre a los campos de entrada si es necesario
                self.nombre_acudiente_entry.delete(0, tk.END)
                self.telefono_acudiente_entry.delete(0, tk.END)
                self.correo_acudiente_entry.delete(0, tk.END)
                self.direccion_acudiente_entry.delete(0, tk.END)
                self.nombre_acudiente_entry.insert(0, self.padre_nombre_entry.get())
                self.telefono_acudiente_entry.insert(0, self.padre_telefono_entry.get())
                self.correo_acudiente_entry.insert(0, self.padre_correo_entry.get())
                self.direccion_acudiente_entry.insert(
                    0, self.padre_direccion_entry.get()
                )

            elif self.relacion_var.get() == "otro":
                # Si la relación es otro, habilitamos los campos de entrada
                self.nombre_acudiente_entry.configure(state="normal")
                self.telefono_acudiente_entry.configure(state="normal")
                self.correo_acudiente_entry.configure(state="normal")
                self.direccion_acudiente_entry.configure(state="normal")

        # Llamar a la función de actualización al cargar la página
        actualizar_campos_acudiente()

        # Asignar la función a los botones de opción
        self.check_madre.configure(command=actualizar_campos_acudiente)
        self.check_padre.configure(command=actualizar_campos_acudiente)
        self.check_otro.configure(command=actualizar_campos_acudiente)

        # <<<<<<<<<<<<<<<<<<<<<< SUBIR DOCUMENTOS >>>>>>>>>>>>>>>>>>>><
        self.Documentos_label = CTkLabel(
            self.content_frame,
            text="Documentación:",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.Documentos_label.pack(
            padx=10, pady=(10, 5), fill=tk.BOTH, expand=True, anchor="w"
        )

        # Frame para los datos del acudiente
        self.frame_documentos = tk.Frame(self.content_frame, background="white")
        self.frame_documentos.pack(padx=10, pady=(5, 5), fill=tk.BOTH, expand=True)

        # Lista de documentos con sus botones para cargar
        self.documentos = [
            ("Fotocopia del registro civil", self.cargar_registro_civil),
            (
                "Fotocopia de la Tarjeta de Identidad (si es mayor de 7 años)",
                self.cargar_tarjeta_identidad,
            ),
            ("Fotocopia C.C. de Padres y Acudiente", self.cargar_cc_padres_acudiente),
            ("EPS vigente o Fosyga", self.cargar_eps),
            ("Recibo de servicio público reciente", self.cargar_recibo_servicio),
            (
                "Fotocopia del carnet de vacunas (para primaria y preescolar)",
                self.cargar_carnet_vacunas,
            ),
            ("Boletín de aprobado del año anterior", self.cargar_boletin),
            ("Certificado de paz y salvo", self.cargar_paz_y_salvo),
        ]

        # Crear los frames para cada documento
        self.documento_labels = {}
        for documento, funcion in self.documentos:
            # Título para cada documento
            documento_label = CTkLabel(
                self.frame_documentos,
                text=f"{documento}:",
                font=("Arial", 14, "bold"),
                text_color=COLOR_FONT_BLACK,
            )
            documento_label.pack(padx=10, pady=(10, 5), anchor="w")

            # Frame para los botones de cargar documentos
            frame = CTkFrame(self.frame_documentos, fg_color="white")
            frame.pack(padx=10, pady=(5, 10), fill=tk.BOTH, expand=True)

            # Label para mostrar el nombre del archivo
            archivo_label = CTkLabel(
                frame,
                text="No se ha cargado archivo",
                fg_color="#CDCDCD",
                font=("Arial", 12),
                text_color=COLOR_FONT_BLACK,
            )
            archivo_label.pack(side=tk.LEFT, padx=10)
            self.documento_labels[documento] = archivo_label

            # Botón para cargar el archivo
            boton = CTkButton(
                frame,
                text=f"Cargar documento",
                command=lambda doc=documento: funcion(doc),
                font=("JasmineUPC", 16),
                border_color=COLOR_MENU_LATERAL,
                fg_color=COLOR_MENU_LATERAL,
                hover_color=COLOR_MENU_LATERAL,
                corner_radius=12,
                border_width=2,
                height=35,
                width=180,
            )
            boton.pack(side=tk.RIGHT)

        self.buton_Agregar_Nueva_matricula = CTkButton(
            self.content_frame,
            text="Guardar Nueva Matricula",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_BARRA_SUPERIOR,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=35,
            width=180,
        )
        self.buton_Agregar_Nueva_matricula.pack(
            padx=10, pady=(20, 20), fill=tk.BOTH, expand=True, anchor="w"
        )

    # Funcion para cargar foto del estudiante
    def cargar_imagen(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )

        if file_path:
            img = Image.open(file_path).resize((150, 150))
            img = ImageTk.PhotoImage(img)

            self.img_referencia = img
            # Label para mostrar la imagen
            if hasattr(self, "label_imagen"):
                self.label_imagen.config(image=img)
                self.label_imagen.image = img  # Guardar referencia de la imagen
            else:
                self.label_imagen = tk.Label(self.frame_imagen, image=img, bg="white")
                self.label_imagen.image = img  # Guardar referencia de la imagen
                self.label_imagen.pack(pady=10)

    # Función para cargar el documento
    def cargar_documento(self, nombre_documento):
        # Abrir un cuadro de diálogo para seleccionar un archivo
        archivo = filedialog.askopenfilename(
            title=f"Selecciona {nombre_documento}",
            filetypes=[("Todos los archivos", "*.*")],
        )

        if archivo:
            # Actualizar el texto del Label con el nombre del archivo
            self.documento_labels[nombre_documento].configure(
                text=archivo.split("/")[-1],
                fg_color="#a9d39e",
            )
            messagebox.showinfo(
                "Documento Cargado", f"{nombre_documento} cargado exitosamente."
            )
        else:
            messagebox.showwarning(
                "Advertencia",
                f"No se seleccionó ningún archivo para {nombre_documento}.",
            )

    # Funciones para cada tipo de documento
    def cargar_registro_civil(self, documento):
        self.cargar_documento(documento)

    def cargar_tarjeta_identidad(self, documento):
        self.cargar_documento(documento)

    def cargar_cc_padres_acudiente(self, documento):
        self.cargar_documento(documento)

    def cargar_eps(self, documento):
        self.cargar_documento(documento)

    def cargar_recibo_servicio(self, documento):
        self.cargar_documento(documento)

    def cargar_carnet_vacunas(self, documento):
        self.cargar_documento(documento)

    def cargar_boletin(self, documento):
        self.cargar_documento(documento)

    def cargar_paz_y_salvo(self, documento):
        self.cargar_documento(documento)

    # <<<<<<<<<<<<!!!!!!! NO TOCAR !!!!!!!!!!!>>>>>>>
    # Método para redimensionar el canvas
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        # Crear una ventana en el canvas
        window_id = self.canvas.create_window(
            0, 0, window=self.content_frame, anchor="nw"
        )

        # Luego, cuando quieras configurar las propiedades de esa ventana
        self.canvas.itemconfig(window_id, width=canvas_width)
