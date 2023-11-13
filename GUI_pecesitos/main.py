import mysql.connector
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QColor, QIcon


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 50, 900, 600)
        self.setWindowTitle('Pecesitos')

        tabla = QTableWidget(self)
        tabla.setRowCount(5)
        tabla.setColumnCount(3)

        for i in range(tabla.rowCount()):
            for j in range(tabla.columnCount()):
                item = QTableWidgetItem(f"Fila {i + 1}, Col {j + 1}")
                tabla.setItem(i, j, item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Crear un layout horizontal
        layout_horizontal = QHBoxLayout(self)

        # Agregar el spacer y la tabla al layout horizontal
        layout_horizontal.addItem(spacer)
        layout_horizontal.addWidget(tabla)

        self.setLayout(layout_horizontal)

        # ---------------------------------BOTONES------------------------------------------------------------------------------------

        self.boton1 = QPushButton(self)
        self.boton1.setFixedSize(300, 100)  # Establecer tamaño del boton
        self.boton1.setIcon(QIcon('insert.png')) # Ingresa el icono en el boton
        self.boton1.setIconSize(self.boton1.size()) # Establece el tamaño del icono del mismo tamaño que el boton
        self.boton1.setStyleSheet('border: none;') # Quita los bordes del boton
        self.boton1.clicked.connect(lambda: self.mostrarHola(self.boton1)) # Evento que sucede cuando lo clikeas (Por ahora no hace nada mas que cambiar de color el boton)

        self.boton2 = QPushButton(self)
        self.boton2.setFixedSize(300, 100)
        self.boton2.setIcon(QIcon('DELETE.png'))
        self.boton2.setIconSize(self.boton2.size())
        self.boton2.setStyleSheet('border: none;')
        self.boton2.clicked.connect(lambda: self.mostrarHola(self.boton2))

        self.boton3 = QPushButton(self)
        self.boton3.setFixedSize(300, 100)
        self.boton3.setIcon(QIcon('update.png'))
        self.boton3.setIconSize(self.boton3.size())
        self.boton3.setStyleSheet('border: none;')
        self.boton3.clicked.connect(lambda: self.mostrarHola(self.boton3))

        self.boton4 = QPushButton(self)
        self.boton4.setFixedSize(300, 100)
        self.boton4.setIcon(QIcon('consulta.png'))
        self.boton4.setIconSize(self.boton4.size())
        self.boton4.setStyleSheet('border: none;')
        self.boton4.clicked.connect(lambda: self.mostrarHola(self.boton4))

        color_de_fondo = QColor(173, 216, 230) # Color de fondo principal
        self.setStyleSheet(f"background-color: {color_de_fondo.name()};")

        etiqueta = QLabel(self)  # etiqueta a la izquierda
        etiqueta.setGeometry(0, 0, 350, 600)

        color_etiqueta_fondo = QColor(224, 255, 255)    # Color de fondo de la etiqueta
        etiqueta.setStyleSheet(f"background-color: {color_etiqueta_fondo.name()};")

        botones = QVBoxLayout()

#-------------Ingresa los botones al label-----------------------------------------------------
        botones.addWidget(self.boton1)
        botones.addWidget(self.boton2)
        botones.addWidget(self.boton3)
        botones.addWidget(self.boton4)
        botones.setSpacing(0)
        etiqueta.setLayout(botones)

        self.show()

#-------------Fución de prueba-----------------------------------------------------------------
    def mostrarHola(self, boton):
        # Función para cambiar la transparencia del botón temporalmente
        current_stylesheet = boton.styleSheet()
        transparency_value = 0.5  # Ajusta el valor de transparencia según tus preferencias
        new_stylesheet = f"{current_stylesheet} background-color: rgba(0, 0, 0, {transparency_value});"
        boton.setStyleSheet(new_stylesheet)

        QTimer.singleShot(50, lambda: self.restaurarColorOriginal(boton))

    def restaurarColorOriginal(self, boton):
        # Función para restaurar el color original del botón
        boton.setStyleSheet(f"{boton.styleSheet()} background-color: none;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    sys.exit(app.exec_())










# conexion = mysql.connector.connect(user='root', password='salchipapa12',
#                                  host='localhost',
#                                  database= 'proyecto_final',
#                                  port='3306')

# mycursor = conexion.cursor()

# sql = "INSERT INTO acuario (Numero_RUT, Coste_mantenimento) VALUES (%s, %s)"
# val = ("12345678", 12.5)
# mycursor.execute(sql, val)

# sql = "INSERT INTO tanque (Numero_tanque, Numero_RUT, Habitat, Tamano) VALUES (%s, %s, %s, %s)"
# val = (0, "12345678", "Dulce", "Pequeño")
# mycursor.execute(sql, val)

# sql = "INSERT INTO vida_marina (ID, Numero_tanque, Habitat, Alimento, Tipo_vida_marina) VALUES (%s, %s, %s, %s, %s)"
# val = (0, 1, "Dulce", "Gusanos", "Animales")
# mycursor.execute(sql, val)


# sql = "INSERT INTO animal (ID_animal, Comportamiento) VALUES (%s, %s)"
# val = (1, "Agresivo")
# mycursor.execute(sql, val)

# conexion.commit()

# print(mycursor.lastrowid, "record inserted.")
