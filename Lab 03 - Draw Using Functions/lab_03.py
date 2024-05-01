import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_moon():
    arcade.draw_circle_filled(50, SCREEN_HEIGHT - 50, 75, arcade.color.SUNSET)
    arcade.draw_circle_outline(50, SCREEN_HEIGHT - 50, 75, arcade.color.BLACK_BEAN)
def draw_snowman(x,y):
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(300 + x, 340 +y, radius=3, color=arcade.color.ORANGE_RED)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()
    draw_moon()
    draw_grass()
    draw_snowman(1, 1)
    draw_snowman(150, -10)
    draw_snowman( -100, -30)


    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
