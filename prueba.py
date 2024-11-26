import customtkinter as ctk


class HorarioApp:
    def __init__(self, root):
        root.title("Horario Semanal")
        root.geometry("800x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Título principal
        title = ctk.CTkLabel(
            root,
            text="Horario Semanal",
            font=("Arial", 24, "bold"),
            text_color="blue",
        )
        title.pack(pady=20)

        # Frame para el horario
        horario_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=15)
        horario_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Días y horas
        dias = ["Hora", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horas = [f"{h}:00 - {h + 1}:00" for h in range(6, 9)] + ["9:00 - 10:00 (Descanso)"] + [f"{h}:00 - {h + 1}:00" for h in range(10, 12)]

        # Crear la cuadrícula
        for i, dia in enumerate(dias):
            header = ctk.CTkLabel(
                horario_frame,
                text=dia,
                font=("Arial", 14, "bold"),
                text_color="white",
                fg_color="blue",
                corner_radius=10,
            )
            header.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

        for i, hora in enumerate(horas):
            hora_label = ctk.CTkLabel(
                horario_frame,
                text=hora,
                font=("Arial", 12),
                text_color="black",
                fg_color="#e1e1e1",
                corner_radius=5,
            )
            hora_label.grid(row=i + 1, column=0, sticky="nsew", padx=5, pady=5)

        # Agregar celdas para actividades
        for row in range(1, len(horas) + 1):
            for col in range(1, len(dias)):
                actividad_celda = ctk.CTkLabel(
                    horario_frame,
                    text="",
                    font=("Arial", 12),
                    text_color="black",
                    fg_color="white",
                    corner_radius=5,
                )
                actividad_celda.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Ajustar pesos para distribuir el espacio
        for i in range(len(dias)):
            horario_frame.columnconfigure(i, weight=1)
        for i in range(len(horas) + 1):
            horario_frame.rowconfigure(i, weight=1)


# Crear la aplicación
root = ctk.CTk()
app = HorarioApp(root)
root.mainloop()
