from sql import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QMessageBox
from PyQt5.QtGui import QColor, QIcon

class Ventana_update_animal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI9()

    def initUI9(self):
        self.setGeometry(300, 50, 500, 300)
        self.setWindowTitle('update_p')
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
        boton_procesar.clicked.connect(self.procesar_datos2)

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

        self.datos = []

    def procesar_datos2(self):
        conexion = mysql.connector.connect(user='root', password='salchipapa12',
                                           host='localhost',
                                           database='proyecto_final',
                                           port='3306')


        mycursor = conexion.cursor()

        t_id= self.line_edit_ID.text()
        t_tanque = self.line_edit_tanque.text()
        t_habitad = self.line_edit_habitad.text()
        t_alimento = self.line_edit_alimento.text()
        t_comportamiento = self.line_edit_comportamiento.text()

        id = int(t_id)

        if t_tanque:
            self.datos.append(("Numero_tanque", int(t_tanque)))

        if t_habitad:
            self.datos.append(("Habitat", t_habitad))

        if t_alimento:
            self.datos.append(("Alimento", t_alimento))

        if t_comportamiento:
            self.datos.append(("Comportamiento", t_comportamiento))


        print(self.datos)

        if id:
            for elemt in self.datos:
                if elemt[0] == "Comportamiento":
                    sql_update = "UPDATE animal SET Comportamiento = %s WHERE ID_animal = %s"
                    mycursor.execute(sql_update, (elemt[1], id))
                else:
                    sql_update = f"UPDATE vida_marina SET {elemt[0]} = %s WHERE ID = %s"
                    mycursor.execute(sql_update, (elemt[1], id))





            conexion.commit()

            mycursor.close()
            conexion.close()
        else:
            mensaje_box = QMessageBox()
            mensaje_box.setIcon(QMessageBox.Information)
            mensaje_box.setWindowTitle("Mensaje")
            mensaje_box.setText("ID necesaria.")
            mensaje_box.addButton(QMessageBox.Ok)
            respuesta = mensaje_box.exec_()
