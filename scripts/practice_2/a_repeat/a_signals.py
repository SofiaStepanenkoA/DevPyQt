"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtCore


def is_palindrome(text):
    return text.lower() == text.lower()[::-1]


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.setMinimumSize(400, 100)

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditInput.setPlaceholderText("Исходное значение")

        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setPlaceholderText("Результат")
        self.lineEditMirror.setReadOnly(True)

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

        l_inputs = QtWidgets.QHBoxLayout()
        l_inputs.addWidget(self.lineEditInput)
        l_inputs.addWidget(self.lineEditMirror)

        l_buttons = QtWidgets.QVBoxLayout()
        l_buttons.addWidget(self.pushButtonMirror)
        l_buttons.addWidget(self.pushButtonClear)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_inputs)
        l_main.addLayout(l_buttons)
        self.setLayout(l_main)

    def __initSignals(self):
        self.pushButtonMirror.clicked.connect(self.__onPushButtonMirrorClicked)
        self.pushButtonClear.clicked.connect(self.__onPushButtonClearClicked)

        self.lineEditInput.textChanged.connect(self.__onPushButtonMirrorClicked)

    def __onPushButtonMirrorClicked(self):
        source_text = self.lineEditInput.text()

        if not source_text.strip():
            self.__onPushButtonClearClicked()
            return

        self.lineEditMirror.setText(source_text[::-1])

        if is_palindrome(source_text) and len(source_text) > 1:
            QtWidgets.QMessageBox.about(self, 'Palindrome', f'Слово {source_text} является палиндромом')



    def __onPushButtonClearClicked(self):
        self.lineEditMirror.clear()
        self.lineEditInput.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
