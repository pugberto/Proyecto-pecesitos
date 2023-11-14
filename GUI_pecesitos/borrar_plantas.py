from sql import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

class Ventana_borar_plantas(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI7()

    def initUI7(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('borrar_p')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        layout = QVBoxLayout()

        label_ID = QLabel('Primary key:', self)
        self.line_edit_ID = QLineEdit(self)

        # Botón para realizar alguna acción con los datos ingresados
        boton_procesar = QPushButton('Procesar Datos', self)
        boton_procesar.clicked.connect(self.procesar_datos3)

        layout.addWidget(label_ID)
        layout.addWidget(self.line_edit_ID)
        layout.addWidget(boton_procesar)

        self.setLayout(layout)

    def procesar_datos3(self):
        print("HOLA")
        conexion = mysql.connector.connect(user='root', password='salchipapa12',
                                           host='localhost',
                                           database='proyecto_final',
                                           port='3306')


        mycursor = conexion.cursor()


        t_id = self.line_edit_ID.text()

        try:
            id = int(t_id)

        except ValueError:
            print("Hay un dato erroneo")


        sql_delete = f"DELETE FROM planta WHERE ID_planta = {id}"
        sql_delete2 = f"DELETE FROM vida_marina WHERE ID = {id}"
        mycursor.execute(sql_delete)
        mycursor.execute(sql_delete2)


        conexion.commit()

        mycursor.close()
        conexion.close()