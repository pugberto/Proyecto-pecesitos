import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

from GUI import MiVentana_marina
from insert_pescados import Ventana_insertar_pescado
from planta import Ventana_insertar_planta
from sql import sql


class Ventana_inicial(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI2()

    def initUI2(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('Inicio')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        self.boton_m = QPushButton(self)
        self.boton_m.setFixedSize(300, 100)  # Establecer tamaño del boton
        self.boton_m.setIcon(QIcon('pescado.png'))  # Ingresa el icono en el boton
        self.boton_m.setIconSize(self.boton_m.size())  # Establece el tamaño del icono del mismo tamaño que el boton
        self.boton_m.setStyleSheet('border: none;')  # Quita los bordes del boton
        self.boton_m.clicked.connect(lambda: self.choosep(self.boton_m))  # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

        self.boton_t = QPushButton(self)
        self.boton_t.setFixedSize(300, 100)
        self.boton_t.setIcon(QIcon('algas-marinas.png'))
        self.boton_t.setIconSize(self.boton_t.size())
        self.boton_t.setStyleSheet('border: none;')
        self.boton_t.clicked.connect(lambda: self.choosea(self.boton_t))


        botones = QVBoxLayout()
        botones.addWidget(self.boton_m)
        botones.addWidget(self.boton_t)
        botones.setSpacing(0)
        fondo.setLayout(botones)



        self.show()

    def choose_mar(self, boton):
        miSql = sql("vida_marina")
        self.transparencia2(boton)
        ventana = MiVentana_marina(miSql.resultado[0], miSql.c, miSql.resultados, miSql.nombres_columnas, "vida_marina")
        self.ventana_insert2.show()

    def choose_tanq(self, boton):
        self.transparencia2(boton)
        self.ventana_insert3 = Ventana_insertar_planta()
        self.ventana_insert3.show()

    def transparencia2(self, boton):
        current_stylesheet = boton.styleSheet()
        transparency_value = 0.5
        new_stylesheet = f"{current_stylesheet} background-color: rgba(0, 0, 0, {transparency_value});"
        boton.setStyleSheet(new_stylesheet)

        QTimer.singleShot(50, lambda: self.restaurarColorOriginal2(boton))


    def restaurarColorOriginal2(self, boton):
        # Función para restaurar el color original del botón
        boton.setStyleSheet(f"{boton.styleSheet()} background-color: none;")