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
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """

        super().__init__(width, height, title)
        self.grid = []
        for row in range(ROW_COUNT):

            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.PINK
                else:
                    color = arcade.color.BLUE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH/2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT/2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x/(WIDTH + MARGIN))
        row = int(y/(HEIGHT + MARGIN))

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
