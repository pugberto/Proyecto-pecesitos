from sql import *
from GUI import *

if __name__ == '__main__':
    miSql = sql("vida_marina")

    app = QApplication(sys.argv)
    ventana = MiVentana_marina(miSql.resultado[0], miSql.c, miSql.resultados, miSql.nombres_columnas, "vida_marina")
    sys.exit(app.exec_())



"""
#sql = "INSERT INTO acuario (Numero_RUT, Coste_mantenimento) VALUES (%s, %s)"
    #val = ("12345678", 12.5)
    #mycursor.execute(sql, val)

    #sql = "INSERT INTO tanque (Numero_tanque, Numero_RUT, Habitat, Tamano) VALUES (%s, %s, %s, %s)"
    #val = (0, "12345678", "Dulce", "Pequeño")
    #mycursor.execute(sql, val)

    sql = "INSERT INTO vida_marina (ID, Numero_tanque, Habitat, Alimento, Tipo_vida_marina) VALUES (%s, %s, %s, %s, %s)"
    val = (2, 1, "Salada", "N/A", "Planta")
    mycursor.execute(sql, val)

    sql = "INSERT INTO planta (ID_planta, funcion) VALUES (%s, %s)"
    val = (2, "Decoración")

    mycursor.execute(sql, val)

    conexion.commit()

    print(mycursor.lastrowid, "record inserted.")


"""










