import tkinter as tk
from util.util_imagenes import leer_imagen
from tkcalendar import DateEntry
from tkinter import filedialog
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
)

# Datos de ejemplo para las tarjetas
datos_tarjetas = [
    {
        "nombre": "Juanita Pérez",
        "grado": "Directora 10º A",
        "id": "01",
        "imagen": "./Assets/Prueba 3.jpg",
        "detalle": "Juan es un estudiante destacado en matemáticas.",
    },
    {
        "nombre": "Ana Gómez",
        "grado": "Directora 11º B",
        "id": "02",
        "imagen": "./Assets/Prueba 3.jpg",
        "detalle": "Ana tiene un excelente rendimiento en ciencias.",
    },
    {
        "nombre": "Carolina López",
        "grado": "Directora 12º C",
        "id": "03",
        "imagen": "./Assets/Prueba 3.jpg",
        "detalle": "Carlos es un líder en actividades extracurriculares.",
    },
]


class FormularioProfesoresDesign:

    def __init__(self, panel_principal):
        # Barra superior
        self.panel_pricipal = panel_principal
        self.barra_superior = tk.Frame(panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

        self.Btn_NuevoProfesor = CTkButton(
            self.barra_superior,
            text="Nuevo Profesor",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            image=icon,
            compound="left",
        )
        self.Btn_NuevoProfesor.image = icon
        self.Btn_NuevoProfesor.pack(side=tk.RIGHT, padx=10, pady=10)

        # Cuerpo de la seccion
        self.cuerpo_seccion = CTkFrame(panel_principal, fg_color="white")
        self.cuerpo_seccion.pack(pady=20, padx=20, fill="both", expand=True)
        self.frame_tarjetas = CTkFrame(self.cuerpo_seccion, fg_color="white")
        self.frame_tarjetas.pack(fill="both", expand=True)

        # Crear las tarjetas
        self.crear_tarjetas()

    def crear_tarjetas(self):
        # enumerate = función que recorre los elementos de una lista y devuelve dos valores en cada iteración
        for i, tarjeta in enumerate(
            datos_tarjetas
        ):  # i = indice de cada interación empezando en 0 y "tarjeta" es el valor de la iteración
            tarjeta_frame = CTkFrame(
                self.frame_tarjetas,
                fg_color="lightgray",
                corner_radius=30,
                height=200,
                width=300,
            )
            tarjeta_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10)

            # Crear un frame dentro de la tarjeta para dividir imagen y texto
            contenido_frame = CTkFrame(tarjeta_frame, fg_color="lightgray")
            contenido_frame.pack(fill=tk.BOTH, expand=True)

            # Crear el frame para el texto (a la izquierda)
            texto_frame = CTkFrame(contenido_frame, fg_color="lightgray")
            texto_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

            # Imagen de la tarjeta
            try:
                self.imagen = leer_imagen(
                    tarjeta["imagen"], (100, 100)
                )  # Ajusta la ruta de la imagen
                imagen_label = tk.Label(
                    contenido_frame, image=self.imagen, background="lightgray"
                )
                imagen_label.pack(side=tk.RIGHT, pady=5, padx=10)
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

            # Nombre de la tarjeta
            nombre_label = CTkLabel(
                texto_frame,
                text=tarjeta["nombre"],
                font=("Arial", 14),
                text_color="black",
            )
            nombre_label.pack(pady=5, padx=10)

            # Grado asignado
            grado_label = CTkLabel(
                texto_frame,
                text=tarjeta["grado"],
                font=("Arial", 12),
                text_color="black",
            )
            grado_label.pack(pady=5, padx=10)

            # ID
            id_label = CTkLabel(
                texto_frame,
                text=tarjeta["id"],
                font=("Arial", 12),
                text_color=COLOR_FONT_BLACK,
            )
            id_label.pack(pady=1, padx=10)

            # Agregar el botón para ver detalles
            boton_detalles = CTkButton(
                texto_frame,
                text="Ver detalles",
                font=("Arial", 12),
                fg_color=COLOR_FONT_PURPLE,
                text_color="white",
                hover_color=COLOR_MENU_LATERAL,
                command=lambda tarjeta=tarjeta: self.mostrar_detalles(
                    tarjeta
                ),  # Llamamos a la función con la tarjeta
            )
            boton_detalles.pack(pady=5)

    def mostrar_detalles(self, tarjeta):
        # Limpiar la ventana y mostrar detalles
        for widget in self.panel_pricipal.winfo_children():
            widget.destroy()

        # Mostrar una nueva ventana con los detalles
        self.ventana_detalles(tarjeta)
        
    def cargar_imagen(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((100, 100))  # Redimensionar la imagen
            img = ImageTk.PhotoImage(img)
            
            # Label para mostrar la imagen
            if hasattr(self.cargar_imagen, 'label_imagen'):
                self.cargar_imagen.label_imagen.config(image=img)
            else:
                self.cargar_imagen.label_imagen = tk.Label(self.frame_imagen, image=img, bg="white")
                self.cargar_imagen.label_imagen.image = img  # Guardar referencia de la imagen
                self.cargar_imagen.label_imagen.pack(pady=10)
            
    def ventana_detalles(self, tarjeta):
        # Re-crear el contenedor principal después de limpiar la pantalla
        self.cuerpo_seccion = CTkFrame(self.panel_pricipal, fg_color="white")
        self.cuerpo_seccion.pack(pady=20, padx=20, fill="both", expand=True)

        # frame superior que contiene datos personales
        self.Datos_personales = tk.Frame(self.cuerpo_seccion, background="Black")
        self.Datos_personales.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
        # Frame de Imagen
        self.frame_imagen = tk.Frame(self.Datos_personales, bg="white", width=100, height=100)
        self.frame_imagen.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para cargar imagen
        btn_cargar_imagen = CTkButton(self.frame_imagen, text="Cargar Foto", command=self.cargar_imagen)
        btn_cargar_imagen.pack(pady=5)
        # Frame con informacion academica
        self.Datos_academicos = tk.Frame(self.cuerpo_seccion, background="white")
        self.Datos_academicos.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Frame de documentación
        self.documentos = tk.Frame(self.cuerpo_seccion, background="Blue")
        self.documentos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # //////////// Secion Datos Personales //////////////
        # Crear un frame dentro del frame para dividir imagen y texto
        self.contenido_frame = CTkFrame(self.Datos_personales, fg_color="white")
        self.contenido_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el frame para el texto
        self.texto_frame = CTkFrame(self.contenido_frame, fg_color="white")
        self.texto_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Nombre de profesor
        self.nombre_label = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Nombre:",
            text_color=COLOR_FONT_BLACK,
        )
        self.nombre_label.grid(column=0, row=0, sticky="w",)

        self.entry_nombre = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_nombre.grid(column=1, row=0, padx=10, pady=2, sticky="w",)

        # Tipo de documento
        self.label_tipo_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Tipo de documento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_tipo_documento.grid(column=0, row=1, sticky="w",)
        self.option_tipo_documento = CTkOptionMenu(
            self.texto_frame,
            values=["C.C", "C.E"],
            width=50,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.option_tipo_documento.grid(column=1, row=1, sticky="w",)
        
        #Numero de documento 
        self.Numero_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Numero de documento",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_documento.grid(column=0, row=2, sticky="w",)

        self.entry_numero_documento = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_numero_documento.grid(column=1, row=2, padx=10, pady=2, sticky="w",)
        
        #Numero de telefono 
        self.Numero_Telefono = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Numero de Telefono:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_Telefono.grid(column=0, row=3, sticky="w",)

        self.entry_numero_telefono = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_numero_telefono.grid(column=1, row=3, padx=10, pady=2, sticky="w")
        
        #Direccion 
        self.Direccion = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Dirección:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Direccion.grid(column=0, row=4, sticky="w",)

        self.entry_direccion = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_direccion.grid(column=1, row=4, padx=10, pady=2, sticky="w",)
        
        # correo electronico 
        self.CorreoElectronico = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Correo electronico",
            text_color=COLOR_FONT_BLACK,
        )
        self.CorreoElectronico.grid(column=0, row=5, sticky="w",)

        self.entry_Correo_electronico = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_Correo_electronico.grid(column=1, row=5, padx=5, pady=2, sticky="w",)
        
        #Fecha de nacimiento 
        self.Numero_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 14),
            text="Fecha de nacimiento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_documento.grid(column=0, row=6, sticky="w")
        
        # Crear y colocar el selector de fecha
        cal = DateEntry(self.texto_frame, width=18, background=COLOR_FONT_WHITE, foreground=COLOR_FONT_BLACK, borderwidth=0, date_pattern='y-mm-dd', selectforeground=COLOR_FONT_WHITE, selectbackground=COLOR_FONT_PURPLE, font=("Arial", 10),)
        cal.grid(row=6, column=1, padx=5, pady=10, sticky="w")

        # Botón para obtener la fecha seleccionada
        # def obtener_fecha():
        #     print("Fecha seleccionada:", cal.get())

        # boton = CTkButton(self.texto_frame, 
        #                   text="Confirmar fecha",font=("Arial", 12), fg_color=COLOR_FONT_PURPLE, text_color="white", hover_color=COLOR_MENU_LATERAL, command=obtener_fecha)
        # boton.grid(row=7, column=0, columnspan=2, pady=10)
        
        # //////////// Secion Datos Academicos //////////////
        
        self.label_informacion_academica = CTkLabel(self.Datos_academicos, font=("Arial", 22), text="Información Académica:",text_color=COLOR_FONT_PURPLE)
        self.label_informacion_academica.grid (row=0 , column=0)
        
        self.Frame_datosAcademicos = tk.Frame(self.Datos_academicos, background="Gray")
        self.Frame_datosAcademicos.grid(row=1 , column=0, padx=10, pady=5)
        
        #Grado a cargo 
        self.label_grado_cargo = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 14),
            text="Grado a cargo:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_grado_cargo.grid(column=0, row=0, padx=10, pady=2, sticky="w",)

        self.entry_grado_cargo= CTkEntry(
            self.Frame_datosAcademicos,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_grado_cargo.grid(column=0, row=1, padx=10, pady=2, sticky="w")
        
        #Materias dictadas
        self.label_Materias_dictadas = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 14),
            text="Tipo de documento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Materias_dictadas.grid(column=1, row=0, padx=10, pady=2, sticky="w",)
        
        self.option_Materias_dictadas = CTkOptionMenu(
            self.Frame_datosAcademicos,
            values=["Matematicas", "Ingles", "Español"],
            width=80,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.option_Materias_dictadas.grid(column=1, row=1,padx=10, pady=2, sticky="w",)



        # Contratado desde
        self.label_fecha_contratacion = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 14),
            text="Grado a cargo:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_fecha_contratacion.grid(column=2, row=0, padx=10, pady=2, sticky="w",)
        
        cal_fecha_contratacion = DateEntry(self.Frame_datosAcademicos, width=18, background=COLOR_FONT_WHITE, foreground=COLOR_FONT_BLACK, borderwidth=0, date_pattern='y-mm-dd', selectforeground=COLOR_FONT_WHITE, selectbackground=COLOR_FONT_PURPLE, font=("Arial", 10),)
        cal_fecha_contratacion.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        
        
        # //////////// Secion Documentos //////////////
        
        self.label_Documentos = CTkLabel(self.documentos, font=("Arial", 22), text="Documentos:",text_color=COLOR_FONT_PURPLE)
        self.label_Documentos.grid (row=0 , column=0)
        
        #CARGA DE DOCUMENTO DE IDENTIDAD
        self.label_Documento_identidad = CTkLabel(
            self.documentos,
            font=("Arial", 14),
            text="Documento de identidad",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Documento_identidad.grid(column=0, row=1, padx=10, pady=2, sticky="w",)
        
        btn_cargar_documento_identidad = CTkButton(self.documentos, text="Cargar documento", command=self.cargar_imagen)
        btn_cargar_documento_identidad.grid(column=1, row=1, pady=5, padx=50, sticky="E")
        
        #CARGA DE DIPLOMA
        self.label_DIPLOMA = CTkLabel(
            self.documentos,
            font=("Arial", 14),
            text="Diploma",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_DIPLOMA.grid(column=0, row=2, padx=10, pady=2, sticky="w",)
        
        btn_cargar_diploma = CTkButton(self.documentos, text="Cargar documento", command=self.cargar_imagen)
        btn_cargar_diploma.grid(column=1, row=2, pady=5, padx=50, sticky="E")
        
        #CARGA DE ESPECIALIZACION
        self.label_especializacion = CTkLabel(
            self.documentos,
            font=("Arial", 14),
            text="Documento de identidad",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_especializacion.grid(column=0, row=3, padx=10, pady=2, sticky="w",)
        
        btn_cargar_especializacion = CTkButton(self.documentos, text="Cargar documento", command=self.cargar_imagen)
        btn_cargar_especializacion.grid(column=1, row=3, pady=5, padx=50, sticky="E")