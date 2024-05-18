"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import sys
from PySide6 import QtWidgets
from b_systeminfo_widget import MainWindow as System
from c_weatherapi_widget import MainWindow as Weather

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("System and Weather Info")

        # Создаем экземпляры виджетов
        self.systemWidget = System()
        self.weatherWidget = Weather()

        # Размещаем виджеты на форме
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.systemWidget)
        layout.addWidget(self.weatherWidget)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
