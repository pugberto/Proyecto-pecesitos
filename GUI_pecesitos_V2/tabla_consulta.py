from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QColor, QIcon


class VentanaConsulta(QWidget):
    def __init__(self, resultados):
        super().__init__()

        layout = QVBoxLayout(self)

        # Crear la tabla y establecer el número de filas y columnas
        tabla = QTableWidget(self)
        tabla.setRowCount(len(resultados))
        tabla.setColumnCount(len(resultados[0]) if resultados else 0)

        # Llenar la tabla con los resultados de la consulta
        for i, fila in enumerate(resultados):
            for j, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                tabla.setItem(i, j, item)

        tabla.verticalHeader().setVisible(False)
        tabla.horizontalHeader().setVisible(False)
        layout.addWidget(tabla)
        self.setLayout(layout)