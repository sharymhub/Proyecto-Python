import tkinter as tk
from tkinter import ttk
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

COLOR_CUERPO_PRINCIPAL = "#f5f5f5"
COLOR_BOTON_AGREGAR = "#6a1b9a"
COLOR_BOTON_CANCELAR = "#757575"
COLOR_BORDE_ENTRADA = "#8e44ad"
COLOR_FONDO_TITULO = "#b39ddb"
COLOR_TEXTO = "#000"  # Gris Negro (Muy Oscuro)

from tkinter import messagebox as mb
import mysql.connector

class FormularioMateriasDesign:
    
    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

        # Botón para Editar Materia
        self.Btn_EditarMateria = CTkButton(
            self.barra_superior,
            text="Editar Materia",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            compound="left",
            command=self.Editar_Materia,
        )
        self.Btn_EditarMateria.image = icon
        self.Btn_EditarMateria.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para Agregar Materia
        self.Btn_NuevaMateria = CTkButton(
            self.barra_superior,
            text="Agregar Materias",
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
            command=self.Crear_Nueva_Materia,
        )
        self.Btn_NuevaMateria.image = icon
        self.Btn_NuevaMateria.pack(side=tk.RIGHT, padx=10, pady=10)

        # Botón para Eliminar Materia
        self.Btn_EliminarMateria = CTkButton(
            self.barra_superior,
            text="Eliminar Materia",
            font=("JasmineUPC", 16),
            border_color=COLOR_MENU_LATERAL,
            fg_color=COLOR_MENU_LATERAL,
            hover_color=COLOR_MENU_LATERAL,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            compound="left",
            command=self.eliminar_materia,
        )
        self.Btn_EliminarMateria.image = icon
        self.Btn_EliminarMateria.pack(side=tk.LEFT, padx=10, pady=10)

        # Contenedor para la tabla de materias
        self.formtabla = tk.LabelFrame(panel_principal, background='purple')
        self.formtabla.pack(side=tk.LEFT, padx=10, pady=10)

        # Tabla para mostrar las materias
        self.tabla = ttk.Treeview(self.formtabla, columns=["Nombre", "idProfesor"], show="headings")
        self.tabla.grid(column=0, row=0, padx=5, pady=5)
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("idProfesor", text="Profesor")
        self.tabla.column("Nombre", width=120)

        # Cargar los datos desde la base de datos
        self.cargar_materias()

    # Nueva función para eliminar una materia
    def eliminar_materia(self):
        # Obtener la materia seleccionada en la tabla
        selected_item = self.tabla.selection()
        if not selected_item:
            mb.showwarning("Advertencia", "Por favor, seleccione una materia para eliminar.")
            return

        # Confirmar la eliminación
        confirmacion = mb.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar esta materia?")
        if not confirmacion:
            return

        # Obtener el nombre de la materia seleccionada
        materia = self.tabla.item(selected_item, "values")
        nombre_materia = materia[0]

        # Conectar a la base de datos y eliminar la materia
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()

                # Eliminar la materia de la base de datos
                cursor.execute("DELETE FROM materias WHERE Nombre = %s", (nombre_materia,))
                conn.commit()

                mb.showinfo("Éxito", "Materia eliminada correctamente.")

                # Actualizar la tabla
                self.cargar_materias()
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al eliminar la materia: {err}")
            finally:
                conn.close()
        
        
    def cargar_materias(self):  
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT 
                    materias.Nombre AS Materia, 
                    COALESCE(profesores.Nombre, 'No asignada') AS Profesor 
                FROM materias
                LEFT JOIN profesores ON materias.idProfesor = profesores.Correo_electronico
                ORDER BY materias.Nombre
                """)
                materias = cursor.fetchall()

                if not materias:
                    print("No se encontraron materias.")
                else:
                    print("Materias cargadas:", materias)

                # Limpiar la tabla antes de insertar nuevos datos
                self.tabla.delete(*self.tabla.get_children())

                # Insertar los datos en la tabla
                for materia in materias:
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


    # ///////////////////// CREAR NUEVA MATERIA //////////////////////
    def Crear_Nueva_Materia(self, modo="Nueva", nombre_materia=None, correo_profesor=None):
        self.Ventana_formulario_nueva_materia = tk.Toplevel()
        self.Ventana_formulario_nueva_materia.title(modo.capitalize() + " Materia")
        self.Ventana_formulario_nueva_materia.geometry("300x300+980+280")
        self.Ventana_formulario_nueva_materia.configure(bg="white")

        # Encabezado de la ventana
        self.frame_titulo = CTkFrame(
            self.Ventana_formulario_nueva_materia, fg_color=COLOR_BORDE_ENTRADA
        )
        self.frame_titulo.pack(fill="x", pady=10)
        self.Titulo_pagina = CTkLabel(
            self.frame_titulo, text=modo.capitalize() + " Materia", font=("Arial", 20)
        )
        self.Titulo_pagina.pack(pady=10)

        # Campo: Nombre de Materia
        self.label_materia = CTkLabel(
            self.Ventana_formulario_nueva_materia,
            text="Nombre de materia:",
            text_color=COLOR_TEXTO,
            font=("Arial", 16, "bold"),
        )
        self.label_materia.pack(anchor="w", padx=20)
        self.entry_materia = CTkEntry(
            self.Ventana_formulario_nueva_materia,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_materia.pack(pady=5)

        if nombre_materia:  # Si estamos en modo Editar
            self.entry_materia.insert(0, nombre_materia)

        # Campo: Profesor encargado (opciones desplegables)
        self.label_profesor_encargado = CTkLabel(
            self.Ventana_formulario_nueva_materia,
            text="ID profesor encargado de la materia:",
            text_color=COLOR_TEXTO,
        )
        profesores = self.obtener_profesores()
        if not profesores:
            mb.showerror("Error", "No hay profesores disponibles.")
            self.Ventana_formulario_nueva_materia.destroy()
            return

        # Lista de profesores para el menú desplegable
        profesor_nombres = [f"{prof['Nombre']} ({prof['Correo_electronico']})" for prof in profesores]
        self.label_profesor_encargado.pack(anchor="w", padx=20)
        self.option_profesor = CTkOptionMenu(
            self.Ventana_formulario_nueva_materia,
            values=profesor_nombres,
            width=250,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_BOTON_AGREGAR,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONDO_TITULO,
            text_color=COLOR_TEXTO,
            dropdown_text_color=COLOR_TEXTO,
        )
        self.option_profesor.pack(pady=5)

        if correo_profesor:  # Seleccionar el profesor asignado en modo Editar
            for idx, prof in enumerate(profesores):
                if prof["Correo_electronico"] == correo_profesor:
                    self.option_profesor.set(f"{prof['Nombre']} ({prof['Correo_electronico']})")
                    break

        # Botones
        self.frame_botones = CTkFrame(
            self.Ventana_formulario_nueva_materia, fg_color=COLOR_CUERPO_PRINCIPAL
        )
        self.frame_botones.pack(pady=20)

        self.btn_cancelar = CTkButton(
            self.frame_botones,
            text="Cancelar",
            fg_color=COLOR_BOTON_CANCELAR,
            hover_color="#757575",
            width=100,
            height=30,
            command=self.Ventana_formulario_nueva_materia.destroy,
        )
        self.btn_cancelar.grid(row=0, column=0, padx=10)

        self.btn_agregar = CTkButton(
            self.frame_botones,
            text="Guardar" if modo == "Editar" else "Agregar",
            fg_color=COLOR_BOTON_AGREGAR,
            command=lambda: self._procesar_agregar_materia(profesores, modo),
        )
        self.btn_agregar.grid(row=0, column=1, padx=10)

    def _procesar_agregar_materia(self, profesores, modo):
        try:
            opcion = self.option_profesor.get()
            correo_profesor = opcion.split("(")[1].strip(")")
        except IndexError:
            mb.showerror("Error", "Seleccione un profesor válido.")
            return

        nombre_materia = self.entry_materia.get()
        if modo == "Nueva":
            self.agregar_materia(nombre_materia, correo_profesor)
        else:
            self.actualizar_materia(nombre_materia, correo_profesor)
            
    def obtener_profesores(self):
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT Correo_electronico, Nombre FROM profesores")
                return cursor.fetchall()
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al obtener profesores: {err}")
            finally:
                conn.close()
        return []

    def agregar_materia(self, nombre_materia, correo_profesor):
        if not nombre_materia:
            mb.showwarning("Advertencia", "Por favor, ingrese un nombre para la materia.")
            return

        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                
                # Insertar materia y obtener el ID generado
                cursor.execute(
                    "INSERT INTO materias (Nombre, idProfesor) VALUES (%s, %s)",
                    (nombre_materia, correo_profesor),
                )
                id_materia = cursor.lastrowid  # Obtener el ID generado automáticamente

                # Actualizar profesor en tabla de profesores
                cursor.execute(
                    "UPDATE profesores SET materiaacargo = %s WHERE Correo_electronico = %s",
                    (id_materia, correo_profesor),
                )

                conn.commit()
                mb.showinfo("Éxito", "Materia agregada correctamente.")
                self.Ventana_formulario_nueva_materia.destroy()
                self.cargar_materias()
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al agregar la materia: {err}")
            finally:
                conn.close()

    def actualizar_materia_a_cargo(self, correo_profesor, id_nueva_materia):
        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()

                # Actualizar el campo materiaacargo del profesor
                cursor.execute(
                    "UPDATE profesores SET materiaacargo = %s WHERE Correo_electronico = %s",
                    (id_nueva_materia, correo_profesor)
                )

                # Actualizar el profesor asociado en la tabla materias
                cursor.execute(
                    "UPDATE materias SET idProfesor = %s WHERE idmateria = %s",
                    (correo_profesor, id_nueva_materia)
                )

                conn.commit()
                mb.showinfo("Éxito", "Los cambios se reflejaron correctamente.")
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al actualizar los datos: {err}")
            finally:
                conn.close()




    

    def Editar_Materia(self):
        # Obtener la materia seleccionada en la tabla
        selected_item = self.tabla.selection()
        if not selected_item:
            mb.showwarning("Advertencia", "Por favor, seleccione una materia para editar.")
            return

        # Obtener los datos de la materia seleccionada
        materia = self.tabla.item(selected_item, "values")
        nombre_materia = materia[0]
        correo_profesor = materia[1] if materia[1] != 'No asignada' else None

        # Llamar a Crear_Nueva_Materia pero en modo editar
        self.Crear_Nueva_Materia(modo="Editar", nombre_materia=nombre_materia, correo_profesor=correo_profesor)
        
    def actualizar_materia(self, nombre_materia, correo_profesor):
        if not nombre_materia:
            mb.showwarning("Advertencia", "Por favor, ingrese un nombre para la materia.")
            return

        conn = self.conectar_mysql()
        if conn:
            try:
                cursor = conn.cursor()

                # Actualizar la materia
                cursor.execute(
                    "UPDATE materias SET Nombre = %s, idProfesor = %s WHERE Nombre = %s",
                    (nombre_materia, correo_profesor, nombre_materia),
                )

                conn.commit()
                mb.showinfo("Éxito", "Materia actualizada correctamente.")
                self.Ventana_formulario_nueva_materia.destroy()
                self.cargar_materias()
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Error al actualizar la materia: {err}")
            finally:
                conn.close()
