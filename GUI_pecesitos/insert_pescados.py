from sql import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

class Ventana_insertar_pescado(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI3()

    def initUI3(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('insertar_pez')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        layout = QVBoxLayout()

        label_ID = QLabel('ID:', self)
        self.line_edit_ID = QLineEdit(self)

        label_tanque = QLabel('num_tanque:', self)
        self.line_edit_tanque = QLineEdit(self)

        label_habitad = QLabel('Habitad:', self)
        self.line_edit_habitad = QLineEdit(self)

        label_alimento = QLabel('Alimento:', self)
        self.line_edit_alimento = QLineEdit(self)

        label_comportamiento = QLabel('Comportamiento:', self)
        self.line_edit_comportamiento = QLineEdit(self)

        # Botón para realizar alguna acción con los datos ingresados
        boton_procesar = QPushButton('Procesar Datos', self)
        boton_procesar.clicked.connect(self.procesar_datos)

        layout.addWidget(label_ID)
        layout.addWidget(self.line_edit_ID)
        layout.addWidget(label_tanque)
        layout.addWidget(self.line_edit_tanque)
        layout.addWidget(label_habitad)
        layout.addWidget(self.line_edit_habitad)
        layout.addWidget(label_alimento)
        layout.addWidget(self.line_edit_alimento)
        layout.addWidget(label_comportamiento)
        layout.addWidget(self.line_edit_comportamiento)
        layout.addWidget(boton_procesar)

        self.setLayout(layout)

    def procesar_datos(self):
        conexion = mysql.connector.connect(user='root', password='salchipapa12',
                                           host='localhost',
                                           database='proyecto_final',
                                           port='3306')

        mycursor = conexion.cursor()





        t_id = self.line_edit_ID.text()
        t_tanque = self.line_edit_tanque.text()
        t_habitad = self.line_edit_habitad.text()
        t_alimento = self.line_edit_alimento.text()
        t_comp = self.line_edit_comportamiento.text()

        try:
            id = int(t_id)
            tanque = int(t_tanque)

        except ValueError:
            print("Hay un dato erroneo")

        sql = "INSERT INTO vida_marina (ID, Numero_tanque, Habitat, Alimento, Tipo_vida_marina) VALUES (%s, %s, %s, %s, %s)"
        val = (id, tanque, t_habitad, t_alimento, "Animal")
        mycursor.execute(sql, val)

        sql = "INSERT INTO animal (ID_animal, Comportamiento) VALUES (%s, %s)"
        val = (id, t_comp)

        mycursor.execute(sql, val)

        conexion.commit()

        mycursor.close()
        conexion.close()

