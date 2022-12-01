import sqlite3

def createDB():
    conn = sqlite3.connect("Colegio.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sqlite3.connect("Alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Alumnos (
            id integer,
            nombre text,
            apellido text
        )"""
    )
    conn.commit()
    cursor.close()
    conn.close()

def insertRow(id,nombre,apellido):
    conn = sqlite3.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Alumnos VALUES ({id},'{nombre}','{apellido}')"
    cursor.execute(instruccion)
    conn.commit()
    cursor.close()
    conn.close()

def readRows():
    conn = sqlite3.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Alumnos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    print(datos)

def readWhere():
    conn = sqlite3.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Alumnos WHERE nombre = 'Roly' "
    cursor.execute(instruccion)
    datos = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    print(datos)



if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow(1,"Carolina","Torres")
    #insertRow(2,"Karen","Yañez")
    #insertRow(3,"Roly","Vivanco")
    #insertRow(4,"Sergio","Duran")
    #insertRow(5,"Ana","Gutierrez")
    #insertRow(6,"Andrea","Cabrera")
    #insertRow(7,"Juan","Muñoz")
    #insertRow(8,"Mauricio","Ugarte")
    #readRows()
    readWhere()