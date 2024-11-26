from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import PhotoImage
import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector 
import subprocess


class Login:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("400x600")
        self.root.title("Inicio de sesión")
        self.root.resizable(False, False)

        # Ajustar ventana al centro
        self.anchov = 400
        self.altov = 600
        # Halla el tamaño de la ventana
        self.anchop = self.root.winfo_screenwidth()
        self.altop = self.root.winfo_screenheight()

        #
        self.puntoX = (self.anchop // 2) - (self.anchov // 2)
        self.puntoY = (self.altop // 2) - (self.altov // 2)

        # Posicion de la ventana
        self.root.geometry(f"{self.anchov}x{self.altov}+{self.puntoX}+{self.puntoY}")

        # Apariencia de la ventana
        self.root._set_appearance_mode("light")

        # importaciones
        logo = PhotoImage(file="Assets/usuario (3).png")
        Morado = "#9735C7"

        # Configuracr el grid del root
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Crear el frame
        self.frame = CTkFrame(self.root, fg_color="white")
        self.frame.grid(
            column=0, row=0, sticky="nsew"
        )  # sticky permite que se expanda de todos los lados cuando se agranda la pantalla
        self.frame.columnconfigure(0, weight=1)

        # imagen
        CTkLabel(self.frame, image=logo, text="").grid(
            columnspan=2, row=0, pady=(10, 10)
        )

        self.LbUser = CTkLabel(
            self.frame,
            font=("JasmineUPC", 16, "bold"),
            text_color="Black",
            text="Usuario:",
        ).grid(columnspan=1, row=1, sticky="w", padx=90, pady=(0, 0))
        self.Uusuario= tk.StringVar()
        self.Usuario = CTkEntry(
            self.frame,
            font=(
                "sans serif",
                16,
            ),
            text_color="black",
            border_color=Morado,
            fg_color="white",
            width=220,
            height=40,
            textvariable=self.Uusuario
        )
        self.Usuario.grid(columnspan=2, row=2, padx=4, pady=(0, 10))

        self.Lbcontraseña = CTkLabel(
            self.frame,
            font=("JasmineUPC", 16, "bold"),
            text_color="Black",
            text="Contraseña:",
        ).grid(columnspan=1, row=3, sticky="w", padx=90, pady=(10, 0))
        self.psswd= tk.StringVar()
        self.Contraseña = CTkEntry(
            self.frame,
            show="*",
            font=("sans serif", 16),
            text_color="black",
            border_color=Morado,
            fg_color="white",
            width=220,
            height=40,
            textvariable=self.psswd
        )
        self.Contraseña.grid(columnspan=2, row=4, padx=4, pady=(0, 10))
        self.seleccion = tk.IntVar()
        self.VerContraseña = CTkCheckBox(
            self.frame,
            text="Mostrar contraseña",
            font=("JasmineUPC", 12),
            text_color="Black",
            checkbox_width=20,
            checkbox_height=20,
            corner_radius=100,
            variable=self.seleccion,
            hover_color=Morado,
            border_color=Morado,
            fg_color=Morado,
            command=self.Mostrar_contraseña,
        ).grid(columnspan=2, row=5)

        self.btn_ingresar = CTkButton(
            self.frame,
            text="Iniciar Sesión",
            font=("JasmineUPC", 16),
            border_color=Morado,
            fg_color=Morado,
            hover_color=Morado,
            corner_radius=12,
            border_width=2,
            height=40,
            width=200,
            command=self.validardatos
        )
        self.btn_ingresar.grid(columnspan=2, row=6, padx=6, pady=(10, 0))

        self.root.mainloop()
        
    def VentanaAdmin(self):
        subprocess.Popen(['python','main.py'])
    def validardatos(self):
        #Obtener valores ingresados
        usuario= self.Uusuario.get()
        contraseña= self.psswd.get()
        #Conectar a la base de datos
        try:
            conn= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='giebd'
                )
                
            cursor= conn.cursor()
                
                # Consulta SQL para obtener el nombre de usuario y la contraseña almacenada (encriptada)
            query = "SELECT Nombreusuario, Contraseña, Rol FROM usuarios WHERE Nombreusuario = %s"
            cursor.execute(query, (usuario,))
                #buscar el usuario en la base de datos
            user= cursor.fetchone()
            
            #Verificar si el usuario exite
            if user:
                stored_username= user[0]
                stored_password= user[1] #Para contraseñas en texto plano
                rol= user[2]
                
                #comprobar las contraseñas(sin cifrado)
                if usuario == stored_username and contraseña == stored_password:
                    mb.showinfo('Login exitoso',f'Bienvenido {usuario}')
                    if rol == 'Administrativo':
                        self.VentanaAdmin()
                        self.root.quit()
                        self.root.destroy()
                else:
                    mb.showerror('Error de inicio de sesión', 'Contraseña o Usuario incorrecto')
            else:
                mb.showerror('Error de inicio de sesión', 'Usuario no existente')
                
        except mysql.connector.Error as error:
            mb.showerror('Error de conexión', f'Error al conectar con la base de datos: {error}')
            
        finally:
            if conn:
                conn.close()   
                

    def Mostrar_contraseña(self):
        if self.Contraseña.get() != "":
            if self.seleccion.get() == 1:
                self.Contraseña.configure(show="")
            else:
                self.Contraseña.configure(show="*")


Login()
