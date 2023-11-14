from sql import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QMessageBox
from PyQt5.QtGui import QColor, QIcon

from tabla_consulta import VentanaConsulta


class Ventana_consulta_chars(QWidget):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.initUI9()


    def initUI9(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('update_p')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        layout = QVBoxLayout()

        label_ID = QLabel('dato:', self)
        self.line_edit_ID = QLineEdit(self)

        # Botón para realizar alguna acción con los datos ingresados
        boton_procesar = QPushButton('Procesar Datos', self)
        boton_procesar.clicked.connect(self.hacer_consulta)

        layout.addWidget(label_ID)
        layout.addWidget(self.line_edit_ID)
        layout.addWidget(boton_procesar)

        self.setLayout(layout)

    def hacer_consulta(self):
        conexion = mysql.connector.connect(user='root', password='salchipapa12',
                                           host='localhost',
                                           database='proyecto_final',
                                           port='3306')


        mycursor = conexion.cursor()

        t_id = self.line_edit_ID.text()

        print(t_id)
        print(self.id)

        consulta = f"SELECT * FROM vida_marina WHERE {self.id} = %s;"
        mycursor.execute(consulta, (t_id,))

        resultados = mycursor.fetchall()

        self.ventana_consulta = VentanaConsulta(resultados)
        self.ventana_consulta.show()


