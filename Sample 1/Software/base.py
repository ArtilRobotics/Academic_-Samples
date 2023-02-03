import mariadb

from tkinter import *
root = Tk()

try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="incubadora"
    )
    cursor = conexion.cursor()

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos: {error}")


def toDataBase():
    ilumincacion = 00
    alert_max = 80
    alert_min = 50
    try:
        cursor.execute("INSERT INTO datos "
                       "(iluminacion,max,min)"
                       "VALUES (?,?,?)",
                        (ilumincacion,alert_max,alert_min))
        conexion.commit()
    except mariadb.Error as error_registro:
        print(f"Error en el registro: {error}")


boton = Button(root, text="Registrar", width=20, command=toDataBase)
boton.place(x=25, y=10)

mainloop()
