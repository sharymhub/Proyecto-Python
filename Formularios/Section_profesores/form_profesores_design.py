import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from config import COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL
from customtkinter import (
    CTk,
    CTkFrame,
    CTkEntry,
    CTkButton,
    CTkLabel,
    CTkCheckBox,
    CTkOptionMenu,
)
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime
import re
COLOR_CUERPO_PRINCIPAL = "#f5f5f5"
COLOR_BOTON_AGREGAR = "#6a1b9a"
COLOR_BOTON_CANCELAR = "#757575"
COLOR_BORDE_ENTRADA = "#8e44ad"
COLOR_FONDO_TITULO = "#b39ddb"
COLOR_TEXTO = "#000"  # Gris Negro (Muy Oscuro)
import mysql.connector


class FormularioProfesoresDesign:

    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

        self.Btn_EditarUsuario = CTkButton(
            self.barra_superior,
            text="Editar Profesor",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            compound="left",
            command=self.Editar_Profesor,
        )
        self.Btn_EditarUsuario.image = icon
        self.Btn_EditarUsuario.pack(side=tk.LEFT, padx=10, pady=10)

        self.Btn_NuevoUsuario = CTkButton(
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
            command=self.Crear_Nuevo_Profesor,
        )
        self.Btn_NuevoUsuario.image = icon
        self.Btn_NuevoUsuario.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Botón Eliminar
        self.Btn_EliminarUsuario = CTkButton(
            self.barra_superior,
            text="Eliminar Profesor",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            command=self.Eliminar_Profesor
        )
        self.Btn_EliminarUsuario.pack(side=tk.LEFT, padx=10, pady=10)
        
        
        
        self.formtabla= tk.LabelFrame(panel_principal, background= 'purple')
        self.formtabla.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
         # Tabla para mostrar los usuarios 
        self.tabla = ttk.Treeview(self.formtabla, columns=["Nombre", "Correo", "Tipo DNI", "N° DNI", "Telefono", "Direccion", "Grado a cargo", "Materia a cargo", "Contrato",], show="headings")
        self.tabla.pack(fill="both",expand=True)
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Tipo DNI", text="Tipo DNI")
        self.tabla.heading("N° DNI", text="N° DNI")
        self.tabla.heading("Telefono", text="Teléfono")
        self.tabla.heading("Direccion", text="Direccion")
        self.tabla.heading("Grado a cargo", text="Grado a cargo")
        self.tabla.heading("Materia a cargo", text="Materia a cargo")
        self.tabla.heading("Contrato", text="Contrato")
      
        
        
        
        self.tabla.column("Nombre", width=100)
        self.tabla.column("Correo", width=120)
        self.tabla.column("Tipo DNI", width=60)
        self.tabla.column("N° DNI", width=100)
        self.tabla.column("Telefono", width=100)
        self.tabla.column("Direccion", width=80)
        self.tabla.column("Grado a cargo", width=60)
        self.tabla.column("Materia a cargo", width=70)
        self.tabla.column("Contrato", width=80)
    
        
        # Cargar los datos desde la base de datos
        self.cargarprofesores()
        
    def cargarprofesores(self):  
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                # Consulta con JOIN para obtener el nombre de la materia
                cursor.execute("""
                    SELECT 
                        p.Nombre, 
                        p.Correo_electronico, 
                        p.Tipodedocumento, 
                        p.N°documento, 
                        p.Telefono, 
                        p.Direccion, 
                        p.Gradoacargo, 
                        m.Nombre AS Materiaacargo, 
                        p.Contrato
                    FROM profesores p
                    LEFT JOIN materias m ON p.Materiaacargo = m.idmateria
                """)
                usuarios = cursor.fetchall()

                if not usuarios:
                    print("No se encontraron Profesores.")
                else:
                    print("Profesores encontrados: ", usuarios)

                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                # Insertar los datos en la tabla
                for profesor in usuarios:
                    nombre = profesor[0]
                    correo = profesor[1]
                    tipodni = profesor[2]
                    Ndni = profesor[3]
                    telefono = int(profesor[4]) if isinstance(profesor[4], float) and profesor[4].is_integer() else profesor[4]
                    direccion = profesor[5]
                    grado = profesor[6]
                    materia = profesor[7] if profesor[7] else "No asignada"  # Manejo de materias no asignadas
                    contrato = profesor[8]

                    self.tabla.insert('', 'end', values=(nombre, correo, tipodni, Ndni, telefono, direccion, grado, materia, contrato))

            except Exception as e:
                print("Error al cargar profesores:", e)
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
        
        
      


    # ///////////////////// CREAR NUEVO USUARIO //////////////////////
    def Crear_Nuevo_Profesor(self, modo="Nuevo "):
        self.Ventana_formulario_nuevo_usuario = tk.Toplevel()
        self.Ventana_formulario_nuevo_usuario.title(modo.capitalize() + "Profesor")
        
        # Tamaño deseado para la ventana (puedes ajustarlo según tus preferencias)
        ancho_ventana =450 
        alto_ventana = 510
        
        # Obtener las dimensiones de la pantalla
        screen_width = self.Ventana_formulario_nuevo_usuario.winfo_screenwidth()
        screen_height = self.Ventana_formulario_nuevo_usuario.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        posicion_x = int((screen_width - ancho_ventana) / 2)
        posicion_y = int((screen_height - alto_ventana) / 2)
        
        # Establecer la geometría de la ventana con tamaño ajustado y centrado
        self.Ventana_formulario_nuevo_usuario.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        self.Ventana_formulario_nuevo_usuario.configure(bg="white")
        self.cargar_materias()

        # Eliminar la barra de título y los controles de la ventana
        self.Ventana_formulario_nuevo_usuario.overrideredirect(False)

        # El resto del formulario sigue igual que antes
        self.frame_titulo = CTkFrame(self.Ventana_formulario_nuevo_usuario, fg_color=COLOR_BORDE_ENTRADA)
        self.frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.Titulo_pagina = CTkLabel(self.frame_titulo, text=modo.capitalize() + "Profesor", font=("Arial", 24))
        self.Titulo_pagina.pack(expand=True, pady=5)

        # Crear formulario con grid
        # Campo Nombre de usuario
        self.label_nombre = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Nombre de Profesor:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_nombre.grid(row=1, column=0, sticky="w", padx=(15,5), pady=5)
        self.entry_nombre = CTkEntry(self.Ventana_formulario_nuevo_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_nombre.grid(row=1, column=1, sticky="w",padx=5, pady=5)

        # Campo Correo
        self.label_correo = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Correo electrónico:", text_color=COLOR_TEXTO, font=("Arial", 14,"bold"))
        self.label_correo.grid(row=2, column=0, sticky="w", padx=(15,5), pady=5)
        self.entry_correo = CTkEntry(self.Ventana_formulario_nuevo_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_correo.grid(row=2, column=1, sticky="w",padx=5, pady=5)

        # Campo Tipo documento (opciones desplegables)
        self.label_tipodni = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Tipo Documento:", text_color=COLOR_TEXTO,font=("Arial", 14, "bold"))
        self.label_tipodni.grid(row=3, column=0, sticky="w", padx=(15,5), pady=5)
        self.option_tipodni = CTkOptionMenu(self.Ventana_formulario_nuevo_usuario, values=["CC", "CE"], width=250, fg_color="#cdcdcd", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_tipodni.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        # Campo Documento
        self.label_DNI = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="DNI:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_DNI.grid(row=4, column=0, sticky="w", padx=(15,5), pady=5)
        self.entry_DNI = CTkEntry(self.Ventana_formulario_nuevo_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_DNI.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # Campo Teléfono
        self.label_telefono = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Teléfono:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_telefono.grid(row=5, column=0, sticky="w", padx=(15,5), pady=5)
        self.entry_telefono = CTkEntry(self.Ventana_formulario_nuevo_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_telefono.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        # Campo Dirección
        self.label_direccion = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Dirección:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_direccion.grid(row=6, column=0, sticky="w", padx=(15,5), pady=5)
        self.entry_direccion = CTkEntry(self.Ventana_formulario_nuevo_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_direccion.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        # Campo fecha de nacimiento
        self.label_fechanacimiento = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Fecha de nacimiento:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_fechanacimiento.grid(row=7, column=0, sticky="w", padx=(15,5), pady=5)
        self.date_entry_fechanacimiento = DateEntry(self.Ventana_formulario_nuevo_usuario, width=20, background="#2C3E50", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_entry_fechanacimiento.grid(row=7, column=1, sticky="w", padx=5, pady=5)

        # Campo grado a cargo
        self.label_gradocargo = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Grado a cargo:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_gradocargo.grid(row=8, column=0, sticky="w", padx=(15,5), pady=5)
        self.option_gradocargo = CTkOptionMenu(self.Ventana_formulario_nuevo_usuario, values=["1", "2", "3", "4", "5"], width=250, fg_color="#cdcdcd", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_gradocargo.grid(row=8, column=1, padx=5, sticky="w", pady=5)

        # Campo materia a cargo
        self.label_materia = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Materia a cargo:", text_color=COLOR_TEXTO, font=("Arial", 14, "bold"))
        self.label_materia.grid(row=9, column=0, sticky="w", padx=(15,5), pady=5)
        materias = self.cargar_materias()
        lista_materias = [f"{materia[0]} - {materia[1]}" for materia in materias] if materias else ["No hay materias disponibles"]
        self.option_materia = CTkOptionMenu(self.Ventana_formulario_nuevo_usuario, values=lista_materias, width=250, fg_color="#cdcdcd", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_materia.grid(row=9, column=1, padx=5, sticky="w", pady=5)

        # Campo fecha de contratación
        self.label_fechacontrato = CTkLabel(self.Ventana_formulario_nuevo_usuario, text="Fecha de contratación:", text_color=COLOR_TEXTO, font=("Arial", 14,"bold"))
        self.label_fechacontrato.grid(row=10, column=0, sticky="w", padx=(15,5), pady=5)
        self.date_entry_fechacontrato = DateEntry(self.Ventana_formulario_nuevo_usuario, width=20, background="#2C3E50", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_entry_fechacontrato.grid(row=10, column=1, padx=5, sticky="w", pady=5)

        # Botones
        self.frame_botones = CTkFrame(self.Ventana_formulario_nuevo_usuario, fg_color="white")
        self.frame_botones.grid(row=11, column=0, columnspan=2, sticky="nsew", padx=25, pady=5)
        # Configuración para centrar los botones
        
        self.frame_botones.grid_columnconfigure(0, weight=1)  # Espacio antes del botón "Cancelar"
        self.frame_botones.grid_columnconfigure(1, weight=0)  # Columna del botón "Cancelar"
        self.frame_botones.grid_columnconfigure(2, weight=0)  # Columna del botón "Guardar"
        self.frame_botones.grid_columnconfigure(3, weight=1)  # Espacio después del botón "Guardar"
        
        # Botón Cancelar
        self.btn_cancelar = CTkButton(
            self.frame_botones,
            text="Cancelar",
            font=("Arial", 16),
            fg_color=COLOR_BOTON_CANCELAR,
            hover_color="#757575",
            width=100,
            height=30,
            command=self.Ventana_formulario_nuevo_usuario.destroy
        )
        self.btn_cancelar.grid(row=0, column=1, padx=10, pady=10)

        # Botón Guardar
        self.btn_guardar = CTkButton(
            self.frame_botones,
            text="Guardar",
            font=("Arial", 16),
            fg_color=COLOR_BOTON_AGREGAR,
            hover_color=COLOR_BOTON_AGREGAR,
            width=100,
            height=30,
            command=self.agregar_profesor
        )
        self.btn_guardar.grid(row=0, column=2, padx=10, pady=10)
        
     # //////// EDITAR USUARIO /////////   
    def Editar_Profesor(self, modo="Editar "):
    # Obtener la selección actual en la tabla
    
        seleccion = self.tabla.selection()
        if not seleccion:
            mb.showwarning("Selección vacía", "Por favor, selecciona un Profesor para editar.")
            return
        
        # Obtener los datos del usuario seleccionado
        item = seleccion[0]
        usuario_seleccionado = self.tabla.item(item)
        datos_usuario = usuario_seleccionado["values"]  # [Correo, Nombreusuario, Contraseña, Telefono, Rol]
        
        # Crear ventana de edición
        self.Ventana_formulario_editar_usuario = tk.Toplevel()
        self.Ventana_formulario_editar_usuario.title(modo.capitalize() + "Profesor")
        self.Ventana_formulario_editar_usuario.geometry("325x750+600+30")
        self.Ventana_formulario_editar_usuario.configure(bg="white")
        self.Ventana_formulario_editar_usuario.resizable(True, True)

        # Encabezado de la ventana
        self.frame_titulo = CTkFrame(self.Ventana_formulario_editar_usuario, fg_color=COLOR_BORDE_ENTRADA)
        self.frame_titulo.pack(fill="x", pady=10)
        
        self.Titulo_pagina = CTkLabel(self.frame_titulo, text=modo.capitalize() + "Profesor", font=("Arial", 20))
        self.Titulo_pagina.pack(pady=10)

        # Campos de edición
        self.label_nombre = CTkLabel(self.Ventana_formulario_editar_usuario, text="Nombre de Profesor:", text_color=COLOR_TEXTO)
        self.label_nombre.pack(anchor="w", padx=20)
        self.entry_nombre = CTkEntry(self.Ventana_formulario_editar_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_nombre.pack(pady=5)
        self.entry_nombre.insert(0, datos_usuario[0])

        # Campo Correo
        self.label_correo = CTkLabel(self.Ventana_formulario_editar_usuario, text="Correo electrónico:", text_color=COLOR_TEXTO)
        self.label_correo.pack(anchor="w", padx=20)
        self.entry_correo = CTkEntry(self.Ventana_formulario_editar_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_correo.pack(pady=5)
        self.entry_correo.insert(0, datos_usuario[1])
        self.entry_correo.configure(state="disabled")  # Correo no editable

        # Tipo Documento
        self.label_tipodni = CTkLabel(self.Ventana_formulario_editar_usuario, text="Tipo Documento:", text_color=COLOR_TEXTO)
        self.label_tipodni.pack(anchor="w", padx=20)
        self.option_tipodni = CTkOptionMenu(self.Ventana_formulario_editar_usuario, values=["CC", "CE"], width=250, fg_color="white", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_tipodni.pack(pady=5)
        self.option_tipodni.set(datos_usuario[2])

        # Campo DNI
        self.label_DNI = CTkLabel(self.Ventana_formulario_editar_usuario, text="DNI:", text_color=COLOR_TEXTO)
        self.label_DNI.pack(anchor="w", padx=20)
        self.entry_DNI = CTkEntry(self.Ventana_formulario_editar_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_DNI.pack(pady=5)
        self.entry_DNI.insert(0, datos_usuario[3])

        # Teléfono
        self.label_telefono = CTkLabel(self.Ventana_formulario_editar_usuario, text="Teléfono:", text_color=COLOR_TEXTO)
        self.label_telefono.pack(anchor="w", padx=20)
        self.entry_telefono = CTkEntry(self.Ventana_formulario_editar_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_telefono.pack(pady=5)
        self.entry_telefono.insert(0, datos_usuario[4])

        # Dirección
        self.label_direccion = CTkLabel(self.Ventana_formulario_editar_usuario, text="Dirección:", text_color=COLOR_TEXTO)
        self.label_direccion.pack(anchor="w", padx=20)
        self.entry_direccion = CTkEntry(self.Ventana_formulario_editar_usuario, width=250, border_color=COLOR_BORDE_ENTRADA, fg_color="white", text_color=COLOR_TEXTO)
        self.entry_direccion.pack(pady=5)
        self.entry_direccion.insert(0, datos_usuario[5])

        # Grado a cargo
        self.label_gradocargo = CTkLabel(self.Ventana_formulario_editar_usuario, text="Grado a cargo:", text_color=COLOR_TEXTO)
        self.label_gradocargo.pack(anchor="w", padx=20)
        self.option_gradocargo = CTkOptionMenu(self.Ventana_formulario_editar_usuario, values=["1", "2", "3", "4", "5"], width=250, fg_color="white", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_gradocargo.pack(pady=5)
        self.option_gradocargo.set(datos_usuario[6])

        # Materia a cargo
        self.label_materia = CTkLabel(self.Ventana_formulario_editar_usuario, text="Materia a cargo:", text_color=COLOR_TEXTO)
        self.label_materia.pack(anchor="w", padx=20)
        materias = self.cargar_materias()
        lista_materias = [f"{materia[0]} - {materia[1]}" for materia in materias] if materias else ["No hay materias disponibles"]
        self.option_materia = CTkOptionMenu(self.Ventana_formulario_editar_usuario, values=lista_materias, width=250, fg_color="white", button_color="white", button_hover_color=COLOR_BOTON_AGREGAR, dropdown_fg_color="white", dropdown_hover_color=COLOR_FONDO_TITULO, text_color=COLOR_TEXTO, dropdown_text_color=COLOR_TEXTO)
        self.option_materia.pack(pady=5)

        # Seleccionar la materia actual del usuario
        for materia in materias:
            if str(materia[0]) == str(datos_usuario[7]):
                self.option_materia.set(f"{materia[0]} - {materia[1]}")
                break

        # Fecha de contratación
        self.label_fechacontrato = CTkLabel(self.Ventana_formulario_editar_usuario, text="Fecha de contratación:", text_color=COLOR_TEXTO)
        self.label_fechacontrato.pack(anchor="w", padx=20)
        self.date_entry_fechacontrato = DateEntry(self.Ventana_formulario_editar_usuario, width=20, background="#2C3E50", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
        self.date_entry_fechacontrato.pack(pady=5)
        self.date_entry_fechacontrato.set_date(datos_usuario[8])

        # Botones
        self.frame_botones = CTkFrame(self.Ventana_formulario_editar_usuario, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.frame_botones.pack(pady=20)

        self.btn_cancelar = CTkButton(self.frame_botones, text="Cancelar", fg_color=COLOR_BOTON_CANCELAR, hover_color="#757575", width=100, height=30, command=self.Ventana_formulario_editar_usuario.destroy)
        self.btn_cancelar.grid(row=0, column=0, padx=10)

        self.btn_guardar = CTkButton(self.frame_botones, text="Guardar Cambios", fg_color=COLOR_BOTON_AGREGAR, hover_color=COLOR_BOTON_AGREGAR, width=100, height=30, command=lambda: self.guardar_cambios_profesor(datos_usuario[1]))  # Pasar correo como identificador
        self.btn_guardar.grid(row=0, column=1, padx=10)


    def guardar_cambios_profesor(self, correo):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        tipodni = self.option_tipodni.get()
        Ndni = self.entry_DNI.get()
        telefono = self.entry_telefono.get()
        direccion = self.entry_direccion.get()
        grado = self.option_gradocargo.get()
        materia_seleccionada = self.option_materia.get()  # Ejemplo: "1 - Matemáticas"
        materia_id = materia_seleccionada.split(" - ")[0]  # Obtiene solo el ID de la materia
        contrato = self.date_entry_fechacontrato.get_date()

        # Validación
        if not all([nombre, correo, tipodni, Ndni, telefono, direccion, grado, materia_id, contrato]):
            mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        # Formatear fechas
        try:
            
            contrato_formateado = datetime.strptime(contrato, "%Y-%m-%d") if isinstance(contrato, str) else contrato
        except ValueError:
            mb.showerror("Formato de fecha inválido", "Asegúrate de que las fechas estén en el formato AAAA-MM-DD.")
            return

        # Conexión a la base de datos
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                # Actualizar datos en la base de datos
                cursor.execute("""
                    UPDATE profesores
                    SET Nombre = %s, 
                        Correo_electronico = %s, 
                        Tipodedocumento = %s, 
                        N°documento = %s, 
                        Telefono = %s, 
                        Direccion = %s, 
                        Gradoacargo = %s, 
                        Materiaacargo = %s, 
                        Contrato = %s
                    WHERE Correo_electronico = %s
                """, (
                    nombre,
                    correo,
                    tipodni,
                    Ndni,
                    telefono,
                    direccion,
                    grado,
                    materia_id,
                    contrato_formateado.strftime("%Y-%m-%d"),
                    correo  # Correo actual como condición
                ))
                conn.commit()
                mb.showinfo("Éxito", "Datos actualizados correctamente.")
                self.Ventana_formulario_editar_usuario.destroy()
                
            except Exception as e:
                mb.showerror("Error en la base de datos", f"Hubo un error al actualizar los datos: {e}")
            finally:
                self.cargarprofesores()
                cursor.close()
                conn.close()
        else:
            mb.showerror("Conexión fallida", "No se pudo conectar a la base de datos.")

    def cargar_materias(self):
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT idmateria, Nombre FROM materias")
                materias = cursor.fetchall()  # Obtiene todas las materias
                return materias  # Retorna una lista de tuplas [(idmateria, nombre), ...]
            except Exception as e:
                mb.showerror("Error en la base de datos", f"Hubo un error al cargar las materias: {e}")
            finally:
                cursor.close()
                conn.close()
        return []  # Devuelve una lista vacía si ocurre un error
 # ///////////////////// AGREGAR USUARIO //////////////////////
    def agregar_profesor(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        tipodni = self.option_tipodni.get()
        Ndni = self.entry_DNI.get()
        telefono = self.entry_telefono.get()
        direccion = self.entry_direccion.get()
        nacimiento = self.date_entry_fechanacimiento.get_date()
        grado = self.option_gradocargo.get()
        materia = self.option_materia.get().split(" - ")[0]
        contrato = self.date_entry_fechacontrato.get_date()

        # Validación
        if not all([nombre, correo, tipodni, Ndni, telefono, direccion, nacimiento, grado, materia, contrato]):
            mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        # Conectar a la base de datos
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO profesores (Nombre, Correo_electronico, Tipodedocumento, N°documento, Telefono, Direccion, Fechanacimiento, Gradoacargo, Materiaacargo, Contrato)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (nombre, correo, tipodni, Ndni, telefono, direccion, nacimiento, grado, materia, contrato))
                conn.commit()
                mb.showinfo("Usuario agregado", "El usuario ha sido agregado exitosamente.")
                self.Ventana_formulario_nuevo_usuario.destroy()
                self.cargarprofesores()  # Recargar la tabla de usuarios
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al agregar el usuario: {err}")
            finally:
                conn.close()
                
    def Eliminar_Profesor(self):
        # Obtener el usuario seleccionado en la tabla
        seleccion = self.tabla.selection()
        
        if not seleccion:
            mb.showwarning("Selección vacía", "Por favor, selecciona un usuario para eliminar.")
            return
        
        # Obtener el identificador único (Correo) del usuario seleccionado
        item = seleccion[0]
        usuario_seleccionado = self.tabla.item(item)
        nombre_usuario = usuario_seleccionado["values"][0]  # Correo es la primera columna
        
        # Confirmar la eliminación
        confirmacion = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el usuario con correo: {nombre_usuario}?")
        
        if confirmacion:
            # Conectar a la base de datos
            conn = self.conectar_mysql()
            if conn:
                try:
                    cursor = conn.cursor()
                    # Eliminar el usuario de la base de datos usando el nombre del profesor como identificador
                    cursor.execute("""
                        DELETE FROM profesores WHERE Nombre = %s
                    """, (nombre_usuario,))
                    conn.commit()
                    
                    # Verificar si se eliminó algún registro
                    if cursor.rowcount > 0:
                        mb.showinfo("Usuario eliminado", f"El usuario con correo {nombre_usuario} ha sido eliminado exitosamente.")
                        self.cargarprofesores()  # Recargar la tabla de usuarios
                    else:
                        mb.showwarning("Error", "No se pudo eliminar el usuario. Verifique que el usuario exista.")
                
                except mysql.connector.Error as err:
                    mb.showerror("Error", f"Error al eliminar el usuario: {err}")
                finally:
                    conn.close()
