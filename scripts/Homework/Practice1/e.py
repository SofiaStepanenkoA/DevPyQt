from PySide6 import QtWidgets
from e_profile_card.Form1 import Ui_Form
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