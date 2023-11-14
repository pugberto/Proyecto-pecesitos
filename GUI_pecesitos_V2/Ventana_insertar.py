import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

from insert_pescados import Ventana_insertar_pescado
from planta import Ventana_insertar_planta


class Ventana_insertar(QWidget):
    def __init__(self, nombre_tabla):
        super().__init__()

        self.nombre = nombre_tabla
        self.initUI2()

    def initUI2(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('insertar')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")






        if(self.nombre == "vida_marina"):
            self.botonp = QPushButton(self)
            self.botonp.setFixedSize(300, 100)  # Establecer tamaño del boton
            self.botonp.setIcon(QIcon('pescado.png'))  # Ingresa el icono en el boton
            self.botonp.setIconSize(self.botonp.size())  # Establece el tamaño del icono del mismo tamaño que el boton
            self.botonp.setStyleSheet('border: none;')  # Quita los bordes del boton
            self.botonp.clicked.connect(lambda: self.choosep(self.botonp))  # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

            self.botona = QPushButton(self)
            self.botona.setFixedSize(300, 100)
            self.botona.setIcon(QIcon('algas-marinas.png'))
            self.botona.setIconSize(self.botona.size())
            self.botona.setStyleSheet('border: none;')
            self.botona.clicked.connect(lambda: self.choosea(self.botona))


            botones = QVBoxLayout()
            botones.addWidget(self.botonp)
            botones.addWidget(self.botona)
            botones.setSpacing(0)
            fondo.setLayout(botones)


        if(self.nombre == "tanque"):
            layout = QVBoxLayout()

            # Contenido de la segunda ventana
            etiqueta = QLabel('Esta es la segunda ventana', self)

            layout.addWidget(etiqueta)
            self.setLayout(layout)

        self.show()

    def choosep(self, boton):
        self.transparencia2(boton)
        self.ventana_insert2 = Ventana_insertar_pescado()
        self.ventana_insert2.show()

    def choosea(self, boton):
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

