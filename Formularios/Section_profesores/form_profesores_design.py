import tkinter as tk
from util.util_imagenes import leer_imagen
from config import COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL
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
        self.frame_tarjetas = CTkFrame(panel_principal, fg_color="white")
        self.frame_tarjetas.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear las tarjetas
        self.crear_tarjetas()

    def crear_tarjetas(self):
        # enumerate = función que recorre los elementos de una lista y devuelve dos valores en cada iteración
        for i, tarjeta in enumerate(datos_tarjetas):  # i = indice de cada interación empezando en 0 y "tarjeta" es el valor de la iteración
            tarjeta_frame = CTkFrame(
                self.frame_tarjetas,
                fg_color="lightgray",
                corner_radius=30,
                height=120,
                width=250,
            )
            tarjeta_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)
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
            
            #ID 
            id_label = CTkLabel(
                texto_frame, text=tarjeta["id"], font=("Arial", 12), text_color="black"
            )
            id_label.pack(pady=1, padx=10)

            # Agregar evento al hacer clic en la tarjeta
            tarjeta_frame.bind(
                "<Button-1>", lambda event, tarjeta=tarjeta: self.mostrar_detalles(tarjeta)
            )

    def mostrar_detalles(self, tarjeta):
        # Limpiar la ventana y mostrar detalles
        for widget in self.frame_tarjetas.winfo_children():
            widget.destroy()

        # Mostrar una nueva ventana con los detalles
        self.ventana_detalles(tarjeta)

    def ventana_detalles(self, tarjeta):
        ventana_detalles = tk.Toplevel(self.frame_tarjetas)
        ventana_detalles.title(f"Detalles de {tarjeta['nombre']}")
        ventana_detalles.geometry("400x300")

        # Mostrar información detallada
        detalle_label = CTkLabel(
            ventana_detalles,
            text=tarjeta["detalle"],
            font=("Arial", 14),
            text_color="black",
        )
        detalle_label.pack(pady=20)

        # Botón para cerrar la ventana de detalles
        boton_cerrar = CTkButton(
            ventana_detalles, text="Cerrar", command=ventana_detalles.destroy
        )
        boton_cerrar.pack(pady=10)
