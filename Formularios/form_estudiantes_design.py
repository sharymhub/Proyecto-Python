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
        
        self.grades = ["Ninguno", "1","2","3","4","5"]
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
        self.filtar_grado.configure(command= lambda _: self.filtrar_por_grado())
        
        # Barra de búsqueda
        self.lbl_search = CTkLabel(
            self.barra_superior,
            text="Buscar por Nombre o N°identificación:",
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
        #self.btn_inhabilitados = CTkButton(
        #    self.barra_superior,
        #    text="Inhabilitados",
        #    command=self.ver_inhabilitados,  # Define este método más abajo
        #    fg_color="#CDCDCD", 
        #    text_color="#65558F",
        #    hover_color= "#B3A6D6"
        #)
        #self.btn_inhabilitados.grid(row=0, column=5, sticky="e", padx=30, pady=5)
        
        self.cuerpo_estudiantes = tk.Frame(self.panel_principal, background="white")
        self.cuerpo_estudiantes.pack(side=tk.TOP, fill=tk.X, expand=False)
       
        # Boton ver más +
        self.btn_ver_mas = CTkButton(
            self.cuerpo_estudiantes,
            text="Ver más +",
            fg_color="#65558F",  # Color del botón
            text_color="white",
            hover_color="#B3A6D6",# Color al pasar el mouse
            command= self.vista_detallada,
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
        
    def filtrar_por_grado(self):
        grado_seleccionado = self.grade_var.get()  # Obtener el grado seleccionado
        conn = self.conectar_mysql()
        
        if conn:
            try:
                cursor = conn.cursor()
                
                if grado_seleccionado == "Ninguno":
                    # Mostrar todos los estudiantes si se selecciona "Ninguno"
                    consulta = """
                        SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente
                        FROM estudiantes
                    """
                    cursor.execute(consulta)
                else:
                    # Filtrar por el grado seleccionado
                    consulta = """
                        SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente
                        FROM estudiantes
                        WHERE Grado = %s
                    """
                    cursor.execute(consulta, (grado_seleccionado,))
                
                estudiantes = cursor.fetchall()
                
                # Limpiar la tabla antes de insertar los datos
                self.tabla.delete(*self.tabla.get_children())

                if not estudiantes:
                    print(f"No se encontraron estudiantes en {grado_seleccionado}.")
                else:
                    # Insertar los datos filtrados en la tabla
                    for estudiante in estudiantes:
                        self.tabla.insert('', 'end', values=(estudiante[0], estudiante[1], estudiante[2], estudiante[3]))
            
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al ejecutar consulta: {err}")
            finally:
                conn.close()
    def cargar_estudiantes(self):  
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente FROM estudiantes")
                alumnos = cursor.fetchall()

                if not alumnos:
                    print("No se encontraron estudiantes.")
                else:
                    print("Estudiantes encontrados:", alumnos)

                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                # Insertar los datos en la tabla
                for materia in alumnos:
                    self.tabla.insert('', 'end', values=(materia[0], materia[1], materia[2], materia[3])) 

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
        termino = self.search_var.get().strip()  # Obtiene el término de búsqueda
        conn = self.conectar_mysql()
        
        if conn:
            try:
                cursor = conn.cursor()
                
                if termino:
                    # Consulta con filtro de búsqueda
                    consulta = """
                        SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente 
                        FROM estudiantes
                        WHERE No_identificacion LIKE %s 
                        OR Nombre LIKE %s
                        OR Grado LIKE %s
                        OR TelefonoAcudiente LIKE %s
                    """
                    cursor.execute(consulta, (f"%{termino}%", f"%{termino}%", f"%{termino}%", f"%{termino}%"))
                else:
                    # Consulta sin filtro
                    consulta = "SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente FROM estudiantes"
                    cursor.execute(consulta)
                
                alumnos = cursor.fetchall()
                
                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                if not alumnos:
                    print("No se encontraron estudiantes.")
                else:
                    # Insertar los datos en la tabla
                    for materia in alumnos:
                        self.tabla.insert('', 'end', values=(materia[0], materia[1], materia[2], materia[3]))

            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al ejecutar consulta: {err}")
            finally:
                conn.close()

         # Método para manejar inhabilitados
   # def ver_inhabilitados(self):
   #     print("Mostrando elementos inhabilitados.")
   #     conn = self.conectar_mysql()
   # 
   #     if conn:
   #         try:
   #             cursor = conn.cursor()
   #             # Consulta basada en otro criterio (ajusta según tu lógica)
   #             consulta = """
   #                 SELECT No_identificacion, Nombre, Grado, TelefonoAcudiente
   #                 FROM estudiantes
   #                 WHERE Grado IS NULL OR Grado = ''
   #             """
   #             cursor.execute(consulta)
   #             inhabilitados = cursor.fetchall()
   #             
   #             # Limpiar la tabla antes de mostrar los datos
   #             self.tabla.delete(*self.tabla.get_children())

   #             if not inhabilitados:
   #                 print("No hay estudiantes inhabilitados.")
   #             else:
   ##                 # Insertar los datos de estudiantes inhabilitados en la tabla
   #                 for estudiante in inhabilitados:
   #                     self.tabla.insert('', 'end', values=(estudiante[0], estudiante[1], estudiante[2], estudiante[3]))#

    #        except mysql.connector.Error as err:
    #            mb.showerror("Error", f"Error al ejecutar consulta: {err}")
    #        finally:
    #            conn.close()
        
        
    
    def vista_detallada(self):
        print("Mostrando vista detallada.")
        #def vista_detallada(self):
        print("Mostrando vista detallada.")
        # Obtener el estudiante seleccionado
         #Abre una nueva ventana con detalles del estudiante seleccionado#
        item_seleccionado = self.tabla.selection()
        if not item_seleccionado:
            mb.showwarning("Advertencia", "Por favor, selecciona un estudiante.")
            return

        datos_estudiante = self.tabla.item(item_seleccionado, "values")
        if not datos_estudiante:
            mb.showerror("Error", "No se pudo obtener la información del estudiante.")
            return

        # Crear una nueva ventana
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Vista Detallada")
        nueva_ventana.geometry("400x300")

        # Etiqueta de título
        tk.Label(nueva_ventana, text="Vista Detallada", font=("Arial", 20, "bold")).pack(pady=10)

        # Mostrar los detalles del estudiante
        detalles = [
            ("N° Identificación", datos_estudiante[0]),
            ("Nombre", datos_estudiante[1]),
            ("Grado", datos_estudiante[2]),
            ("Teléfono Acudiente", datos_estudiante[3]),
        ]

        for etiqueta, valor in detalles:
            frame = tk.Frame(nueva_ventana)
            frame.pack(fill=tk.X, pady=5, padx=20)
            tk.Label(frame, text=f"{etiqueta}:", font=("Arial", 14, "bold"), width=20, anchor="w").pack(side=tk.LEFT)
            tk.Label(frame, text=valor, font=("Arial", 14), anchor="w").pack(side=tk.LEFT)

        # Botón para cerrar la ventana
        tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=20)
       
    
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<< DOCUMENTOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Parte inferior: Frame de documentos
        # Parte inferior: Frame de documentos
        #self.frame_documentos = tk.Frame(self.content_frame, bg="white")
        #self.frame_documentos.pack(padx=10, pady=(5, 5), fill=tk.BOTH, expand=True)

        # Título de la sección de documentos
       # self.label_documentos = CTkLabel(
       #     self.frame_documentos,
       ##     text="Documentos Subidos",
        #    font=("Arial", 20, "bold"),
        #    text_color=COLOR_FONT_PURPLE,
        #)
        #self.label_documentos.grid(row=0, column=0, padx=10, pady=5, sticky="w")

         # Crear etiquetas y botones de descarga para cada documento
        #self.crear_documento_descarga(self.frame_documentos, "Tarjeta de identidad:", estudiante["documentos"]["cedula"], 1)
        #self.crear_documento_descarga(self.frame_documentos, "Registro civil:", estudiante["documentos"]["certificado_nacimiento"], 2)
        #self.crear_documento_descarga(self.frame_documentos, "Boletines:", estudiante["documentos"]["boletines"], 3)
        #self.crear_documento_descarga(self.frame_documentos, "Historia clínica:", estudiante["documentos"]["historia_clinica"], 4)

    # Método que crea la etiqueta y el botón de descarga
    #def crear_documento_descarga(self, frame, label_text, documento_path, row):
    #    """Crea la etiqueta y el botón de descarga para un documento."""
    #    fila = tk.Frame(frame, bg="white")
    #   fila.grid(row=row, column=0, sticky="w", padx=5, pady=2)

         # Etiqueta para el nombre del documento
    #    label = CTkLabel(fila, font=("Arial", 16), text=label_text, text_color=COLOR_FONT_BLACK)
    #    label.pack(side=tk.LEFT, padx=5)

         # Botón de descarga
    #    download_button = CTkButton(fila, 
    #        text="Descargar", 
    #        command=lambda path=documento_path: self.descargar_documento(path),
    #        fg_color="#65558F", 
    #        text_color="white", 
    #        hover_color="#B3A6D6"
    #    )
    #    download_button.pack(side=tk.LEFT, padx=10)

     # Método para descargar el documento
    #def descargar_documento(self, path):
    #    """Método para descargar el archivo del documento."""
    #    try:
    #        # Aquí puedes utilizar filedialog para pedir la ubicación donde guardar el archivo
    #        destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    #        
    #        if destino:
    #            # Aquí deberías copiar o mover el archivo de la ruta original a la ruta destino
    ##            # Usaremos shutil para mover el archivo (asegúrate de importar shutil)
    #           import shutil
    #            shutil.copy(path, destino)  # Copia el archivo al destino seleccionado
    #            mb.showinfo("Éxito", f"Documento descargado en: {destino}")
    #        else:
    #            mb.showwarning("Error", "No se seleccionó un destino para guardar el archivo.")
    #    except Exception as e:
    #        mb.showerror("Error", f"No se pudo descargar el archivo. Error: {e}")

            
    #def agregar_label(self, frame, label_text, value_text, row):
    #    """Agrega una fila con un texto y su valor en el layout utilizando pack."""
    #    # Contenedor horizontal para el texto y valor
    #    fila = tk.Frame(frame, bg="white")
    #    fila.pack(fill=tk.X, padx=5, pady=2)

    ##    # Etiqueta del texto
     #   label = CTkLabel(
     #       fila,
    ##        font=("Arial", 16, "bold"),
     #       text=label_text,
     ##       text_color=COLOR_FONT_BLACK,
      #  )
     ##   label.pack(side=tk.LEFT, padx=5)

    #    # Etiqueta del valor
    ##    value = CTkLabel(
     #       fila, font=("Arial", 16), text=value_text, text_color=COLOR_FONT_BLACK
     #   )
     #   value.pack(side=tk.LEFT, padx=5)

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
        
        
