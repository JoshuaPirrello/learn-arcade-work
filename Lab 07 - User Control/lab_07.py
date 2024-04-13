import arcade


class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 300
        self.red_x = 500
        self.red_y = 500

        self.player_x = 100
        self.player_y = 100
        self.player_speed = 250
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        screen_width = 600
        screen_height = 600
        arcade.draw_lrtb_rectangle_filled(0, screen_height, screen_width / 3, 0, arcade.color.GUPPIE_GREEN)
        arcade.draw_rectangle_filled(15, 115, 14, 80, arcade.color.REDWOOD)
        arcade.draw_circle_filled(25, 225, 75, arcade.color.FERN_GREEN)
        arcade.draw_rectangle_filled(215, 115, 14, 80, arcade.color.REDWOOD)
        arcade.draw_circle_filled(225, 225, 75, arcade.color.FERN_GREEN)
        arcade.draw_rectangle_filled(415, 115, 14, 550, arcade.color.REDWOOD)
        arcade.draw_circle_filled(425, 425, 75, arcade.color.FERN_GREEN)
        arcade.draw_circle_filled(50, screen_height - 50, 75, arcade.color.SUNSET)
        arcade.draw_circle_outline(50, screen_height - 50, 75, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(self.c_x, self.c_y, 50, arcade.color.PURPLE_PIZZAZZ, 20)
        arcade.draw_circle_filled(self.player_x, self.player_y, 70, arcade.color.WHITE)
        arcade.draw_circle_filled(self.player_x, self.player_y, 50, arcade.color.OCEAN_BOAT_BLUE, 2, 20)
        arcade.draw_ellipse_filled(self.player_x, self.player_y, screen_width / 20, screen_height / 15, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(self.red_x, self.red_y, 70, arcade.color.WHITE)
        arcade.draw_circle_filled(self.red_x, self.red_y, 50, arcade.color.RED_DEVIL, 20)
        arcade.draw_ellipse_filled(self.red_x, self.red_y, screen_width/20, screen_height/15, arcade.color.BLACK_OLIVE)

    def on_update(self, delta_time):
        self.c_x += self.x_speed * delta_time
        self.c_y += self.y_speed * delta_time

        if self.c_x > 600 - 50 or self.c_x < 0 + 50:
            self.x_speed *= -1
        if self.c_y > 600 - 50 or self.c_y < 0 + 50:
            self.y_speed *= -1

        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_y += self.player_speed * delta_time
        if self.down:
            self.player_y -= self.player_speed * delta_time

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.red_x = x
            self.red_y = y
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.red_x = x
            self.red_y = y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.red_x = x
        self.red_y = y


GameWindow(600, 600, "Witch's Eyes over spooky forest ")
arcade.run()
