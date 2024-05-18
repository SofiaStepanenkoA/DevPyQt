"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore


class DigitalClockWidget(QtWidgets.QLabel):
    dateChanged = QtCore.Signal(QtCore.QDateTime)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initTimers()

    def __initUi(self):
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial")
        self.__updateTime()

    def __initTimers(self):
        self.__timer = QtCore.QTimer(self)
        self.__timer.timeout.connect(self.__updateTime)
        self.__timer.setInterval(1000)
        self.__timer.start()

    def __updateTime(self):
        dateTime = QtCore.QDateTime.currentDateTime()
        self.setText(dateTime.toString("hh:mm:ss"))
        self.dateChanged.emit(dateTime)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = DigitalClockWidget()
    window.dateChanged.connect(print)
    window.show()

    app.exec()
