"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import sys
from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.weatherThread = None
        self.initUI()
        self.initSignals()

    def initUI(self):
        self.setWindowTitle("Weather Info")

        self.latInput = QtWidgets.QLineEdit()
        self.latInput.setPlaceholderText("Введите широту")

        self.lonInput = QtWidgets.QLineEdit()
        self.lonInput.setPlaceholderText("Введите долготу")

        self.delayInput = QtWidgets.QLineEdit()
        self.delayInput.setPlaceholderText("Введите время задержки (в секундах)")

        self.weatherInfo = QtWidgets.QPlainTextEdit()
        self.weatherInfo.setReadOnly(True)

        self.toggleButton = QtWidgets.QPushButton("Запустить поток")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.latInput)
        layout.addWidget(self.lonInput)
        layout.addWidget(self.delayInput)
        layout.addWidget(self.weatherInfo)
        layout.addWidget(self.toggleButton)

        self.setLayout(layout)

    def initSignals(self):
        self.toggleButton.clicked.connect(self.toggleThread)

    def toggleThread(self):
        if self.weatherThread is None:
            try:
                lat = float(self.latInput.text())
                lon = float(self.lonInput.text())
                delay = int(self.delayInput.text())
            except ValueError:
                self.weatherInfo.setPlainText("Введите корректные значения широты, долготы и задержки.")
                return

            self.weatherThread = WeatherHandler(lat, lon)
            self.weatherThread.setDelay(delay)
            self.weatherThread.Weatherinfo.connect(self.receiveWeatherInfo)
            self.weatherThread.__status = True
            self.weatherThread.start()

            self.latInput.setDisabled(True)
            self.lonInput.setDisabled(True)
            self.delayInput.setDisabled(True)
            self.toggleButton.setText("Остановить поток")
            print("Поток запущен")
        else:
            self.weatherThread.__status = False
            self.weatherThread.terminate()
            self.weatherThread = None

            self.latInput.setDisabled(False)
            self.lonInput.setDisabled(False)
            self.delayInput.setDisabled(False)
            self.toggleButton.setText("Запустить поток")
            print("Поток остановлен")

    def receiveWeatherInfo(self, data):
        print("Получены данные о погоде")  # Отладочное сообщение
        self.updateWeatherInfo(data)

    def updateWeatherInfo(self, data):
        print("Обновление информации о погоде")  # Отладочное сообщение
        try:
            weather = data["current_weather"]
            self.weatherInfo.setPlainText(
                f"Температура: {weather['temperature']}°C\n"
                f"Скорость ветра: {weather['windspeed']} км/ч\n"
            )
        except KeyError:
            self.weatherInfo.setPlainText("Ошибка получения данных о погоде.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
