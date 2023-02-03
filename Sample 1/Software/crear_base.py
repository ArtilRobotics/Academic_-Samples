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


def crear_tabla():
    try:
        cursor.execute("CREATE TABLE datos(id INT NOT NULL AUTO_INCREMENT,"
                       "iluminacion VARCHAR(8) NOT NULL,"
                       "max VARCHAR(8) NOT NULL,"
                       "min VARCHAR(8) NOT NULL,PRIMARY KEY (id))")
        conexion.commit()
    except mariadb.Error as error:
        print(f"Error al crear la tabla: {error}")


boton = Button(root, text="Crear Tabla", width=20, command=crear_tabla)
boton.place(x=25, y=10)

mainloop()
