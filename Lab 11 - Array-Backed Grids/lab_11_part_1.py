import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10
WIDTH = 20
HEIGHT = 20
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Color and Grid Example"


class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([0] * COLUMN_COUNT)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.PINK
                else:
                    color = arcade.color.BLUE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT / 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x / (WIDTH + MARGIN))
        row = int(y / (HEIGHT + MARGIN))
        self.grid[row][column] = 1 if self.grid[row][column] == 0 else 0
        for r in range(max(0, row - 1), min(row + 2, ROW_COUNT)):
            self.grid[r][column] = 1 if self.grid[r][column] == 0 else 0
        for c in range(max(0, column - 1), min(column + 2, COLUMN_COUNT)):
            self.grid[row][c] = 1 if self.grid[row][c] == 0 else 0


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
