import sys
import random
import json
from PySide6 import QtCore, QtWidgets

GRID_SIZE = 4
TILE_COLORS = {
    0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
    256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}


class Game2048(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_game_state()

    def initUI(self):
        self.setWindowTitle("2048")
        self.gridLayout = QtWidgets.QGridLayout()
        self.setLayout(self.gridLayout)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setFixedSize(400, 500)

        self.new_game_button = QtWidgets.QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.new_game)
        self.gridLayout.addWidget(self.new_game_button, GRID_SIZE, 0, 1, GRID_SIZE)

        self.tiles = [[QtWidgets.QLabel(self) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                label = self.tiles[i][j]
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet(f"QLabel {{background-color: {TILE_COLORS[0]}; color: white; font-size: 24px;}}")
                self.gridLayout.addWidget(label, i, j)

    def load_game_state(self):
        try:
            with open('game_state.json', 'r') as f:
                state = json.load(f)
                self.grid = state['grid']
                self.score = state['score']
                self.updateUI()
        except FileNotFoundError:
            self.new_game()

    def save_game_state(self):
        state = {'grid': self.grid, 'score': self.score}
        with open('game_state.json', 'w') as f:
            json.dump(state, f)

    def new_game(self):
        self.score = 0
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.addRandomTile()
        self.addRandomTile()
        self.updateUI()

    def addRandomTile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.grid[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col] = 2 if random.random() < 0.9 else 4

    def updateUI(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.grid[i][j]
                label = self.tiles[i][j]
                label.setText(str(value) if value != 0 else "")
                label.setStyleSheet(
                    f"QLabel {{background-color: {TILE_COLORS[value]}; color: white; font-size: 24px;}}")

        if self.is_game_over():
            max_tile = max(max(row) for row in self.grid)
            QMessageBox = QtWidgets.QMessageBox(self)
            QMessageBox.setWindowTitle("Game Over")
            QMessageBox.setText(f"Game over! Your score is {max_tile}")
            QMessageBox.exec()
            self.new_game()

    def is_game_over(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == 0:
                    return False
                if col < GRID_SIZE - 1 and self.grid[row][col] == self.grid[row][col + 1]:
                    return False
                if row < GRID_SIZE - 1 and self.grid[row][col] == self.grid[row + 1][col]:
                    return False
        return True

    def keyPressEvent(self, event):
        key = event.key()
        moved = False

        if key == QtCore.Qt.Key_Up:
            moved = self.move_up()
        elif key == QtCore.Qt.Key_Down:
            moved = self.move_down()
        elif key == QtCore.Qt.Key_Left:
            moved = self.move_left()
        elif key == QtCore.Qt.Key_Right:
            moved = self.move_right()

        if moved:
            self.addRandomTile()
            self.updateUI()
            self.save_game_state()

    def compress(self, grid):
        new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        for row in range(GRID_SIZE):
            pos = 0
            for col in range(GRID_SIZE):
                if grid[row][col] != 0:
                    new_grid[row][pos] = grid[row][col]
                    pos += 1
        return new_grid

    def merge(self, grid):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE - 1):
                if grid[row][col] == grid[row][col + 1] and grid[row][col] != 0:
                    grid[row][col] *= 2
                    grid[row][col + 1] = 0
                    self.score += grid[row][col]
        return grid

    def reverse(self, grid):
        new_grid = []
        for row in grid:
            new_grid.append(row[::-1])
        return new_grid

    def transpose(self, grid):
        new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                new_grid[row][col] = grid[col][row]
        return new_grid

    def move_left(self):
        new_grid = self.compress(self.grid)
        new_grid = self.merge(new_grid)
        new_grid = self.compress(new_grid)
        if self.grid != new_grid:
            self.grid = new_grid
            return True
        return False

    def move_right(self):
        new_grid = self.reverse(self.grid)
        new_grid = self.compress(new_grid)
        new_grid = self.merge(new_grid)
        new_grid = self.compress(new_grid)
        new_grid = self.reverse(new_grid)
        if self.grid != new_grid:
            self.grid = new_grid
            return True
        return False

    def move_up(self):
        new_grid = self.transpose(self.grid)
        new_grid = self.compress(new_grid)
        new_grid = self.merge(new_grid)
        new_grid = self.compress(new_grid)
        new_grid = self.transpose(new_grid)
        if self.grid != new_grid:
            self.grid = new_grid
            return True
        return False

    def move_down(self):
        new_grid = self.transpose(self.grid)
        new_grid = self.reverse(new_grid)
        new_grid = self.compress(new_grid)
        new_grid = self.merge(new_grid)
        new_grid = self.compress(new_grid)
        new_grid = self.reverse(new_grid)
        new_grid = self.transpose(new_grid)
        if self.grid != new_grid:
            self.grid = new_grid
            return True
        return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = Game2048()
    game.show()
    sys.exit(app.exec())
