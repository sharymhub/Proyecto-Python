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

estudiante = {
    "Datos personales" :{
        "nombre": "Juan Pérez",
        "edad": 16,
        "fecha_nacimiento": "2008-03-15",
        "sexo": "Masculino",
        "direccion": "Calle Ficticia 123, Ciudad X",
        "telefono": "123-456-7890",
        "correo": "juan.perez@email.com",
        "imagen": "Assets/prueba1.jpg"
    },
    "padre": {
        "nombre": "Carlos Pérez",
        "edad": 42,
        "ocupacion": "Ingeniero",
        "telefono": "987-654-3210",
        "correo": "carlos.perez@email.com",
        "direccion": "Calle Ficticia 123, Ciudad X"
    },
    "madre": {
        "nombre": "Ana Martínez",
        "edad": 40,
        "ocupacion": "Docente",
        "telefono": "876-543-2109",
        "correo": "ana.martinez@email.com",
        "direccion": "Calle Ficticia 123, Ciudad X"
    },
    "informacion_medica": {
        "tipo_sangre": "O+",
        "alergias": ["Polen", "Cacahuates"],
        "enfermedades": ["Asma", "Rinitis alérgica"],
        "medicamentos": ["Inhalador salbutamol", "Antihistamínicos"],
        "discapacidad_fisica": "No",
        "discapacidad_mental": "No"
        
    },
    "acudiente": {
        "nombre": "María González",
        "relacion": "Tía materna",
        "telefono": "555-123-4567",
        "correo": "maria.gonzalez@email.com",
        "direccion": "Calle Ficticia 456, Ciudad X"
    },
    "documentos": {
        "cedula": "ruta/a/documentos/cedula_juan_perez.pdf",
        "certificado_nacimiento": "ruta/a/documentos/certificado_nacimiento_juan_perez.pdf",
        "boletines": "ruta/a/documentos/boletines_juan_perez.pdf",
        "historia_clinica": "ruta/a/documentos/historia_clinica_juan_perez.pdf"
    }
}


