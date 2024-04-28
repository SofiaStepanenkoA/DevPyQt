from PySide6 import QtWidgets
from b_login.Form1 import Ui_Dialog
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()