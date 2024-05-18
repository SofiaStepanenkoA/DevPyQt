"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""
import hashlib

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal

from scripts.Homework.Practice1.b_login.app1 import app as LoginWidget
from scripts.Homework.Practice1.b_login.Form1 import Ui_Dialog

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initChilds()
        self.__initSignals()

    def __initUi(self):
        label = QtWidgets.QLabel()
        label.setText("<h2>Пройдите регистрацию</h2>")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.__pushButton = QtWidgets.QPushButton()
        self.__pushButton.setText("Зарегистрироваться")

        l = QtWidgets.QVBoxLayout()
        l.addWidget(label)
        l.addWidget(self.__pushButton)

        self.setLayout(l)

    def __initChilds(self):
        self.registrationWidget = RegistrationWidget()

    def __initSignals(self):
        self.__pushButton.clicked.connect(self.registrationWidget.show)
        self.registrationWidget.registered.connect(self.__registeredUser)

    def __registeredUser(self, data):
        l = self.layout()
        widget = l.itemAt(0).widget()
        widget.setText(f'<h2>Привет,</h2> <h1>{data[0]}</h1>')
        print(hashlib.sha1(data[1].encode()).hexdigest())


class RegistrationWidget(LoginWidget):
    registered = Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        labelRepeat = QtWidgets.QLabel("Повторите пароль")
        labelRepeat.setMinimumWidth(250)

        self.lineEditRepeatPassword = QtWidgets.QLineEdit()
        self.lineEditRepeatPassword.setPlaceholderText("Повторите пароль")

        l = QtWidgets.QHBoxLayout()
        l.addWidget(labelRepeat)
        l.addWidget(self.lineEditRepeatPassword)

        self.ui.verticalLayout.insertLayout(2, l)

        self.ui.label.setMinimumWidth(250)
        self.ui.label_2.setMinimumWidth(250)
        self.ui.pushButtonAuth.setText("Регистрация")
        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def __initSignals(self):
        self.ui.pushButtonAuth.clicked.connect(self.__onPushButtonAuthClicked)

    def __onPushButtonAuthClicked(self):
        login = self.ui.lineEditLogin.text()

        if not login.strip():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы не указали логин")
            return

        password_1 = self.ui.lineEditPassword.text()
        password_2 = self.lineEditRepeatPassword.text()

        if not password_1.strip() or not password_2.strip():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Вы не указали пароль")
            return

        if password_1 != password_2:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пароли не совпадают")
            return

        self.registered.emit((login, password_1))

        self.clear()
        self.close()

    def clear(self):
        self.ui.lineEditPassword.clear()
        self.ui.lineEditLogin.clear()
        self.lineEditRepeatPassword.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    # window.registered.connect(lambda data: print(data))
    window.show()

    app.exec()