import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QIcon

from borrar_animal import Ventana_borar_animal
from borrar_plantas import Ventana_borar_plantas
from consulta_chats import Ventana_consulta_chars
from consulta_ints import Ventana_consulta_ints


class Ventana_consulta(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI6()

    def initUI6(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('consulta')
        fondo = QLabel(self) # fondo
        color_tabla_fondo = QColor(173, 216, 230)
        fondo.setGeometry(0, 0, 500, 300)
        fondo.setStyleSheet(f"background-color: {color_tabla_fondo.name()};")

        self.boton_id = QPushButton(self)
        self.boton_id.setText("ID")
        self.boton_id.setFixedSize(300, 100)
        self.boton_id.clicked.connect(lambda: self.consulta_id(self.boton_id))

        self.boton_tanq = QPushButton(self)
        self.boton_tanq.setText("num_tanque")
        self.boton_tanq.setFixedSize(300, 100)
        self.boton_tanq.clicked.connect(lambda: self.consulta_tanq(self.boton_tanq))

        self.boton_habit = QPushButton(self)
        self.boton_habit.setText("Habitat")
        self.boton_habit.setFixedSize(300, 100)
        self.boton_habit.clicked.connect(lambda: self.consulta_habit(self.boton_habit))

        self.boton_Alimento = QPushButton(self)
        self.boton_Alimento.setText("Alimento")
        self.boton_Alimento.setFixedSize(300, 100)
        self.boton_Alimento.clicked.connect(lambda: self.consulta_Alimento(self.boton_Alimento))

        self.boton_t_vida = QPushButton(self)
        self.boton_t_vida.setText("tipo de vida")
        self.boton_t_vida.setFixedSize(300, 100)
        self.boton_t_vida.clicked.connect(lambda: self.consulta_tipo(self.boton_t_vida))

        botones = QVBoxLayout()
        botones.addWidget(self.boton_id)
        botones.addWidget(self.boton_tanq)
        botones.addWidget(self.boton_habit)
        botones.addWidget(self.boton_Alimento)
        botones.addWidget(self.boton_t_vida)
        botones.setSpacing(0)
        fondo.setLayout(botones)


        self.show()

    def consulta_id(self, boton):
        self.transparencia2(boton)
        self.ventana_cons_id = Ventana_consulta_ints("ID")
        self.ventana_cons_id.show()

    def consulta_tanq(self, boton):
        self.transparencia2(boton)
        self.ventana_cons_id = Ventana_consulta_ints("Numero_tanque")
        self.ventana_cons_id.show()

    def consulta_habit(self, boton):
        self.transparencia2(boton)
        self.ventana_cons_id = Ventana_consulta_chars("Habitat")
        self.ventana_cons_id.show()

    def consulta_Alimento(self, boton):
        self.transparencia2(boton)
        self.ventana_cons_id = Ventana_consulta_chars("Alimento")
        self.ventana_cons_id.show()

    def consulta_tipo(self, boton):
        self.transparencia2(boton)
        self.ventana_cons_id = Ventana_consulta_chars("Tipo_vida_marina")
        self.ventana_cons_id.show()

    def transparencia2(self, boton):
        current_stylesheet = boton.styleSheet()
        transparency_value = 0.5
        new_stylesheet = f"{current_stylesheet} background-color: rgba(0, 0, 0, {transparency_value});"
        boton.setStyleSheet(new_stylesheet)

        QTimer.singleShot(50, lambda: self.restaurarColorOriginal2(boton))


    def restaurarColorOriginal2(self, boton):
        # Función para restaurar el color original del botón
        boton.setStyleSheet(f"{boton.styleSheet()} background-color: none;")

