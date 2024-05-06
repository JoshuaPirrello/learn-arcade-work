import arcade


class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)
        self.score = 0
        self.frogger_x = 100
        self.frogger_y = 100
        self.vehicle_x = 150
        self.vehicle_y = 150

        self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png", center_x= 300, center_y= 50)
        self.frogger_about_to_jump_sprite = arcade.Sprite("Frogger/frogger_about_to_jump.png")
        self.frogger_start_jump_sprite = arcade.Sprite("Frogger/frogger_start_jump.png")
        self.frogger_landing_sprite = arcade.Sprite("Frogger/frogger_landing.png")
        self.frogger_mid_jump_sprite = arcade.Sprite("Frogger/frogger_mid_jump.png")
        self.frogger_peak_jump_sprite = arcade.Sprite("Frogger/frogger_peak_jump.png")
        self.roadkill_sprite = arcade.Sprite("Frogger/Roadkill.png")

        self.fly_sprite = arcade.Sprite("fly/fly.png", center_x= 550, center_y =500)
        self.bigrig_sprite = arcade.Sprite("obstacles/bigrig.png", center_x= 300, center_y= 600)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        self.frogger_default_sprite.draw()
        self.fly_sprite.draw()
        arcade.draw_rectangle_filled(self.vehicle_x, self.vehicle_y, 75, 25, arcade.color.RED)

    def on_update(self, delta_time):
        if self.right:
            self.frogger_default_sprite.turn_right(2)
            self.frogger_x += 5
        if self.left:
            self.frogger_default_sprite.turn_left(2)
            self.frogger_x -= 5
        if self.up:
            self.frogger_y += 5
        if self.down:
            self.frogger_y -= 5
        self.frogger_default_sprite.set_position(self.frogger_x, self.frogger_y)

        self.vehicle_x -= self.vehicle_x * delta_time
        self.vehicle_y -= self.vehicle_y * delta_time

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

class Lane:
 def __init__(self, row=-1, lanetype="none", direction=0, speed=0, width=0, maxnumber=0, replenish=0, length=0, gap=0):
  self.row = row
  self.type = lanetype
  self.direction = direction
  self.speed = speed
  self.width = width
  self.maxnumber = maxnumber
  self.replenish = replenish
  self.length = length
  self.gap = gap
  self.lanelastupdate = 0
  self.objects = []

class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image


GameWindow(600, 800, "FROGGER CLONE")
arcade.run()
