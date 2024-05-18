"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import sys
from PySide6 import QtWidgets, QtCore
from a_threads import SystemInfo

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.systemInfoThread = SystemInfo(1)
        self.initUI()
        self.initTimer()
        self.__initSignals()
        self.systemInfoThread.start()

    def initUI(self):
        self.setWindowTitle("System Info")

        self.delayInput = QtWidgets.QLineEdit()
        self.delayInput.setPlaceholderText("Введите время задержки (в секундах)")

        self.cpuLabel = QtWidgets.QLabel("Загрузка CPU: ")
        self.cpuInfo = QtWidgets.QPlainTextEdit()
        self.cpuInfo.setReadOnly(True)

        self.ramLabel = QtWidgets.QLabel("Загрузка RAM: ")
        self.ramInfo = QtWidgets.QPlainTextEdit()
        self.ramInfo.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.delayInput)
        layout.addWidget(self.cpuLabel)
        layout.addWidget(self.cpuInfo)
        layout.addWidget(self.ramLabel)
        layout.addWidget(self.ramInfo)

        self.setLayout(layout)

    def initTimer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.start()
        self.timer.setInterval(1000)

    def __initSignals(self):
        self.delayInput.textChanged.connect(self.updateDelay)
        self.timer.timeout.connect(self.updateData)


    def updateDelay(self):
        try:
            delay = int(self.delayInput.text())
            self.timer.setInterval(delay)  # Устанавливаем интервал таймера
            self.systemInfoThread.delay = delay
            print(f"Задержка обновления установлена на {delay} сек")
        except ValueError:
            print("Введите корректное число для задержки")

    def updateData(self):
        self.systemInfoThread.systemInfoReceived.connect(self.updateSystemInfo)


    def updateSystemInfo(self, info):
        cpu_value, ram_value = info
        self.cpuInfo.setPlainText(f"Загрузка CPU: {cpu_value}%")
        self.ramInfo.setPlainText(f"Загрузка RAM: {ram_value.percent}%")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())