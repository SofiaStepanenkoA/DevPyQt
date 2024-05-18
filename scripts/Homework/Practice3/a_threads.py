"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
from PySide6 import QtCore
import requests

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, delay=None, parent=None):
        super().__init__(parent)
        self.delay = delay  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory()  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value,ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    Weatherinfo = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.setDelay(1)
        self.__status = True

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def run(self) -> None:
        while self.__status:
            print("Запрос данных о погоде")  # Отладочное сообщение
            response = requests.get(self.__api_url)
            data = response.json()
            self.Weatherinfo.emit(data)
            print("Сигнал отправлен")  # Отладочное сообщение
            time.sleep(self.__delay)






