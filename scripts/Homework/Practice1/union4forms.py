from PySide6 import QtWidgets
from b import Window as login_window
from c import Window as Ship_window
from d import Window as engine_window
from e import Window as profile_window

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_widget = login_window()
        self.ship_parameters = Ship_window()
        self.engine_window = engine_window()
        self.profile_window = profile_window()

        l_left = QtWidgets.QVBoxLayout()
        l_left.addWidget(self.login_widget)
        l_left.addWidget(self.profile_window)
        l_left.addWidget(self.ship_parameters)

        # l_left.addSpacerItem(QtWidgets.QSpacerItem(
        #     w=0,h=10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding))
        l_main = QtWidgets.QHBoxLayout()
        l_main.addLayout(l_left)
        l_main.addWidget(self.engine_window)
        self.setLayout(l_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()
