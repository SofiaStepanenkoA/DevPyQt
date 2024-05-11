"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from ui.d_eventfilter_settings_form import Ui_Form

ORG_NAME = "PC_master"
APP_NAME = "My_app"

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadSettings()  # Загрузка сохраненных настроек
        self.initSignals()

    def loadSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        # Загрузка сохраненных значений и установка их на виджеты
        self.ui.lcdNumber.display(settings.value('lcd_value', 0, type=int))
        self.ui.dial.setValue(settings.value('lcd_value', 0, type=int))
        self.ui.horizontalSlider.setValue(settings.value('lcd_value', 0, type=int))
        self.ui.comboBox.setCurrentText(settings.value('lcd_mode', 'dec'))

    def saveSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        # Сохранение значений в QSettings
        settings.setValue('lcd_value', int(self.ui.lcdNumber.value()))
        settings.setValue('lcd_mode', self.ui.comboBox.currentText())

    def closeEvent(self, event):
        self.saveSettings()  # Сохранение настроек при закрытии приложения

    def initSignals(self):
        # Подключение сигналов к слотам
        self.ui.dial.valueChanged.connect(self.dialChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.sliderChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.digitMode)

    def keyPressEvent(self, event):
        # Обработка нажатий клавиш
        if event.text() == '+':
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.text() == '-':
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def dialChanged(self):
        # Обновление значений при изменении значения диалога
        value = self.ui.dial.value()
        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)

    def sliderChanged(self):
        # Обновление значений при изменении значения слайдера
        value = self.ui.horizontalSlider.value()
        self.ui.dial.setValue(value)
        self.ui.lcdNumber.display(value)

    def digitMode(self):
        # Установка режима отображения на основе выбранного значения в comboBox
        mode = self.ui.comboBox.currentText()
        if mode == 'hex':
            self.ui.lcdNumber.setHexMode()
        elif mode == 'bin':
            self.ui.lcdNumber.setBinMode()
        elif mode == 'dec':
            self.ui.lcdNumber.setDecMode()
        elif mode == 'oct':
            self.ui.lcdNumber.setOctMode()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()

