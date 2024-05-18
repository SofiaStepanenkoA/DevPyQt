"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

        self.__labelColorStatus = True

    def __initUi(self):
        self.__label = QtWidgets.QLabel()
        self.__label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.__label.setText("<span style='color:red;'>Красивая</span> <span style='color:green;'>кнопка</span>")
        # self.__label.setStyleSheet("background-color: white")

        self.__label.installEventFilter(self)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.__label)

        self.setLayout(l)

    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.__invertColor()

        return super().eventFilter(watched, event)

    def __invertColor(self):
        colors = ['red', 'green']

        self.__label.setText(f"<span style='color:{colors[self.__labelColorStatus]};'>Красивая</span> <span style='color:{colors[not self.__labelColorStatus]};'>кнопка</span>")

        self.__labelColorStatus = not self.__labelColorStatus

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()