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

    # ///////////////////// CREAR NUEVO USUARIO //////////////////////
    def Crear_Nuevo_Usuario(self, modo="Nuevo "):
        self.Ventana_formulario_nuevo_usuario = tk.Toplevel()
        self.Ventana_formulario_nuevo_usuario.title(modo.capitalize() + "usuario")
        self.Ventana_formulario_nuevo_usuario.geometry("300x480+980+280")
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
        )
        self.btn_agregar.grid(row=0, column=1, padx=10)

    def Editar_Usuario(self):
        # Llamar a Crear_Nuevo_Usuario pero en modo editar
        self.Crear_Nuevo_Usuario(modo="Editar ")
