import arcade


class MyGameWindow(arcade.Window):


    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.ANTIQUE_FUCHSIA)

        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 150

        self.player_x = 100
        self.player_y = 100
        self.player_speed = 250
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.c_x, self.c_y, 50,  arcade.color.PURPLE_PIZZAZZ, 20)
        arcade.draw_circle_outline(self.player_x, self.player_y, 50, arcade.color.GOLD, 2, 20)


    def update(self, delta_time):
        self.c_x += self.x_speed * delta_time
        self.c_y += self.y_speed * delta_time

        if self.c_x > 1280 - 50 or self.c_x < 0 + 50:
            self.x_speed *= -1
        if self.c_y > 720 - 50 or self.c_y < 0 + 50:
            self.y_speed *= -1

        if self.right:
            self.player_x += self.player_speed * delta_time
        if self.left:
            self.player_x -= self.player_speed * delta_time
        if self.up:
            self.player_x += self.player_speed * delta_time
        if self.down:
            self.player_x -= self.player_speed * delta_time

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


MyGameWindow(1280, 720, "Basic Bounce")
arcade.run()
