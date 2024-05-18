"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings

ORG_NAME = "PCMaster"
APP_NAME = "MyApp"


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__loadSettings()

    def __initUi(self):
        self.__plainTextEdit = QtWidgets.QPlainTextEdit()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.__plainTextEdit)

        self.setLayout(l)

    def __loadSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        self.__plainTextEdit.setPlainText(settings.value('text', ''))

    def __saveSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        settings.setValue('text', self.__plainTextEdit.toPlainText())

    def closeEvent(self, event):
        self.__saveSettings()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()