import tkinter as tk
import customtkinter as ctk

class FormEstudiantesDesign:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Formulario Estudiantes")
        
        # Datos de ejemplo (en un caso real estarían en una base de datos o archivo)
        self.estudiantes_data = {
            "nombre": "Juan Pérez",
            "cedula": "123456789",
            "direccion": "Calle Ficticia 123",
            "telefono": "987654321"
        }

        # Crear el formulario de estudiantes
        self.create_estudiantes_form()
        
    def create_estudiantes_form(self):
        # Frame de la barra superior
        top_frame = tk.Frame(self.root, bg="#4A4A4A", height=50)
        top_frame.pack(fill="x")
        
        # Título de la barra
        title_label = ctk.CTkLabel(top_frame, text="Formulario Estudiantes", font=("Arial", 20, "bold"), text_color="white")
        title_label.pack(side="left", padx=10)
        
        # Botón de editar
        edit_button = ctk.CTkButton(top_frame, text="Editar", command=self.open_matricula_form)
        edit_button.pack(side="right", padx=20)

        # Frame para mostrar los datos del estudiante
        self.frame_estudiantes = tk.Frame(self.root, bg="white", padx=10, pady=10)
        self.frame_estudiantes.pack(fill="both", expand=True)
        
        # Etiquetas con los datos del estudiante
        self.nombre_label = ctk.CTkLabel(self.frame_estudiantes, text=f"Nombre: {self.estudiantes_data['nombre']}")
        self.nombre_label.pack(pady=5)

        self.cedula_label = ctk.CTkLabel(self.frame_estudiantes, text=f"Cédula: {self.estudiantes_data['cedula']}")
        self.cedula_label.pack(pady=5)

        self.direccion_label = ctk.CTkLabel(self.frame_estudiantes, text=f"Dirección: {self.estudiantes_data['direccion']}")
        self.direccion_label.pack(pady=5)

        self.telefono_label = ctk.CTkLabel(self.frame_estudiantes, text=f"Teléfono: {self.estudiantes_data['telefono']}")
        self.telefono_label.pack(pady=5)

    def open_matricula_form(self):
        # Crear el formulario de matrícula y prellenar los campos con los datos del estudiante
        matricula_window = tk.Toplevel(self.root)
        matricula_window.geometry("400x400")
        matricula_window.title("Formulario Matrícula")
        
        # Variables para los campos del formulario de matrícula
        self.nombre_var = tk.StringVar(value=self.estudiantes_data['nombre'])
        self.cedula_var = tk.StringVar(value=self.estudiantes_data['cedula'])
        self.direccion_var = tk.StringVar(value=self.estudiantes_data['direccion'])
        self.telefono_var = tk.StringVar(value=self.estudiantes_data['telefono'])
        
        # Crear formulario de matrícula
        tk.Label(matricula_window, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(matricula_window, textvariable=self.nombre_var)
        self.nombre_entry.pack(pady=5)

        tk.Label(matricula_window, text="Cédula:").pack(pady=5)
        self.cedula_entry = tk.Entry(matricula_window, textvariable=self.cedula_var)
        self.cedula_entry.pack(pady=5)

        tk.Label(matricula_window, text="Dirección:").pack(pady=5)
        self.direccion_entry = tk.Entry(matricula_window, textvariable=self.direccion_var)
        self.direccion_entry.pack(pady=5)

        tk.Label(matricula_window, text="Teléfono:").pack(pady=5)
        self.telefono_entry = tk.Entry(matricula_window, textvariable=self.telefono_var)
        self.telefono_entry.pack(pady=5)

        # Botón para guardar los cambios
        save_button = tk.Button(matricula_window, text="Guardar", command=self.save_changes)
        save_button.pack(pady=20)

    def save_changes(self):
        # Guardar los cambios (en este ejemplo solo actualizamos el diccionario)
        self.estudiantes_data['nombre'] = self.nombre_var.get()
        self.estudiantes_data['cedula'] = self.cedula_var.get()
        self.estudiantes_data['direccion'] = self.direccion_var.get()
        self.estudiantes_data['telefono'] = self.telefono_var.get()

        # Actualizar las etiquetas en el formulario de estudiantes
        self.nombre_label.config(text=f"Nombre: {self.estudiantes_data['nombre']}")
        self.cedula_label.config(text=f"Cédula: {self.estudiantes_data['cedula']}")
        self.direccion_label.config(text=f"Dirección: {self.estudiantes_data['direccion']}")
        self.telefono_label.config(text=f"Teléfono: {self.estudiantes_data['telefono']}")

        # Cerrar el formulario de matrícula
        for widget in self.root.winfo_children():
            widget.update()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FormEstudiantesDesign(root)
    root.mainloop()
