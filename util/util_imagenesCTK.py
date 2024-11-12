from PIL import Image
from customtkinter import CTkImage


def leer_imagen(path, size):
    imagen_pil = Image.open(path)  # Cargar la imagen con PIL
    imagen_pil = imagen_pil.resize(size, Image.ADAPTIVE)  # Redimensionar la imagen
    return CTkImage(
        light_image=imagen_pil, dark_image=imagen_pil
    )  # Convertir a CTkImage
