from tkinter import Tk, Label,ttk, messagebox
from tkinter import *
import sqlite3, subprocess
class Inicio:
    db = "Database/almacen.db" 
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Login con TKinter")
        frame = LabelFrame(self.ventana, text = "Acceso a usuarios.")
        frame.config(padx=10, pady=10) 
        frame.grid(row = 1, column = 0, columnspan = 2, padx=20,pady = 20)
        ########## Controles del frame ########
        self.etiqueta_nombre = Label(frame, text="Nombre: ",  font=("Helvetica", 12, "bold")) # Texto en negrita.
        self.etiqueta_nombre.grid(row=1, column=0)                  # Entry Nombre (caja de texto que recibira el nombre) 
        self.inputBox_nombre = Entry(frame, fg="blue", justify="center")     # Caja de texto (input de texto) ubicada en el frame 
        self.inputBox_nombre.focus()                                         # foco a este Entry al cargar 
        self.inputBox_nombre.grid(row=1, column=1)                           # indica la cuadrícula de espacio
        self.etiqueta_pass = Label(frame, text="Contraseña:", font=("Helvetica", 12, "bold"))  # Label de Contraseña. 
        self.etiqueta_pass.grid(row=2, column=0)                    # Posicionado de contraseña
        self.inputBox_passw = Entry(frame, show="*",fg="blue", justify="center")  # Entry passw
        self.inputBox_passw.grid(row=2,column=1)                             # Posición del entry
        self.buttonEdit = ttk.Button(frame, text="Entrar", command=self.comprobarAcceso) #botón de ENTRAR llama a la función comprobar
        self.buttonEdit.grid(row=5, columnspan=2, sticky=W+E)       # Colocación del boton de confirmar.

    def validacionName(self):                                   #Comprueba que el nombre esté rellenado
        nombre_introducido_user = self.inputBox_nombre.get()
        return len(nombre_introducido_user) !=0
    def validacionPassw(self):                                   #Comprueba que el Passw esté rellenado
        passw_user = self.inputBox_passw.get()
        return len(passw_user) !=0
    def comprobarAcceso(self):
        if self.validacionName() and self.validacionPassw():
            query ="select Nombre, passW from usuarios where Nombre =(?, ?)"
            self.comprobarUserReg()
        elif self.validacionName() and self.validacionPassw()==False:
            messagebox.showwarning(message="¡Tienes que introducir la contraseña!", title="¡Contraseña obligatoria!")
        elif self.validacionName()==False and self.validacionPassw():
            messagebox.showwarning(message="¡Tienes que escribir un nombre de usuario!", title="¡Nombre Obligatorio!")
        elif self.validacionName()==False and self.validacionPassw()==False:
            messagebox.showwarning(message="!Los campos no pueden estar vacios!", title="¡Campos vacios!") 

    def comprobarUserReg(self):
        if self.validacionName() and self.validacionPassw():
            user = self.inputBox_nombre.get()
            Passw=self.inputBox_passw.get()
            con = sqlite3.connect("Database/almacen.db")
            cur = con.cursor()
            statement = "select Nombre, passW from usuarios"
            queries_user = f"SELECT Nombre, passW from usuarios WHERE Nombre='{user}' AND passW = '{Passw}';"
            cur.execute(queries_user)
            if not cur.fetchone():  # Comprobación de que el usuario existe.
                messagebox.showerror("ERROR!", "El usuario o contraseña no existen!")
            else:
                messagebox.showinfo("BIENVENIDO", "Bienvenido a GESINPY, {}".format(user))
                subprocess.Popen("bienvenida.py", shell=True)
                ventana.destroy()



if __name__ == '__main__':
    ventana = Tk()            # Instancia de tkinter para generar más objetos de escritorio.
    app = Inicio(ventana)
    ventana.mainloop()        # Ejecuta el bucle de inicio (muestra ventana)
    


