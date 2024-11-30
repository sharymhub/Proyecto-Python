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
)

tarjeta = [{"nombre": "Juanita Pérez",
        "grado": "segundo",
        "id": "01",
        "tipo_documento" : "C.C",
        "imagen": "./Assets/Prueba 3.jpg",
        "detalle": "Juan es un estudiante destacado en matemáticas.",
        "numero_documento": "123456789",
        "telefono": "+57 3001234567",
        "direccion": "Calle 123 #45-67, Bogotá",
        "correo_electronico": "juanita.perez@example.com",
        "fecha_nacimiento": "1985-06-15",
        "materia_dictada": "Matemáticas",
        "fecha_contratacion": "2010-02-15",}
        ]

class formularioPerfilProfesores:
    def __init__(self, panel_principal):
        self.panel_principal = (
            panel_principal  # Asegúrate de que esté correctamente escrito
        )
        # Crear el contenedor principal con diseño responsivo
        self.cuerpo_seccion = CTkFrame(self.panel_principal, fg_color="white")
        self.cuerpo_seccion.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Botón Editar en la parte superior derecha
        self.boton_editar = CTkButton(
            self.cuerpo_seccion,
            text="Editar",
            width=100,
            command=lambda: self.editar_profesor(tarjeta),
            fg_color=COLOR_FONT_PURPLE,
            text_color="white",
        )
        self.boton_editar.pack(side=tk.TOP, anchor="ne", pady=(10, 0), padx=10)

        # Frame superior para datos personales
        self.Datos_personales = tk.Frame(self.cuerpo_seccion, background="white")
        self.Datos_personales.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
        
        #Frame para boton editar 
        self.frame_editar = tk.Frame(
            self.Datos_personales, bg="white",
        )
        self.frame_editar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        btn_editar_profesor = CTkButton (
            self.frame_editar,
            text="Editar",
            font=("Arial", 14),
            border_color="white",
            fg_color="white",
            bg_color="red",
            command=lambda: self.editar_profesor(tarjeta),
        )
        
        # Frame de Imagen
        self.frame_imagen = tk.Frame(
            self.Datos_personales, bg="white", width=400, height=400
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Cargar la imagen desde la ruta del diccionario
        try:
            img = Image.open(tarjeta[0]["imagen"]).resize((150, 150))
            img_tk = ImageTk.PhotoImage(img)
            imagen_label = tk.Label(self.frame_imagen, image=img_tk, background="white")
            imagen_label.image = img_tk
            imagen_label.pack(pady=5)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # Frame para información del texto
        self.texto_frame = CTkFrame(self.Datos_personales, fg_color="white")
        self.texto_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, expand=True)

        self.agregar_label(self.texto_frame, "Nombre:", tarjeta[0]["nombre"])
        self.agregar_label(self.texto_frame, "Tipo de documento:", tarjeta[0]["tipo_documento"])
        self.agregar_label(
            self.texto_frame, "Número de documento:", tarjeta[0]["numero_documento"]
        )
        self.agregar_label(self.texto_frame, "Teléfono:", tarjeta[0]["telefono"])
        self.agregar_label(self.texto_frame, "Dirección:", tarjeta[0]["direccion"])
        self.agregar_label(self.texto_frame, "Correo:", tarjeta[0]["correo_electronico"])
        self.agregar_label(
            self.texto_frame, "Fecha de nacimiento:", tarjeta[0]["fecha_nacimiento"]
        )

        # Información académica
        self.Datos_academicos = tk.Frame(self.cuerpo_seccion, background="white")
        self.Datos_academicos.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.label_informacion_academica = CTkLabel(
            self.Datos_academicos,
            font=("Arial", 24),
            text="Información Académica:",
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_informacion_academica.pack(anchor="w", pady=5)

        self.agregar_label(self.Datos_academicos, "Grado a cargo:", tarjeta[0]["grado"])
        self.agregar_label(
            self.Datos_academicos, "Materia asignada:", tarjeta[0]["materia_dictada"]
        )
        self.agregar_label(
            self.Datos_academicos, "Inicio de contrato:", tarjeta[0]["fecha_contratacion"]
        )

        # Documentos
        self.documentos = tk.Frame(self.cuerpo_seccion, background="White")
        self.documentos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.label_Documentos = CTkLabel(
            self.documentos,
            font=("Arial", 24),
            text="Documentos:",
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_Documentos.grid(row=0, column=0, columnspan=2, sticky="w")

        self.agregar_boton_documento(self.documentos, "Documento de identidad", 1)
        self.agregar_boton_documento(self.documentos, "Diploma", 2)
        self.agregar_boton_documento(self.documentos, "Especialización", 3)

        # Botón Eliminar en la esquina inferior derecha
        self.btn_eliminar_profesor = CTkButton(
            self.documentos,
            text="Eliminar Profesor",
            command=self.eliminar_profesor,
            width=120,
            height=30,
            fg_color="#CA4A4A",
            text_color="white",
        )
        self.btn_eliminar_profesor.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def agregar_label(self, frame, label_text, value_text):
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

    def agregar_boton_documento(self, frame, label_text, row):
        """Agrega un botón para cargar documentos en una fila."""
        label = CTkLabel(
            frame,
            font=("Arial", 16, "bold"),
            text=label_text,
            text_color=COLOR_FONT_BLACK,
        )
        label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
        boton = CTkButton(
            frame,
            text="Cargar documento",
            command=self.Cargar_documento,
            fg_color=COLOR_FONT_PURPLE,
            text_color="white",
        )
        boton.grid(row=row, column=1, padx=(50, 10), pady=2)

    def editar_profesor(self, tarjeta):
        # Limpiar la ventana y mostrar detalles
        for widget in self.panel_principal.winfo_children():
            widget.destroy()
            
        # Contenedor para el formulario de edición
        self.formulario = CTkFrame(self.panel_principal, fg_color="white")
        self.formulario.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

         # Crear un frame para los datos personales
        self.Datos_personales = tk.Frame(self.formulario, background="white")
        self.Datos_personales.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
        
        # Frame de Imagen
        self.frame_imagen = tk.Frame(
            self.Datos_personales, bg="white", width=100, height=100
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón para cargar imagen
        btn_cargar_imagen = CTkButton(
            self.frame_imagen, text="Cargar Foto", command=self.cargar_imagen
        )
        btn_cargar_imagen.pack(pady=5)
        # Frame con informacion academica
        self.Datos_academicos = tk.Frame(self.formulario, background="white")
        self.Datos_academicos.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Frame de documentación
        self.documentos = tk.Frame(self.formulario, background="White")
        self.documentos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # //////////// Secion Datos Personales //////////////
        # Crear un frame dentro del frame para dividir imagen y texto
        self.contenido_frame = CTkFrame(self.Datos_personales, fg_color="white")
        self.contenido_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el frame para el texto
        self.texto_frame = CTkFrame(self.contenido_frame, fg_color="white")
        self.texto_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Nombre de profesor
        self.nombre_label = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Nombre:",
            text_color=COLOR_FONT_BLACK,
        )
        self.nombre_label.grid(
            column=0,
            row=0,
            sticky="w",
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
            column=1,
            row=0,
            padx=10,
            pady=2,
            sticky="ew",
        )
        self.entry_nombre.insert(0, tarjeta[0]["nombre"])

        # Tipo de documento
        self.label_tipo_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Tipo de documento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_tipo_documento.grid(
            column=0,
            row=1,
            sticky="w",
        )
        self.option_tipo_documento = CTkOptionMenu(
            self.texto_frame,
            values=["C.C", "C.E"],
            width=30,
            fg_color="#cdcdcd",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.option_tipo_documento.grid(
            column=1,
            row=1,
            sticky="ew",
        )
        self.option_tipo_documento.set(tarjeta[0]["tipo_documento"])

        # Numero de documento
        self.Numero_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Numero de documento",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_documento.grid(
            column=0,
            row=2,
            sticky="w",
        )

        self.entry_numero_documento = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_numero_documento.grid(
            column=1,
            row=2,
            padx=10,
            pady=2,
            sticky="ew",
        )
        self.entry_numero_documento.insert(0, tarjeta[0]["numero_documento"])
        
        # Numero de telefono
        self.Numero_Telefono = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Numero de Telefono:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_Telefono.grid(
            column=0,
            row=3,
            sticky="w",
        )
        
        
        self.entry_numero_telefono = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_numero_telefono.grid(column=1, row=3, padx=10, pady=2, sticky="ew")
        self.entry_numero_telefono.insert(0, tarjeta[0]["telefono"])
        
        # Direccion
        self.Direccion = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Dirección:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Direccion.grid(
            column=0,
            row=4,
            sticky="w",
        )

        self.entry_direccion = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_direccion.grid(
            column=1,
            row=4,
            padx=10,
            pady=2,
            sticky="ew",
        )
        self.entry_direccion.insert(0, tarjeta[0]["direccion"])
        
        # correo electronico
        self.CorreoElectronico = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Correo electronico:",
            text_color=COLOR_FONT_BLACK,
        )
        self.CorreoElectronico.grid(
            column=0,
            row=5,
            sticky="w",
        )

        self.entry_Correo_electronico = CTkEntry(
            self.texto_frame,
            width=250,
            border_color=COLOR_FONT_PURPLE,
            fg_color="white",
            text_color=COLOR_FONT_BLACK,
            font=("Arial", 14),
        )
        self.entry_Correo_electronico.grid(
            column=1,
            row=5,
            padx=5,
            pady=2,
            sticky="ew",
        )
        self.entry_Correo_electronico.insert(0, tarjeta[0]["correo_electronico"])
        
        # Fecha de nacimiento
        self.Numero_documento = CTkLabel(
            self.texto_frame,
            font=("Arial", 16, "bold"),
            text="Fecha de nacimiento:",
            text_color=COLOR_FONT_BLACK,
        )
        self.Numero_documento.grid(column=0, row=6, sticky="w")

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
        cal.grid(row=6, column=1, padx=5, pady=10, sticky="ew")
        cal.set_date(tarjeta[0]["fecha_nacimiento"])
        
        self.label_informacion_academica = CTkLabel(
            self.Datos_academicos,
            font=("Arial", 26, "bold"),
            text="Información Académica:",
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_informacion_academica.grid(row=0, column=0)

        self.Frame_datosAcademicos = tk.Frame(self.Datos_academicos, background="#cdcdcd")
        self.Frame_datosAcademicos.grid(row=1, column=0, padx=10, pady=5)

        # Grado a cargo
        self.label_grado_cargo = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 16, "bold"),
            text="Grado a cargo:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_grado_cargo.grid(
            column=0,
            row=0,
            padx=10,
            pady=2,
            sticky="w",
        )

        self.option_Grado_a_cargo = CTkOptionMenu(
            self.Frame_datosAcademicos,
            values=["Primero", "Segundo", "Tercero", "Cuarto", "Quinto"],
            width=200,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.option_Grado_a_cargo.grid(
            column=0,
            row=1,
            padx=10,
            pady=2,
            sticky="ew",
        )
        self.option_Grado_a_cargo.set(tarjeta[0]["grado"])


        # Materias dictadas
        self.label_Materias_dictadas = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 16, "bold"),
            text="Materia a cargo:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Materias_dictadas.grid(
            column=1,
            row=0,
            padx=10,
            pady=2,
            sticky="w",
        )
        

        self.option_Materias_dictadas = CTkOptionMenu(
            self.Frame_datosAcademicos,
            values=["Matematicas", "Ingles", "Español"],
            width=200,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_FONT_PURPLE,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONT_PURPLE,
            text_color=COLOR_FONT_BLACK,
            dropdown_text_color=COLOR_FONT_BLACK,
        )
        self.option_Materias_dictadas.grid(
            column=1,
            row=1,
            padx=10,
            pady=2,
            sticky="ew",
        )
        self.option_Materias_dictadas.set(tarjeta[0]["materia_dictada"])
        
        # Contratado desde
        self.label_fecha_contratacion = CTkLabel(
            self.Frame_datosAcademicos,
            font=("Arial", 16, "bold"),
            text="Contratado desde:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_fecha_contratacion.grid(
            column=2,
            row=0,
            padx=10,
            pady=2,
            sticky="w",
        )

        cal_fecha_contratacion = DateEntry(
            self.Frame_datosAcademicos,
            width=18,
            background=COLOR_FONT_WHITE,
            foreground=COLOR_FONT_BLACK,
            borderwidth=0,
            date_pattern="y-mm-dd",
            selectforeground=COLOR_FONT_WHITE,
            selectbackground=COLOR_FONT_PURPLE,
            font=("Arial", 10),
        )
        cal_fecha_contratacion.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        cal_fecha_contratacion.set_date(tarjeta[0]["fecha_contratacion"])

        # //////////// Secion Documentos //////////////

        self.label_Documentos = CTkLabel(
            self.documentos,
            font=("Arial", 26, "bold"),
            text="Documentos:",
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_Documentos.grid(row=0, column=0)

        # CARGA DE DOCUMENTO DE IDENTIDAD
        self.label_Documento_identidad = CTkLabel(
            self.documentos,
            font=("Arial", 16, "bold"),
            text="Documento de identidad",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_Documento_identidad.grid(
            column=0,
            row=1,
            padx=10,
            pady=2,
            sticky="w",
        )

        btn_cargar_documento_identidad = CTkButton(
            self.documentos, text="Cargar documento", command=self.Cargar_documento
        )
        btn_cargar_documento_identidad.grid(
            column=1, row=1, pady=5, padx=(100, 10), sticky="E"
        )

        # CARGA DE DIPLOMA
        self.label_DIPLOMA = CTkLabel(
            self.documentos,
            font=("Arial", 16, "bold"),
            text="Diploma",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_DIPLOMA.grid(
            column=0,
            row=2,
            padx=10,
            pady=2,
            sticky="w",
        )

        btn_cargar_diploma = CTkButton(
            self.documentos, text="Cargar documento", command=self.Cargar_documento
        )
        btn_cargar_diploma.grid(column=1, row=2, pady=5, padx=(100, 10), sticky="E")

        # CARGA DE ESPECIALIZACION
        self.label_especializacion = CTkLabel(
            self.documentos,
            font=("Arial", 16, "bold"),
            text="Documento de identidad",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_especializacion.grid(
            column=0,
            row=3,
            padx=10,
            pady=2,
            sticky="w",
        )

        btn_cargar_especializacion = CTkButton(
            self.documentos, text="Cargar documento", command=self.Cargar_documento
        )
        btn_cargar_especializacion.grid(
            column=1, row=3, pady=5, padx=(100, 10), sticky="E"
        )
        # Botón para guardar cambios
        self.boton_guardar = CTkButton(self.documentos, text="Guardar cambios", command=lambda: self.guardar_cambios(tarjeta), fg_color=COLOR_FONT_PURPLE, text_color="white")
        self.boton_guardar.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        # Botón para cancelar la edición
        self.boton_cancelar = CTkButton(self.documentos, text="Cancelar", command=self.panel_pricipal.destroy, fg_color="gray", text_color="white")
        self.boton_cancelar.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-50)

    def guardar_cambios(self, tarjeta):
        # Aquí puedes guardar los nuevos valores editados
        tarjeta["nombre"] = self.nombre_entry.get()
        tarjeta["telefono"] = self.telefono_entry.get()
        tarjeta["direccion"] = self.direccion_entry.get()
        tarjeta["correo_electronico"] = self.correo_entry.get()
        
        # Limpiar el panel principal para mostrar la vista detallada con los nuevos datos
        for widget in self.panel_pricipal.winfo_children():
            widget.destroy()  # Elimina todos los widgets del panel actual

        # Llamar a la función que muestra los detalles de la tarjeta, con los datos actualizados
        self.ventana_detalles(tarjeta)  # Vuelve a mostrar la vista detallada


        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Guardado", "Los cambios se han guardado correctamente.")

    def eliminar_profesor(self):
        messagebox.showwarning("Eliminar", "¿Estás seguro de eliminar este profesor?")

    def Cargar_documento(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar documento",
            filetypes=[
                ("Archivos PDF", "*.pdf"),
                ("Archivos de Texto", "*.txt"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if archivo:
            messagebox.showinfo(
                "Archivo seleccionado", f"Has cargado el archivo:\n{archivo}"
            )
        else:
            messagebox.showerror("Error", "No has seleccionado un archivo.")
    
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
