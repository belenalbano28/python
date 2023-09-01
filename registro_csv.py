from tkinter import *
from tkinter import messagebox
import pandas as pd


# Creamos la ventana que es el contenedor para todos los elementos.

ventana = Tk()
ventana.geometry("500x300")
ventana.title("Registro en csv")

# Creamos una lista vacia con cada uno de los campos a ser exportados a CSV
nombre, apellido, telefono, mail, password = [], [], [], [], []

# validar_telefono, solo admite el ingreso de numeros, no permite ingresar texto.

# Inicio validaciones--------------------------------------------

# validar_nombre: Valida que se introduzcan caracteres.
def validar_nombre():
    nombre = nombre_valor.get()
    if len(nombre) == 0:
        status_nombre.configure(text="Ingresar nombre", bg="red")
        return False
    elif nombre.isdigit():
        status_nombre.configure(text="Solo se admiten letras", bg="red")
        return False
    else:
        status_nombre.configure(text="Correcto", bg="green")
        return True

# validar_apellido: Valida que se introduzcan caracteres.
def validar_apellido():
    apellido = apellido_valor.get()
    if len(apellido) == 0:
        status_apellido.configure(text="Ingresar apellido", bg="red")
        return False
    elif apellido.isdigit():
        status_apellido.configure(text="Solo se admiten letras", bg="red")
        return False
    else:
        status_apellido.configure(text="Correcto", bg="green")
        return True

# validar_telefono: valida que se introduzcan numeros.
def validar_telefono():
    telefono = telefono_valor.get()
    if len(telefono) == 0:
        status_telefono.configure(text="Ingresar telefono", bg="red")
        return False
    elif not telefono.isdigit():
        status_telefono.configure(text="Solo números", bg="red")
        return False
    else:
        status_telefono.configure(text="Correcto",bg="green")
        return True

# validar_mail: valida que se introduzca el correo con '@' y '.'
def validar_mail():
    mail = mail_valor.get()
    if len(mail) == 0:
        status_mail.configure(text="Ingresar mail", bg="red")
        return False
    elif "@" and "." not in mail:
        status_mail.configure(text="Correo inválido, corrija", bg="red")
        return False
    else:
        status_mail.configure(text="Correcto", bg="green")
        return True

# validar_password: valida que se introduzcan al menos 3 caracteres
def validar_password():
    password = password_valor.get()
    if len(password) == 0:
        status_password.configure(text="Ingresar password", bg="red")
        return False
    elif len(password) <= 2:
        status_password.configure(text="Mínimo 3 caracteres",bg="red")
        return False
    else:
        status_password.configure(text="Correcto", bg="green")
        return True

# Fin validaciones--------------------------------------------


# La funcion agregar, toma lo ingresado por el usuario, lo agrega a las listas anteriores, limpia el formulario
# para seguir agregando datos.
def agregar():

    nombre.append(nombre_valor.get())
    apellido.append(apellido_valor.get())
    telefono.append(telefono_valor.get())
    mail.append(mail_valor.get())
    password.append(password_valor.get())

    nombre_valor.delete(0, END)
    apellido_valor.delete(0, END)
    telefono_valor.delete(0, END)
    mail_valor.delete(0, END)
    password_valor.delete(0, END)

    status_nombre.configure(text="...esperando nombre")
    status_apellido.configure(text="...esperando apellido")
    status_telefono.configure(text="...esperando telefono")
    status_mail.configure(text="...esperando mail")
    status_password.configure(text="...esperando password")

# La funcion guardar genera un diccionario con los datos almacenados del formulario, completa los encabezados,
# inserta los datos almacenados en las listas, genera un archivo csv con el nombre obligatorio1 y lo almacena en la
# misma ubicacion en la que se ejecuta el archivo registro_csv.py

def guardar():
    global nombre, apellido, telefono, mail, password
    datos = {'Nombre': nombre, 'Apellido': apellido, 'Telefono': telefono, 'Mail': mail, 'Password': password}
    df = pd.DataFrame(datos, columns=['Nombre', 'Apellido', 'Telefono', 'Mail', 'Password'])
    df.to_csv("obligatorio1.csv")
    messagebox.showinfo(message="Archivo guardado con éxito con el nombre obligatorio1.csv", title="Archivo guardado")

# Elementos del formulario ----------------------------------
# Se crean las etiquetas y los campos de entrada para los 5 elementos del formulario (nombre, apellido, telefono, mail y password)


Label(text="Nombre", width=10, padx=10, pady=10).grid(row=0, column=0)
nombre_valor = Entry(width=20, validatecommand=validar_nombre, validate='focusout')
nombre_valor.grid(row=0, column=1)


Label(text="Apellido", width=10, padx=10, pady=10).grid(row=1, column=0)
apellido_valor = Entry(width=20, validatecommand=validar_apellido, validate='focusout')
apellido_valor.grid(row=1, column=1)

Label(text="Telefono", width=10, padx=10, pady=10).grid(row=2, column=0)
telefono_valor = Entry(width=20, validatecommand=validar_telefono, validate='focusout')
telefono_valor.grid(row=2, column=1)

Label(text="Mail", width=10, padx=10, pady=10).grid(row=3, column=0)
mail_valor = Entry(width=20, validatecommand=validar_mail, validate='focusout')
mail_valor.grid(row=3, column=1)

Label(text="Password", width=10, padx=10, pady=10).grid(row=4, column=0)
password_valor = Entry(show="*", width=20, validatecommand=validar_password, validate='focusout')
password_valor.grid(row=4, column=1)

status_nombre = Label(text="...esperando nombre", width=25, padx=10, pady=10)
status_nombre.grid(row=0, column=3)
status_apellido = Label(text="...esperando apellido", width=25, padx=10, pady=10)
status_apellido.grid(row=1, column=3)
status_telefono = Label(text="...esperando telefono", width=25, padx=10, pady=10)
status_telefono.grid(row=2, column=3)
status_mail = Label(text="...esperando mail", width=25, padx=10, pady=10)
status_mail.grid(row=3, column=3)
status_password = Label(text="...esperando password", width=25, padx=10, pady=10)
status_password.grid(row=4, column=3)



# Los botones agregar y guardar estan explicados en la definicion de sus funciones.

add = Button(text="Agregar", command=agregar)
add.grid(row=5, column=1, rowspan=2)
save = Button(text="Guardar", command=guardar)
save.grid(row=5, column=2, rowspan=2)

# Fin de Elementos del formulario ----------------------------------

# Creamos un mainloop que es el que se encarga de llevar un registro de lo que pasa en la ventana

ventana.mainloop()

