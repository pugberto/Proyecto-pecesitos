import mysql.connector

class sql():
    def __init__(self, name_tabla):
        super().__init__()
        self.conexion = mysql.connector.connect(user='root', password='salchipapa12',
                                           host='localhost',
                                           database='proyecto_final',
                                           port='3306')
        self.mycursor = self.conexion.cursor()

        self.name = name_tabla

        self.consultas()

    def consultas(self):
        consulta_filas = f"SELECT COUNT(*) FROM {self.name}"

        consulta_Columnas = f"DESCRIBE {self.name}"

        self.mycursor.execute(consulta_filas)

        self.resultado = self.mycursor.fetchone()

        self.mycursor.execute(consulta_Columnas)

        f = self.mycursor.fetchall()

        self.nombres_columnas = [fila[0] for fila in f]

        self.c = len(f)

        consulta_info_vida = f"SELECT * FROM {self.name}"

        self.mycursor.execute(consulta_info_vida)

        self.resultados = self.mycursor.fetchall()

    def cerrar_conexion(self):
        self.mycursor.close()
        self.conexion.close()
