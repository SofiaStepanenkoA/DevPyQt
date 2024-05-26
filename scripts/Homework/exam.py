import sys
from PySide6 import QtCore, QtWidgets, QtGui
import random

class Game2048(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resetGame()

    def initUI(self):
        self.setWindowTitle("2048")
        self.gridLayout = QtWidgets.QGridLayout()
        self.setLayout(self.gridLayout)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setFixedSize(400, 400)

    def resetGame(self):
        self.score = 0
        self.grid = [[0] * 4 for _ in range(4)]
        self.addRandomTile()
        self.addRandomTile()
        self.updateUI()

    def addRandomTile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col] = 2 if random.random() < 0.9 else 4

    def updateUI(self):
        self.gridLayout.itemAt(0)
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        for i in range(4):
            for j in range(4):
                tile = self.grid[i][j]
                label = QtWidgets.QLabel(str(tile) if tile != 0 else "")
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet(f"QLabel {{background-color: {self.getColor(tile)}; color: white; font-size: 24px;}}")
                self.gridLayout.addWidget(label, i, j)

    def getColor(self, value):
        colors = {
            0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def keyPressEvent(self, event):
        key = event.key()
        if key in [QtCore.Qt.Key_Left, QtCore.Qt.Key_Right, QtCore.Qt.Key_Up, QtCore.Qt.Key_Down]:
            self.moveTiles(key)
            self.addRandomTile()
            self.updateUI()

    def moveTiles(self, direction):
        def collapse(row):
            row = [val for val in row if val != 0]
            new_row = []
            i = 0
            while i < len(row):
                if i < len(row) - 1 and row[i] == row[i + 1]:
                    new_row.append(row[i] * 2)
                    self.score += row[i] * 2
                    i += 2
                else:
                    new_row.append(row[i])
                    i += 1
            return new_row + [0] * (4 - len(new_row))

        def rotate(grid):
            return [[grid[j][i] for j in range(4)] for i in range(4)]

        if direction == QtCore.Qt.Key_Left:
            self.grid = [collapse(row) for row in self.grid]
        elif direction == QtCore.Qt.Key_Right:
            self.grid = [collapse(row[::-1])[::-1] for row in self.grid]
        elif direction == QtCore.Qt.Key_Up:
            self.grid = rotate(self.grid)
            self.grid = [collapse(row) for row in self.grid]
            self.grid = rotate(rotate(rotate(self.grid)))
        elif direction == QtCore.Qt.Key_Down:
            self.grid = rotate(rotate(self.grid))
            self.grid = [collapse(row) for row in self.grid]
            self.grid = rotate(self.grid)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = Game2048()
    game.show()
    sys.exit(app.exec())
