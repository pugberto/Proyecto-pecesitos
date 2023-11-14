import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

from update_animal import Ventana_update_animal
from update_plantas import Ventana_update_plantas


class Ventana_update(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI8()

    def initUI8(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('update')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        self.botonpu = QPushButton(self)
        self.botonpu.setFixedSize(300, 100)  # Establecer tamaño del boton
        self.botonpu.setIcon(QIcon('pescado.png'))  # Ingresa el icono en el boton
        self.botonpu.setIconSize(self.botonpu.size())  # Establece el tamaño del icono del mismo tamaño que el boton
        self.botonpu.setStyleSheet('border: none;')  # Quita los bordes del boton
        self.botonpu.clicked.connect(lambda: self.choosepu(self.botonpu))  # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

        self.botonau = QPushButton(self)
        self.botonau.setFixedSize(300, 100)
        self.botonau.setIcon(QIcon('algas-marinas.png'))
        self.botonau.setIconSize(self.botonau.size())
        self.botonau.setStyleSheet('border: none;')
        self.botonau.clicked.connect(lambda: self.chooseau(self.botonau))

        self.botontu = QPushButton(self)
        self.botontu.setFixedSize(300, 100)
        self.botontu.setIcon(QIcon('algas-marinas.png'))
        self.botontu.setIconSize(self.botontu.size())
        self.botontu.setStyleSheet('border: none;')
        self.botontu.clicked.connect(lambda: self.chooseau(self.botontu))

        botones = QVBoxLayout()
        botones.addWidget(self.botonpu)
        botones.addWidget(self.botonau)
        botones.addWidget(self.botontu)
        botones.setSpacing(0)
        fondo.setLayout(botones)


        self.show()

    def choosepu(self, boton):
        self.transparencia3(boton)
        self.ventana_update = Ventana_update_animal()
        self.ventana_update.show()

    def chooseau(self, boton):
        self.transparencia3(boton)
        self.ventana_insert3 = Ventana_update_plantas()
        self.ventana_insert3.show()

    def transparencia3(self, boton):
        current_stylesheet = boton.styleSheet()
        transparency_value = 0.5
        new_stylesheet = f"{current_stylesheet} background-color: rgba(0, 0, 0, {transparency_value});"
        boton.setStyleSheet(new_stylesheet)

        QTimer.singleShot(50, lambda: self.restaurarColorOriginal3(boton))


    def restaurarColorOriginal3(self, boton):
        # Función para restaurar el color original del botón
        boton.setStyleSheet(f"{boton.styleSheet()} background-color: none;")

