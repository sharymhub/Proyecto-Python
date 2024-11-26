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

COLOR_CUERPO_PRINCIPAL = "#f5f5f5"
COLOR_BOTON_AGREGAR = "#6a1b9a"
COLOR_BOTON_CANCELAR = "#757575"
COLOR_BORDE_ENTRADA = "#8e44ad"
COLOR_FONDO_TITULO = "#b39ddb"
COLOR_TEXTO = "#000"
import mysql.connector


class FormularioUsuariosDesign:

    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

        self.Btn_EditarUsuario = CTkButton(
            self.barra_superior,
            text="Editar usuario",
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
            command=self.Editar_Usuario,
        )
        self.Btn_EditarUsuario.image = icon
        self.Btn_EditarUsuario.pack(side=tk.LEFT, padx=10, pady=10)

        self.Btn_NuevoUsuario = CTkButton(
            self.barra_superior,
            text="Nuevo usuario",
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
            command=self.Crear_Nuevo_Usuario,
        )
        self.Btn_NuevoUsuario.image = icon
        self.Btn_NuevoUsuario.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Botón Eliminar
        self.Btn_EliminarUsuario = CTkButton(
            self.barra_superior,
            text="Eliminar usuario",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            command=self.Eliminar_Usuario
        )
        self.Btn_EliminarUsuario.pack(side=tk.LEFT, padx=10, pady=10)
        
        
        
        self.formtabla= tk.LabelFrame(panel_principal, background= 'purple')
        self.formtabla.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
         # Tabla para mostrar los usuarios 
        self.tabla = ttk.Treeview(self.formtabla, columns=["Correo", "Nombreusuario", "Contraseña", "Telefono", "Rol"], show="headings")
        self.tabla.pack(fill="both",expand=True)
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Nombreusuario", text="Nombre usuario")
        self.tabla.heading("Contraseña", text="Contraseña")
        self.tabla.heading("Telefono", text="Teléfono")
        self.tabla.heading("Rol", text="Rol")
        self.tabla.column("Correo", width=120)
        self.tabla.column("Nombreusuario", width=100)
        self.tabla.column("Contraseña", width=120)
        self.tabla.column("Telefono", width=100)
        self.tabla.column("Rol", width=100)
        
        # Cargar los datos desde la base de datos
        self.cargarusuarios()
        
    def cargarusuarios(self):  
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT Correo, Nombreusuario, Contraseña, Telefono, Rol FROM usuarios
                """)
                usuarios = cursor.fetchall()

                if not usuarios:
                    print("No se encontraron usuarios.")
                else:
                    print("Usuarios encontrados: ", usuarios)

                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                # Insertar los datos en la tabla
                for usuario in usuarios:
                    self.tabla.insert('', 'end', values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])) 

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
        
        
      


    # ///////////////////// CREAR NUEVO USUARIO //////////////////////
    def Crear_Nuevo_Usuario(self, modo="Nuevo "):
        self.Ventana_formulario_nuevo_usuario = tk.Toplevel()
        self.Ventana_formulario_nuevo_usuario.title(modo.capitalize() + "usuario")
        self.Ventana_formulario_nuevo_usuario.geometry("300x480+1100+400")
        self.Ventana_formulario_nuevo_usuario.configure(bg="white")

        # Eliminar la barra de título y los controles de la ventana
        self.Ventana_formulario_nuevo_usuario.overrideredirect(True)

        # Encabezado de la ventana
        self.frame_titulo = CTkFrame(
            self.Ventana_formulario_nuevo_usuario, fg_color=COLOR_BORDE_ENTRADA
        )
        self.frame_titulo.pack(fill="x", pady=10)
        self.Titulo_pagina = CTkLabel(
            self.frame_titulo, text=modo.capitalize() + "Usuario", font=("Arial", 20)
        )
        self.Titulo_pagina.pack(pady=10)

        # Campo Nombre de usuario
        self.label_nombre = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Nombre de usuario:",
            text_color=COLOR_TEXTO,
        )
        self.label_nombre.pack(anchor="w", padx=20)
        self.entry_nombre = CTkEntry(
            self.Ventana_formulario_nuevo_usuario,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_nombre.pack(pady=5)

        # Campo Contraseña
        self.label_contraseña = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Contraseña:",
            text_color=COLOR_TEXTO,
        )
        self.label_contraseña.pack(anchor="w", padx=20)
        self.entry_contraseña = CTkEntry(
            self.Ventana_formulario_nuevo_usuario,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_contraseña.pack(pady=5)

        # Campo Cargo (opciones desplegables)
        self.label_cargo = CTkLabel(
            self.Ventana_formulario_nuevo_usuario, text="Cargo:", text_color=COLOR_TEXTO
        )
        self.label_cargo.pack(anchor="w", padx=20)
        self.option_cargo = CTkOptionMenu(
            self.Ventana_formulario_nuevo_usuario,
            values=["Administrativo", "Profesor"],
            width=250,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_BOTON_AGREGAR,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONDO_TITULO,
            text_color=COLOR_TEXTO,
            dropdown_text_color=COLOR_TEXTO,
        )
        self.option_cargo.pack(pady=5)

        # Campo Teléfono
        self.label_telefono = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Teléfono:",
            text_color=COLOR_TEXTO,
        )
        self.label_telefono.pack(anchor="w", padx=20)
        self.entry_telefono = CTkEntry(
            self.Ventana_formulario_nuevo_usuario,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_telefono.pack(pady=5)

        # Campo Correo Electrónico
        self.label_correo = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Correo Electrónico:",
            text_color=COLOR_TEXTO,
        )
        self.label_correo.pack(anchor="w", padx=20)
        self.entry_correo = CTkEntry(
            self.Ventana_formulario_nuevo_usuario,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_correo.pack(pady=5)

        # Botones
        self.frame_botones = CTkFrame(
            self.Ventana_formulario_nuevo_usuario, fg_color=COLOR_CUERPO_PRINCIPAL
        )
        self.frame_botones.pack(pady=20)

        self.btn_cancelar = CTkButton(
            self.frame_botones,
            text="Cancelar",
            fg_color=COLOR_BOTON_CANCELAR,
            hover_color="#757575",
            width=100,
            height=30,
            command=self.Ventana_formulario_nuevo_usuario.destroy,
        )
        self.btn_cancelar.grid(row=0, column=0, padx=10)

        self.btn_agregar = CTkButton(
            self.frame_botones,
            text="Agregar",
            fg_color=COLOR_BOTON_AGREGAR,
            hover_color=COLOR_BOTON_AGREGAR,
            width=100,
            height=30,
            command=self.agregar_usuario
        )
        self.btn_agregar.grid(row=0, column=1, padx=10)

    def Editar_Usuario(self):
        # Llamar a Crear_Nuevo_Usuario pero en modo editar
        self.Crear_Nuevo_Usuario(modo="Editar ")

 # ///////////////////// AGREGAR USUARIO //////////////////////
    def agregar_usuario(self):
        nombre_usuario = self.entry_nombre.get()
        contrasena = self.entry_contraseña.get()
        cargo = self.option_cargo.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()

        # Validación
        if not all([nombre_usuario, contrasena, cargo, telefono, correo]):
            mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        # Conectar a la base de datos
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO usuarios (Nombreusuario, Contraseña, Rol, Telefono, Correo)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nombre_usuario, contrasena, cargo, telefono, correo))
                conn.commit()
                mb.showinfo("Usuario agregado", "El usuario ha sido agregado exitosamente.")
                self.Ventana_formulario_nuevo_usuario.destroy()
                self.cargarusuarios()  # Recargar la tabla de usuarios
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al agregar el usuario: {err}")
            finally:
                conn.close()
                
    def Eliminar_Usuario(self):
        # Obtener el usuario seleccionado en la tabla
        seleccion = self.tabla.selection()
        
        if not seleccion:
            mb.showwarning("Selección vacía", "Por favor, selecciona un usuario para eliminar.")
            return
        
        # Obtener el identificador único (Correo) del usuario seleccionado
        item = seleccion[0]
        usuario_seleccionado = self.tabla.item(item)
        correo_usuario = usuario_seleccionado["values"][0]  # Correo es la primera columna
        
        # Confirmar la eliminación
        confirmacion = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el usuario con correo: {correo_usuario}?")
        
        if confirmacion:
            # Conectar a la base de datos
            conn = self.conectar_mysql()
            if conn:
                try:
                    cursor = conn.cursor()
                    # Eliminar el usuario de la base de datos usando el correo como identificador
                    cursor.execute("""
                        DELETE FROM usuarios WHERE Correo = %s
                    """, (correo_usuario,))
                    conn.commit()
                    
                    # Verificar si se eliminó algún registro
                    if cursor.rowcount > 0:
                        mb.showinfo("Usuario eliminado", f"El usuario con correo {correo_usuario} ha sido eliminado exitosamente.")
                        self.cargarusuarios()  # Recargar la tabla de usuarios
                    else:
                        mb.showwarning("Error", "No se pudo eliminar el usuario. Verifique que el usuario exista.")
                
                except mysql.connector.Error as err:
                    mb.showerror("Error", f"Error al eliminar el usuario: {err}")
                finally:
                    conn.close()
