"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

import requests
from PySide6 import QtWidgets, QtCore




def get_status_code(url):
    try:
        responce = requests.get(url)
        return responce.status_code
    except Exception as err:
        return str(err)

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.getUrlStatusThread = None

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Введите url")

        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(5)

        self.labelStatus = QtWidgets.QLabel()
        self.labelStatus.setText("Статус сайта: ")

        self.plainTextEditLog = QtWidgets.QPlainTextEdit()
        self.plainTextEditLog.setReadOnly(True)

        self.pushButtonHandle = QtWidgets.QPushButton("Запустить")
        self.pushButtonHandle.setCheckable(True)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.lineEditUrl)
        l.addWidget(self.spinBoxDelay)
        l.addWidget(self.labelStatus)
        l.addWidget(self.plainTextEditLog)
        l.addWidget(self.pushButtonHandle)

        self.setLayout(l)

    def __initSignals(self) -> None:
        self.pushButtonHandle.clicked.connect(self.__changeButtonText)
        self.pushButtonHandle.clicked.connect(self.__handleUrl)

        self.spinBoxDelay.valueChanged.connect(self.__setThreadDelay)

    def __startThread(self, url) -> None:
        self.getUrlStatusThread = GetURLStatusThread()
        self.getUrlStatusThread.url = url
        self.getUrlStatusThread.delay = self.spinBoxDelay.value()

        self.getUrlStatusThread.status_code.connect(self.__changeStatus)
        self.getUrlStatusThread.finished.connect(self.__threadFinished)

        self.getUrlStatusThread.start()

    def __threadFinished(self):
        self.getUrlStatusThread = None
        self.pushButtonHandle.setEnabled(True)

    def __handleUrl(self, status):
        if status:
            url = self.lineEditUrl.text()
            if not url.strip():
                QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите url")
                self.pushButtonHandle.setChecked(False)
                self.pushButtonHandle.setText("Запустить")
                return

            self.__startThread(url)

        else:
            self.getUrlStatusThread.status = False
            self.pushButtonHandle.setEnabled(False)

    def __changeButtonText(self, status):
        self.pushButtonHandle.setText("Остановить" if status else "Запустить")

    def __setThreadDelay(self, value):
        if self.getUrlStatusThread:
            self.getUrlStatusThread.delay = value

    def __changeStatus(self, status):
        self.plainTextEditLog.appendPlainText(f"{QtCore.QDateTime.currentDateTime().toString()} >>> {status}")


class GetURLStatusThread(QtCore.QThread):
    status_code = QtCore.Signal(object)

    def __init__(self, url=None, delay=5, parent=None):
        super().__init__(parent)

        self.__url = url
        self.__delay = delay
        self.__status = True

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, value):
        self.__delay = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def run(self):
        if not self.__url:
            self.status_code.emit("URL not set")
            return

        while self.__status:
            self.status_code.emit(get_status_code(self.__url))
            self.sleep(self.delay)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