class FormEstudiantesVistaProfesor:
    
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

        
        self.cuerpo_estudiantes = tk.Frame(self.panel_principal, background="white")
        self.cuerpo_estudiantes.pack(side=tk.TOP, fill=tk.X, expand=False)
       
        # Boton ver más +
        self.btn_ver_mas = CTkButton(
            self.cuerpo_estudiantes,
            text="Ver más +",
            fg_color="#65558F",  # Color del botón
            text_color="white",
            hover_color="#B3A6D6",# Color al pasar el mouse
            command=lambda: self.vista_detallada(estudiante),
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

    def vista_detallada(self, estudiante):
        print("Mostrando vista detallada.")
        # Limpiar el panel principal para mostrar la vista detallada con los nuevos datos
        for widget in self.panel_principal.winfo_children():
            widget.destroy()  # Elimina todos los widgets del panel actual
            
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
        
        # Barra superior
        self.barra_superior = tk.Frame(self.content_frame, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        

        # Título
        self.lbl_title = CTkLabel(
            self.barra_superior,
            text="Vista detallada",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.lbl_title.grid(row=0, column=0, padx=20, pady=10)

        # Grado al que pertenece
        self.lbl_grade_select = CTkLabel(
            self.barra_superior,
            text="Grado al que está matriculado:",
            font=("Arial", 16, "bold"),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_grade_select.grid(row=1, column=0, sticky="w", padx=15)
        
        self.lbl_grade = CTkLabel(
            self.barra_superior,
            text="XXX",
            font=("Arial", 16),
            text_color=COLOR_FONT_BLACK,
        )
        self.lbl_grade.grid(row=2, column=0, padx=10, pady=5)

        # Fecha de inicio del año
        self.label_Inicio_Año = CTkLabel(
            self.barra_superior,
            font=("Arial", 16, "bold"),
            text="Fecha de Inicio del año:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Inicio_Año.grid(
            column=2,
            row=1,
            padx=15,
            pady=2,
            sticky="w",
        )

        cal_Inicio_año = CTkLabel(
            self.barra_superior,
            font=("Arial", 16),
            text="XXX",
            text_color=COLOR_FONT_BLACK,
        ) 
        cal_Inicio_año.grid(row=2, column=2, padx=15, pady=10, sticky="w")

        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCION DATOS PERSONALES DEL ESTUDIANTE>>>>>>>>>>>>>>><<<<
        # Datos personales del estudiante
        self.Datos_personales = tk.Frame(self.content_frame, background="white")
        self.Datos_personales.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

        # Frame de Imagen
        self.frame_imagen = tk.Frame(
            self.Datos_personales, bg="white", width=100, height=100
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Verifica si la ruta de la imagen existe y carga la imagen
        try:
            imagen_estudiante = Image.open(estudiante["Datos personales"]["imagen"])
            imagen_estudiante.thumbnail((100, 100))  # Ajusta el tamaño de la imagen
            img = ImageTk.PhotoImage(imagen_estudiante)
            imagen_label = CTkLabel(self.frame_imagen, image=img, text="")
            imagen_label.image = img  # Guardar una referencia de la imagen
            imagen_label.pack()
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            imagen_label = CTkLabel(self.frame_imagen, text="Imagen no disponible")
            imagen_label.pack()
        
        # Frame para información del texto
        self.texto_frame = CTkFrame(self.Datos_personales, fg_color="white")
        self.texto_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, expand=True)

        # Agregar etiquetas con los datos personales del estudiante
        self.agregar_label(self.texto_frame, "Nombre:", estudiante["Datos personales"]["nombre"], 0)
        self.agregar_label(self.texto_frame, "Edad:", estudiante["Datos personales"]["edad"], 1)
        self.agregar_label(self.texto_frame, "Fecha de nacimiento:", estudiante["Datos personales"]["fecha_nacimiento"], 2)
        self.agregar_label(self.texto_frame, "Sexo:", estudiante["Datos personales"]["sexo"], 3)
        self.agregar_label(self.texto_frame, "Dirección:", estudiante["Datos personales"]["direccion"], 4)
        self.agregar_label(self.texto_frame, "Teléfono:", estudiante["Datos personales"]["telefono"], 5)
        self.agregar_label(self.texto_frame, "Correo:", estudiante["Datos personales"]["correo"], 6)
        
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
        
        self.frame_derecha = tk.Frame(self.Datos_medicos, background="white")
        self.frame_derecha.grid(padx=5, pady=(5, 5), sticky="e", row=1, column=1)
        
        self.agregar_label(self.frame_izquierda, "Alergias:", estudiante["informacion_medica"]["alergias"], 1)
        self.agregar_label(self.frame_izquierda, "Enfermedades Crónicas:", estudiante["informacion_medica"]["enfermedades"], 2)
        self.agregar_label(self.frame_izquierda, "Medicamentos:", estudiante["informacion_medica"]["medicamentos"], 3)
        self.agregar_label(self.frame_derecha, "Discapacidad Mental:", estudiante["informacion_medica"]["discapacidad_mental"], 1)
        self.agregar_label(self.frame_derecha, "Discapacidad Fisica:", estudiante["informacion_medica"]["discapacidad_fisica"],2)
        self.agregar_label(self.frame_derecha, "Tipo de sangre:", estudiante["informacion_medica"]["tipo_sangre"], 3)
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<< SECCIÓN ACUDIENTE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Frame para los datos del acudiente
        self.frame_acudiente = tk.Frame(self.content_frame, background="white")
        self.frame_acudiente.pack(padx=10, pady=(5, 5), fill=tk.BOTH, expand=True)
        
        self.info_acudiente_label = CTkLabel(
            self.frame_acudiente,
            text="Información del Acudiente",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.info_acudiente_label.pack(padx=5, pady=5)
        
        self.agregar_label(self.frame_acudiente, "Nombre:", estudiante["acudiente"]["nombre"], 0)
        self.agregar_label(self.frame_acudiente, "Relación con el menor:", estudiante["acudiente"]["relacion"], 1)
        self.agregar_label(self.frame_acudiente, "Telefono:", estudiante["acudiente"]["telefono"], 2)
        self.agregar_label(self.frame_acudiente, "Correo:", estudiante["acudiente"]["correo"], 3)
        self.agregar_label(self.frame_acudiente, "Dirección:", estudiante["acudiente"]["direccion"], 4)
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCIÓN DE COMENTARIOS >>>>>>>>>>>>>>>>>>>>>>>>>>
        self.frame_comentarios = tk.Frame(self.content_frame, background="white")
        self.frame_comentarios.pack(padx=10, pady=(10, 10), fill=tk.BOTH, expand=True)

        # Título
        self.label_comentarios = CTkLabel(
            self.frame_comentarios,
            text="Comentarios",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_comentarios.pack(pady=(0, 10))

        # Entrada de texto para comentarios
        self.entry_comentario = CTkEntry(
            self.frame_comentarios,
            placeholder_text="Escribe tu comentario aquí...",
            width=600,
            height=60,
            font=("Arial", 14),
            fg_color="#f0f0f0",
            text_color=COLOR_FONT_BLACK,
        )
        self.entry_comentario.pack(pady=(0, 10))

        # Botón para guardar comentario
        self.btn_guardar_comentario = CTkButton(
            self.frame_comentarios,
            text="Guardar Comentario",
            fg_color=COLOR_FONT_PURPLE,
            text_color="white",
            hover_color="#B3A6D6",
            command=self.guardar_comentario,
            font=("Arial", 12),
        )
        self.btn_guardar_comentario.pack(pady=(0, 10))

        # Frame para mostrar comentarios guardados
        self.frame_lista_comentarios = tk.Frame(self.frame_comentarios, background="white")
        self.frame_lista_comentarios.pack(fill=tk.BOTH, expand=True)

    # Método para guardar comentarios
    def guardar_comentario(self):
        comentario = self.entry_comentario.get().strip()
        if comentario:
            from datetime import datetime
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Contenedor individual para el comentario
            comentario_frame = CTkFrame(
                self.frame_lista_comentarios,
                fg_color="#f0f0f0",
                corner_radius=10,
                border_color="#cccccc",
                border_width=1
            )
            comentario_frame.pack(pady=5, padx=10, fill=tk.X)

            # Mostrar fecha y hora
            label_fecha = CTkLabel(
                comentario_frame,
                text=f"{fecha_hora}",
                font=("Arial", 10, "italic"),
                text_color="#777"
            )
            label_fecha.pack(anchor="w", pady=(5, 0), padx=10)

            # Mostrar el texto del comentario
            label_texto = CTkLabel(
                comentario_frame,
                text=comentario,
                font=("Arial", 12),
                text_color="#333",
                wraplength=350,
                anchor="w",
                justify="left"
            )
            label_texto.pack(anchor="w", pady=(0, 10), padx=10)
            # Botón para eliminar el comentario
            btn_eliminar = CTkButton(
                comentario_frame,
                text="Eliminar",
                fg_color="#FF4D4D",
                text_color="white",
                hover_color="#FF9999",
                command=lambda: self.eliminar_comentario(comentario_frame),
                font=("Arial", 10)
            )
            btn_eliminar.pack(anchor="e", padx=10, pady=(0, 10))

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comentario Guardado", "El comentario ha sido guardado exitosamente.")
            # Limpiar el Entry después de guardar el comentario
            self.entry_comentario.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El comentario no puede estar vacío.")
            
    # Método para confirmar y eliminar un comentario
    def eliminar_comentario(self, comentario_frame):
        respuesta = messagebox.askquestion(
            "Confirmar Eliminación",
            "¿Estás seguro de que deseas eliminar este comentario?"
        )
        if respuesta == "yes":
            comentario_frame.destroy()
            messagebox.showinfo("Comentario Eliminado", "El comentario ha sido eliminado.")

        
            
    def agregar_label(self, frame, label_text, value_text, row):
        """Agrega una fila con un texto y su valor en el layout utilizando pack."""
        # Contenedor horizontal para el texto y valor
        fila = tk.Frame(frame, bg="white")
        fila.pack(fill=tk.X, padx=5, pady=2)

        # Etiqueta del texto
        label = CTkLabel(
            fila,
            font=("Arial", 16, "bold"),
            text=label_text,
            text_color=COLOR_FONT_BLACK,
        )
        label.pack(side=tk.LEFT, padx=5)

        # Etiqueta del valor
        value = CTkLabel(
            fila, font=("Arial", 16), text=value_text, text_color=COLOR_FONT_BLACK
        )
        value.pack(side=tk.LEFT, padx=5)

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
        
    def editar (self, estudiante):
        #editar estudiante
        # Limpiar el panel principal para mostrar la vista detallada con los nuevos datos
        for widget in self.panel_principal.winfo_children():
            widget.destroy()  # Elimina todos los widgets del panel actual
        
        
