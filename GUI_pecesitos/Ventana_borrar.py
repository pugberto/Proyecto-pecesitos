import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

from borrar_animal import Ventana_borar_animal
from borrar_plantas import Ventana_borar_plantas


class Ventana_borrado(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI6()

    def initUI6(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('borrar')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        self.botonpb = QPushButton(self)
        self.botonpb.setFixedSize(300, 100)  # Establecer tamaño del boton
        self.botonpb.setIcon(QIcon('pescado.png'))  # Ingresa el icono en el boton
        self.botonpb.setIconSize(self.botonpb.size())  # Establece el tamaño del icono del mismo tamaño que el boton
        self.botonpb.setStyleSheet('border: none;')  # Quita los bordes del boton
        self.botonpb.clicked.connect(lambda: self.choosepb(
            self.botonpb))  # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

        self.botonab = QPushButton(self)
        self.botonab.setFixedSize(300, 100)
        self.botonab.setIcon(QIcon('algas-marinas.png'))
        self.botonab.setIconSize(self.botonab.size())
        self.botonab.setStyleSheet('border: none;')
        self.botonab.clicked.connect(lambda: self.chooseab(self.botonab))

        self.botontb = QPushButton(self)
        self.botontb.setFixedSize(300, 100)
        self.botontb.setIcon(QIcon('algas-marinas.png'))
        self.botontb.setIconSize(self.botontb.size())
        self.botontb.setStyleSheet('border: none;')
        self.botontb.clicked.connect(lambda: self.chooseab(self.botontb))

        botones = QVBoxLayout()
        botones.addWidget(self.botonpb)
        botones.addWidget(self.botonab)
        botones.addWidget(self.botontb)
        botones.setSpacing(0)
        fondo.setLayout(botones)


        self.show()

    def choosepb(self, boton):
        self.transparencia2(boton)
        self.ventana_b = Ventana_borar_animal()
        self.ventana_b.show()

    def chooseab(self, boton):
        self.transparencia2(boton)
        self.ventana_insert3 = Ventana_borar_plantas()
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

