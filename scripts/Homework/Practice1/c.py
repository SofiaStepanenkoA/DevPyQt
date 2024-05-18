from PySide6 import QtWidgets
from c_ship_parameters.ship_parameters import Ui_Form
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()
