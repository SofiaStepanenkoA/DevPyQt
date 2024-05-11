"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets
from ui.c_signals_events_form import Ui_Form
import PySide6
import datetime
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.movecounter=0
        self.initSignals()

    def initSignals(self)-> None:

        self.ui.pushButtonLT.clicked.connect(self.LTmove)
        self.ui.pushButtonLB.clicked.connect(self.LBmove)
        self.ui.pushButtonRT.clicked.connect(self.RTmove)
        self.ui.pushButtonRB.clicked.connect(self.RBmove)
        self.ui.pushButtonCenter.clicked.connect(self.Center)
        self.ui.pushButtonMoveCoords.clicked.connect(self.spinBoxMove)
        self.ui.pushButtonGetData.clicked.connect(self.GetData)

    def LTmove(self) -> None:
        pos1, pos2 = self.pos().toTuple()
        self.move(pos1 - 10, pos2 - 10)

    def LBmove(self) -> None:
        pos1, pos2 = self.pos().toTuple()
        self.move(pos1 - 10, pos2 + 10)

    def RTmove(self) -> None:
        pos1, pos2 = self.pos().toTuple()
        self.move(pos1 + 10, pos2 - 10)

    def RBmove(self) -> None:
        pos1, pos2 = self.pos().toTuple()
        self.move(pos1 + 10, pos2 + 10)
    def Center(self) -> None:
        self.move(self.initial_coordinates[0],self.initial_coordinates[1])

    def spinBoxMove(self)->None:
        value1 = int(self.ui.spinBoxX.text())
        value2 = int(self.ui.spinBoxY.text())
        self.move(value1,value2)

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        print(f'time: {datetime.datetime.now().strftime("%H:%M:%S")} new size {self.size().toTuple()}')
    def moveEvent(self, event: PySide6.QtGui.QMoveEvent) -> None:
        if self.movecounter==0:
            self.initial_coordinates = self.pos().toTuple()
            self.previuos_pos = [self.pos().toTuple()[0], self.pos().toTuple()[1]]
            self.movecounter=self.movecounter+1
        print(f'time: {datetime.datetime.now().strftime("%H:%M:%S")} old pos:{self.previuos_pos} new pos:{self.pos().toTuple()}')
        self.previuos_pos[0] = self.pos().toTuple()[0]
        self.previuos_pos[1] = self.pos().toTuple()[1]
    def GetData(self) -> None:
        screen = QtWidgets.QApplication.primaryScreen()
        screen_count = len(QtWidgets.QApplication.screens())
        current_screen = QtWidgets.QApplication.primaryScreen().name()
        screen_geometry = screen.geometry()
        window_geometry = self.geometry()
        min_window_size = self.minimumSize()
        current_position = self.pos()
        center_position = self.geometry().center()

        data = f"""
            Время: {datetime.datetime.now().strftime("%H:%M:%S")}
            Количество экранов: {screen_count}
            Текущий основной экран: {current_screen}
            Разрешение экрана: {screen_geometry.width()}x{screen_geometry.height()}
            Экран, на котором находится окно: {current_screen}
            Размеры окна: {window_geometry.width()}x{window_geometry.height()}
            Минимальные размеры окна: {min_window_size.width()}x{min_window_size.height()}
            Текущее положение окна: {current_position.x()},{current_position.y()}
            Координаты центра приложения: {center_position.x()},{center_position.y()}
            """

        self.ui.plainTextEdit.appendPlainText(data)
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()
