import tkinter as tk
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
COLOR_TEXTO = "#000"


class FormularioMateriasDesign:

    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, background="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        icon = tk.PhotoImage(file="./Assets/boton-agregar.png")

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
            image=icon,
            compound="left",
            command=self.Editar_Usuario,
        )
        self.Btn_EditarMateria.image = icon
        self.Btn_EditarMateria.pack(side=tk.LEFT, padx=10, pady=10)

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
            command=self.Crear_Nuevo_Usuario,
        )
        self.Btn_NuevaMateria.image = icon
        self.Btn_NuevaMateria.pack(side=tk.RIGHT, padx=10, pady=10)

    # ///////////////////// CREAR NUEVA MATERIA //////////////////////
    def Crear_Nuevo_Usuario(self, modo="Nueva "):
        self.Ventana_formulario_nuevo_usuario = tk.Toplevel()
        self.Ventana_formulario_nuevo_usuario.title(modo.capitalize() + "usuario")
        self.Ventana_formulario_nuevo_usuario.geometry("300x490+980+280")
        self.Ventana_formulario_nuevo_usuario.configure(bg="white")

        # Eliminar la barra de título y los controles de la ventana
        self.Ventana_formulario_nuevo_usuario.overrideredirect(True)

        # Encabezado de la ventana
        self.frame_titulo = CTkFrame(
            self.Ventana_formulario_nuevo_usuario, fg_color=COLOR_BORDE_ENTRADA
        )
        self.frame_titulo.pack(fill="x", pady=10)
        self.Titulo_pagina = CTkLabel(
            self.frame_titulo, text=modo.capitalize() + "Materia", font=("Arial", 20)
        )
        self.Titulo_pagina.pack(pady=10)

        # Campo Nombre de Materia
        self.label_nombre = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Nombre de materia:",
            text_color=COLOR_TEXTO,
            font=("Arial", 16, "bold"),
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
        self.label_Grados_pertenecientes = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Grados a los que pertenece:",
            text_color=COLOR_TEXTO,
            font=("Arial", 16, "bold"),
        )
        self.label_Grados_pertenecientes.pack(anchor="w", padx=20)
        
        # Crear un frame para los checkboxes
        frame_checkboxes = CTkFrame(self.Ventana_formulario_nuevo_usuario, fg_color="white")
        frame_checkboxes.pack(padx=10, pady=10, fill="both")  # Empaqueta el frame principal

        # Variables para los checkboxes
        Grado1 = tk.BooleanVar()
        Grado2 = tk.BooleanVar()
        Grado3 = tk.BooleanVar()
        Grado4 = tk.BooleanVar()
        Grado5 = tk.BooleanVar()

        # Lista de tuplas con texto y variable asociada
        grados = [
            ("Grado 1", Grado1),
            ("Grado 2", Grado2),
            ("Grado 3", Grado3),
            ("Grado 4", Grado4),
            ("Grado 5", Grado5),
        ]

        # Distribuir los checkboxes en dos columnas
        for i, (texto, variable) in enumerate(grados):
            chk = CTkCheckBox(
                frame_checkboxes,
                text=texto,
                variable=variable,
                fg_color=COLOR_BOTON_AGREGAR,  # Color del botón cuando está activado
                hover_color=COLOR_BORDE_ENTRADA,  # Color cuando el mouse pasa por encima
                text_color=COLOR_TEXTO,  # Color del texto
                border_color=COLOR_BORDE_ENTRADA,  # Color del borde
                checkmark_color=COLOR_CUERPO_PRINCIPAL,  # Color del check interno
            )
            chk.grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="w")  # Distribución en dos columnas

        # Campo Cargo (opciones desplegables)
        self.label_profesor_encargado= CTkLabel(
            self.Ventana_formulario_nuevo_usuario, text="ID profesor encargado de la materia:", text_color=COLOR_TEXTO
        )
        self.label_profesor_encargado.pack(anchor="w", padx=20)
        self.option_profesor_encargado = CTkOptionMenu(
            self.Ventana_formulario_nuevo_usuario,
            values=["01", "02", "03"],
            width=250,
            fg_color="white",
            button_color="white",
            button_hover_color=COLOR_BOTON_AGREGAR,
            dropdown_fg_color="white",
            dropdown_hover_color=COLOR_FONDO_TITULO,
            text_color=COLOR_TEXTO,
            dropdown_text_color=COLOR_TEXTO,
        )
        self.option_profesor_encargado.pack(pady=5)

        # Campo Teléfono
        self.label_Nombre_profesor = CTkLabel(
            self.Ventana_formulario_nuevo_usuario,
            text="Nombre profesor:",
            text_color=COLOR_TEXTO,
        )
        self.label_Nombre_profesor.pack(anchor="w", padx=20)
        self.entry_Nombre_profesor = CTkEntry(
            self.Ventana_formulario_nuevo_usuario,
            width=250,
            border_color=COLOR_BORDE_ENTRADA,
            fg_color="white",
            text_color=COLOR_TEXTO,
        )
        self.entry_Nombre_profesor.pack(pady=5)
        self.entry_Nombre_profesor.configure(state="disabled")

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
        )
        self.btn_agregar.grid(row=0, column=1, padx=10)

    def Editar_Usuario(self):
        # Llamar a Crear_Nuevo_Usuario pero en modo editar
        self.Crear_Nuevo_Usuario(modo="Editar ")