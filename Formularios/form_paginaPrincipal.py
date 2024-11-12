import tkinter as tk
from tkinter import font
from config import (
    COLOR_BARRA_SUPERIOR,
    COLOR_MENU_LATERAL,
    COLOR_CUERPO_PRINCIPAL,
    COLOR_MENU_CURSOR_ENCIMA,
    COLOR_FONT_PURPLE,
    COLOR_FONT_BLACK,
    COLOR_FONT_WHITE,
)
import util.util_ventana as util_window
import util.util_imagenes as util_img
from Formularios.form_usuarios_design import FormularioUsuariosDesign
from Formularios.Section_profesores.form_profesores_design import (
    FormularioProfesoresDesign,
)


class formulario(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./Assets/colegio.png", (560, 136))
        self.perfil = util_img.leer_imagen("./Assets/mujer.png", (100, 100))
        self.user = util_img.leer_imagen("./Assets/usuario.png", (30, 30))
        self.menu = util_img.leer_imagen("./Assets/menu.png", (26, 26))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()

    def config_window(self):
        # configuración inicial de la ventana
        self.title("GIE")
        self.iconbitmap("./Assets/colegio.ico")
        w, h = 1024, 600
        util_window.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50
        )  # el 50 no es altura, si no cuantos caracteres pueden caber
        self.barra_superior.pack(side=tk.TOP, fill="both")

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=200)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

    def controles_barra_superior(self):
        # configuración de la barra superior
        font_awesome = font.Font(family="FontAwesome", size=12)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(
            self.barra_superior,
            image=self.menu,
            command=self.toggle_panel,
            bd=0,
            bg=COLOR_BARRA_SUPERIOR,
            fg="white",
        )
        self.buttonMenuLateral.pack(side=tk.LEFT, padx=10)

        self.labelTitulo = tk.Label(self.barra_superior, text="Proyecto GIE")
        self.labelTitulo.config(
            fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=12
        )
        self.labelTitulo.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelUser = tk.Label(self.barra_superior, image=self.user)
        self.labelUser.config(background=COLOR_BARRA_SUPERIOR, width=20)
        self.labelUser.pack(side=tk.RIGHT, padx=20)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 15
        alto_menu = 2
        font_awesome = font.Font(family="JasmineUPC", size=15)

        self.frameEspacioSuperior = tk.Frame(
            self.menu_lateral, height=30, bg=COLOR_MENU_LATERAL
        )
        self.frameEspacioSuperior.pack(side=tk.TOP, fill=tk.X)

        self.buttonUsuarios = tk.Button(self.menu_lateral)
        self.buttonProfesores = tk.Button(self.menu_lateral)
        self.buttonHorarios = tk.Button(self.menu_lateral)
        self.buttonMatriculas = tk.Button(self.menu_lateral)
        self.buttonEstudiantes = tk.Button(self.menu_lateral)
        self.buttonMaterias = tk.Button(self.menu_lateral)
        self.buttonCerrar_Sesion = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Usuarios", self.buttonUsuarios, self.abrir_seccion_usuarios),
            ("Profesores", self.buttonProfesores, self.abrir_seccion_profesores),
            ("Horarios", self.buttonHorarios, self.abrir_seccion_usuarios),
            ("Matriculas", self.buttonMatriculas, self.abrir_seccion_usuarios),
            ("Estudiantes", self.buttonEstudiantes, self.abrir_seccion_usuarios),
            ("Materias", self.buttonMaterias, self.abrir_seccion_usuarios),
        ]

        for text, button, comando in buttons_info:
            self.configurar_boton_menu(
                button, text, font_awesome, ancho_menu, alto_menu, comando
            )

        # Configurar el botón "Cerrar sesión" con los mismos estilos que los demás botones
        self.configurar_boton_menu(
            self.buttonCerrar_Sesion,
            "Cerrar sesión",
            font_awesome,
            ancho_menu,
            alto_menu,
            comando,
        )
        # Se empaqueta el boton "Cerrar sesión" al final
        self.buttonCerrar_Sesion.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=(10, 0))
        # Asociar los eventos de hover con el botón "Cerrar sesión"
        self.bind_hover_events(self.buttonCerrar_Sesion)

    def configurar_boton_menu(
        self, button, text, font_awesome, ancho_menu, alto_menu, comando
    ):
        button.config(
            text=f"  {text}",
            anchor="w",
            font=font_awesome,
            bd=0,
            bg=COLOR_MENU_LATERAL,
            fg=COLOR_FONT_WHITE,
            width=ancho_menu,
            height=alto_menu,
            command=comando,
        )
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_BARRA_SUPERIOR, fg=COLOR_FONT_WHITE)

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg=COLOR_FONT_WHITE)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill="y")

    def abrir_seccion_usuarios(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioUsuariosDesign(self.cuerpo_principal)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrir_seccion_profesores(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioProfesoresDesign(self.cuerpo_principal)
