from Ventana_borrar import *
from Ventana_consulta import Ventana_consulta
from Ventana_insertar import *
from Ventana_update import Ventana_update
from borrar_animal import *
from sql import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QColor, QIcon


class MiVentana_marina(QWidget):
    def __init__(self, f, c, tabla, nom_colums, nombre_tabla):
        super().__init__()

        self.f = f
        self.c = c
        self.tabla = tabla
        self.nom_colums = nom_colums
        self.nom_tabla = nombre_tabla

        self.initUI()

    def initUI(self):
        aux = 0
        aux2 = 0
        self.setGeometry(300, 50, 900, 600)
        self.setWindowTitle('Pecesitos')

#------------------ETIQUETAS------------------------------------------------------------------
    #FONDO
        layout_principal = QHBoxLayout()

    #FONDO DE LA TABLA
        f_tabla = QLabel(self) # etiqueta a la derecha
        color_tabla_fondo = QColor(173, 216, 230)
        f_tabla.setGeometry(350, 0, 550, 600)
        f_tabla.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

    #FONDO DE LOS BOTONES:
        f_botones = QLabel(self)  # etiqueta a la izquierda
        f_botones.setGeometry(0, 0, 350, 600)
        color_etiqueta_fondo = QColor(224, 255, 255)  # Color de fondo de la etiqueta
        f_botones.setStyleSheet(f"background-color: {color_etiqueta_fondo.name()};")


        layout_principal.addWidget(f_botones)
        layout_principal.addWidget(f_tabla)


#------------------TABLA----------------------------------------------------------------------------------------------
        tabla = QTableWidget(self)
        tabla.setRowCount(self.f)
        tabla.setColumnCount(self.c)

        for i in range(tabla.rowCount()):
            for j in range(tabla.columnCount()):
                item = QTableWidgetItem(f"{self.tabla[aux][aux2]}")
                aux2 += 1
                tabla.setItem(i, j, item)
            aux2 = 0
            aux += 1

        tabla.setHorizontalHeaderLabels(self.nom_colums)

        tabla.verticalHeader().setVisible(False)

        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout_horizontal = QHBoxLayout(self)

        layout_horizontal.addItem(spacer)
        layout_horizontal.addWidget(tabla)

        self.setLayout(layout_horizontal)

        # ---------------------------------BOTONES------------------------------------------------------------------------------------


        #-------INSERTAR---------------
        self.boton1 = QPushButton(self)
        self.boton1.setFixedSize(300, 100)  # Establecer tamaño del boton
        self.boton1.setIcon(QIcon('insert.png')) # Ingresa el icono en el boton
        self.boton1.setIconSize(self.boton1.size()) # Establece el tamaño del icono del mismo tamaño que el boton
        self.boton1.setStyleSheet('border: none;') # Quita los bordes del boton
        self.boton1.clicked.connect(lambda: self.insertar_boton(self.boton1)) # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

        # -------BORRAR---------------
        self.boton2 = QPushButton(self)
        self.boton2.setFixedSize(300, 100)
        self.boton2.setIcon(QIcon('DELETE.png'))
        self.boton2.setIconSize(self.boton2.size())
        self.boton2.setStyleSheet('border: none;')
        self.boton2.clicked.connect(lambda: self.borrar_boton(self.boton2))

        # -------UPDATE---------------
        self.boton3 = QPushButton(self)
        self.boton3.setFixedSize(300, 100)
        self.boton3.setIcon(QIcon('update.png'))
        self.boton3.setIconSize(self.boton3.size())
        self.boton3.setStyleSheet('border: none;')
        self.boton3.clicked.connect(lambda: self.update_boton(self.boton3))

        self.boton4 = QPushButton(self)
        self.boton4.setFixedSize(300, 100)
        self.boton4.setIcon(QIcon('consulta.png'))
        self.boton4.setIconSize(self.boton4.size())
        self.boton4.setStyleSheet('border: none;')
        self.boton4.clicked.connect(lambda: self.consulta_boton(self.boton4))







#-------------Ingresa los botones al label-----------------------------------------------------

        botones = QVBoxLayout()
        botones.addWidget(self.boton1)
        botones.addWidget(self.boton2)
        botones.addWidget(self.boton3)
        botones.addWidget(self.boton4)
        botones.setSpacing(0)
        f_botones.setLayout(botones)

        self.show()



    def insertar_boton(self, boton):
        self.transparencia(boton)
        self.ventana_insert = Ventana_insertar(self.nom_tabla)
        self.ventana_insert.show()

    def borrar_boton(self, boton):
        self.transparencia(boton)
        self.ventana_borrar = Ventana_borrado()
        self.ventana_borrar.show()


    def update_boton(self, boton):
        self.transparencia(boton)
        self.ventana_update = Ventana_update()
        self.ventana_update.show()


    def consulta_boton(self, boton):
        self.transparencia(boton)
        self.ventana_consulta = Ventana_consulta()
        self.ventana_consulta.show()
    def transparencia(self, boton):
        current_stylesheet = boton.styleSheet()
        transparency_value = 0.5
        new_stylesheet = f"{current_stylesheet} background-color: rgba(0, 0, 0, {transparency_value});"
        boton.setStyleSheet(new_stylesheet)

        QTimer.singleShot(50, lambda: self.restaurarColorOriginal(boton))

    def restaurarColorOriginal(self, boton):
        boton.setStyleSheet(f"{boton.styleSheet()} background-color: none;")

