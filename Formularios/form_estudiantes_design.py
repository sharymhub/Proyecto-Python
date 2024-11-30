import tkinter as tk
from tkinter import ttk
from util.util_imagenes import leer_imagen
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter import messagebox as mb
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

import mysql.connector
from mysql.connector import Error

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
            hover_color="#B3A6D6",# Color al pasar el mouse
            command=lambda: self.vista_detallada(estudiante),
            font=("Arial", 12),
        )
        self.btn_ver_mas.pack(side=tk.RIGHT, padx=10, pady=5)
        
        self.formtabla= tk.LabelFrame(panel_principal, background= 'purple')
        self.formtabla.pack(side=tk.LEFT, padx=10, pady=10)
         # Tabla para mostrar las materias
        self.tabla = ttk.Treeview(self.formtabla, columns=["No_identificacion","Nombre","Grado", "TelefonoAcudiente"], show="headings")
        self.tabla.grid(column=0, row=0, padx=5, pady=5)
        self.tabla.heading("No_identificacion", text="N° Identificación")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Grado", text="Grado")
        self.tabla.heading("TelefonoAcudiente", text="Teléfono Acudiente")
        
     # Cargar los datos desde la base de datos
        self.cargar_estudiantes()
        
    def cargar_estudiantes(self):  
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente
                    FROM estudiantes
                """)
                alumnos = cursor.fetchall()

                if not alumnos:
                    print("No se encontraron estudiantes.")
                else:
                    print("Materias cargadas:", alumnos)

                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                # Insertar los datos en la tabla
                for materia in alumnos:
                    self.tabla.insert('', 'end', values=(materia[0], materia[1])) 

            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al ejecutar consulta: {err}")
            finally:
                conn.close()
    def conectar_mysql(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="giebd"
            )
            return conn
        except mysql.connector.Error as err:
            mb.showerror("Error de conexión", f"Error al conectar con la base de datos: {err}")
            return None
        except Exception as e:
            mb.showerror("Error desconocido", f"Ocurrió un error inesperado: {e}")
            return None
        
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
        self.boton_editar = CTkButton(
            self.barra_superior,
            text="Editar",
            width=100,
            command=lambda: self.editar(estudiante),
            fg_color=COLOR_FONT_PURPLE,
            text_color="white",
        )
        self.boton_editar.place(relx=1.0, x=-20, y=10, anchor="ne")

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

        # Fecha de matrícula e inicio del año
        self.label_fecha_Matricula = CTkLabel(
            self.barra_superior,
            font=("Arial", 16, "bold"),
            text="Fecha de matricula:",
            text_color=COLOR_FONT_BLACK,
        )
        self.label_fecha_Matricula.grid(
            column=1,
            row=1,
            padx=10,
            pady=2,
            sticky="w",
        )

        cal_fecha_Matricula = CTkLabel(
            self.barra_superior,
            font=("Arial", 16),
            text="XXX",
            text_color=COLOR_FONT_BLACK,
        ) 
        cal_fecha_Matricula.grid(row=2, column=1, padx=10, pady=10, sticky="w")

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
            self.Datos_personales, bg="white", width=300, height=300
        )
        self.frame_imagen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Verifica si la ruta de la imagen existe y carga la imagen
        try:
            imagen_estudiante = Image.open(estudiante["Datos personales"]["imagen"])
            imagen_estudiante.resize((300, 300))  # Ajusta el tamaño de la imagen
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
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<< SECCION INFORMACION DE LOS PADRES >>>>>>>>>>>>>>
        self.Datos_Padres = tk.Frame(self.content_frame, background="white")
        self.Datos_Padres.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
        # --- Información de los Padres ---
        self.label_InformacionP = CTkLabel(
            self.Datos_Padres,
            text="Información de los Padres:",
            font=("Arial", 28, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_InformacionP.grid(row=0, column=0, padx=0, pady=5)
        
        # Frame para los campos de la madre
        self.frame_madre = tk.Frame(self.Datos_Padres, background="white")
        self.frame_madre.grid(padx=5, pady=(5, 5), sticky="w", row=1, column=0)
        
        self.agregar_label(self.frame_madre, "Nombre:", estudiante["madre"]["nombre"], 0)
        self.agregar_label(self.frame_madre, "Edad:", estudiante["madre"]["edad"], 1)
        self.agregar_label(self.frame_madre, "Profesión:", estudiante["madre"]["ocupacion"], 2)
        self.agregar_label(self.frame_madre, "Correo:", estudiante["madre"]["correo"], 3)
        self.agregar_label(self.frame_madre, "Telefono:", estudiante["madre"]["telefono"],4)
        self.agregar_label(self.frame_madre, "Dirección:", estudiante["madre"]["direccion"], 5)
        
        # Frame para los campos del padre
        self.frame_padre = tk.Frame(self.Datos_Padres, background="white")
        self.frame_padre.grid(padx=5, pady=(5, 5), sticky="e", row=1, column=1)
        
        self.agregar_label(self.frame_padre, "Nombre:", estudiante["padre"]["nombre"],0)
        self.agregar_label(self.frame_padre, "Edad:", estudiante["padre"]["edad"], 1)
        self.agregar_label(self.frame_padre, "Profesión:", estudiante["padre"]["ocupacion"], 2)
        self.agregar_label(self.frame_padre, "Correo:", estudiante["padre"]["correo"], 3)
        self.agregar_label(self.frame_padre, "Telefono:", estudiante["padre"]["telefono"], 4)
        self.agregar_label(self.frame_padre, "Dirección:", estudiante["padre"]["direccion"], 5)
        
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
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<< DOCUMENTOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Parte inferior: Frame de documentos
        # Parte inferior: Frame de documentos
        self.frame_documentos = tk.Frame(self.content_frame, bg="white")
        self.frame_documentos.pack(padx=10, pady=(5, 5), fill=tk.BOTH, expand=True)

        # Título de la sección de documentos
        self.label_documentos = CTkLabel(
            self.frame_documentos,
            text="Documentos Subidos",
            font=("Arial", 20, "bold"),
            text_color=COLOR_FONT_PURPLE,
        )
        self.label_documentos.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Crear etiquetas y botones de descarga para cada documento
        self.crear_documento_descarga(self.frame_documentos, "Tarjeta de identidad:", estudiante["documentos"]["cedula"], 1)
        self.crear_documento_descarga(self.frame_documentos, "Registro civil:", estudiante["documentos"]["certificado_nacimiento"], 2)
        self.crear_documento_descarga(self.frame_documentos, "Boletines:", estudiante["documentos"]["boletines"], 3)
        self.crear_documento_descarga(self.frame_documentos, "Historia clínica:", estudiante["documentos"]["historia_clinica"], 4)

    # Método que crea la etiqueta y el botón de descarga
    def crear_documento_descarga(self, frame, label_text, documento_path, row):
        """Crea la etiqueta y el botón de descarga para un documento."""
        fila = tk.Frame(frame, bg="white")
        fila.grid(row=row, column=0, sticky="w", padx=5, pady=2)

        # Etiqueta para el nombre del documento
        label = CTkLabel(fila, font=("Arial", 16), text=label_text, text_color=COLOR_FONT_BLACK)
        label.pack(side=tk.LEFT, padx=5)

        # Botón de descarga
        download_button = CTkButton(fila, 
            text="Descargar", 
            command=lambda path=documento_path: self.descargar_documento(path),
            fg_color="#65558F", 
            text_color="white", 
            hover_color="#B3A6D6"
        )
        download_button.pack(side=tk.LEFT, padx=10)

    # Método para descargar el documento
    def descargar_documento(self, path):
        """Método para descargar el archivo del documento."""
        try:
            # Aquí puedes utilizar filedialog para pedir la ubicación donde guardar el archivo
            destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            
            if destino:
                # Aquí deberías copiar o mover el archivo de la ruta original a la ruta destino
                # Usaremos shutil para mover el archivo (asegúrate de importar shutil)
                import shutil
                shutil.copy(path, destino)  # Copia el archivo al destino seleccionado
                mb.showinfo("Éxito", f"Documento descargado en: {destino}")
            else:
                mb.showwarning("Error", "No se seleccionó un destino para guardar el archivo.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo descargar el archivo. Error: {e}")

            
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
        
        #aun esta en proceso la idea es llamar al formulario matriculas y que desde alla se edite y luego vuelva a estudiantes 
        #Hay que hacerlo directamente con la base de datos
        
        
