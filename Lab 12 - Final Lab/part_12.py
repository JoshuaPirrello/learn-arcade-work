import arcade
import random

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
HOP_DISTANCE = 50
FLY_COUNT = 2

class Movers(arcade.Sprite):
    def reset_pos(self):
        self.center_y = SCREEN_HEIGHT // 2 - 10  # Adjusted initial position
        self.center_x = -self.width / 2  # Start from left side of the screen

    def move(self):
        self.center_x += 10  # Move from left to right
        if self.right > SCREEN_WIDTH + self.width:  # Check if bigrig goes off-screen
            self.reset_pos()

    def collide_with_sprite(self, sprite):
        return self.collides_with_sprite(sprite)


class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        self.frogger_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()
        self.score = 0

        self.frogger_x = 50
        self.frogger_y = 50
        self.hop = False

        self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png", center_x= 300, center_y= 80)
        self.frogger_about_to_jump_sprite = arcade.Sprite("Frogger/frogger_about_to_jump.png")
        self.frogger_start_jump_sprite = arcade.Sprite("Frogger/frogger_start_jump.png")
        self.frogger_landing_sprite = arcade.Sprite("Frogger/frogger_landing.png")
        self.frogger_mid_jump_sprite = arcade.Sprite("Frogger/frogger_mid_jump.png")
        self.frogger_peak_jump_sprite = arcade.Sprite("Frogger/frogger_peak_jump.png")
        self.roadkill_sprite = arcade.Sprite("Frogger/Roadkill.png")

        # Add frogger sprites to the list
        self.frogger_list.append(self.frogger_default_sprite)
        self.frogger_list.append(self.roadkill_sprite)
        # Create bigrig sprite and add to the obstacle list
        self.bigrig_sprite = Movers("obstacles/bigrig.png")
        self.obstacle_list.append(self.bigrig_sprite)
        self.bigrig_sprite.reset_pos()  # Call reset_pos to set initial position

        # Create and position the fly sprites
        for _ in range(FLY_COUNT):
            fly_sprite = arcade.Sprite("fly/fly.png", center_x=random.randrange(SCREEN_WIDTH),
                                       center_y=random.randrange(SCREEN_HEIGHT))
            self.fly_list.append(fly_sprite)

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.frogger_default_sprite.angle = 0
        self.frogger_direction = "right"

        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 9, SCREEN_WIDTH, SCREEN_HEIGHT // 5, arcade.color.FERN_GREEN)

        # Draw horizontal lanes
        for i in range(4):
            y = (i + 1) * SCREEN_HEIGHT // 5
            arcade.draw_line(0, y, SCREEN_WIDTH, y, arcade.color.WHITE, 5)

            # Draw double yellow line between two lanes
        for i in range(1, 4):
            y = i * SCREEN_HEIGHT // 5
            arcade.draw_line(0, y, SCREEN_WIDTH, y, arcade.color.YELLOW, 3)
            arcade.draw_line(0, y + 3, SCREEN_WIDTH, y + 3, arcade.color.YELLOW, 3)

        # Draw sprites and UI elements
        self.fly_list.draw()
        self.obstacle_list.draw()
        self.frogger_default_sprite.draw()

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, 20, SCREEN_WIDTH, 40, arcade.color.ALMOND)

        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20, color=arcade.color.BLUE_VIOLET, font_size=20)

        if self.game_over:
            arcade.draw_text("Game Over. Try again? (Y/N)", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE,
                             font_size=24, anchor_x="center", anchor_y="center")

            # Draw roadkill sprite on top if game over
            self.roadkill_sprite.draw()

    def on_update(self, delta_time):
        if not self.game_over:
            if self.frogger_x > 600 - 50:
                self.frogger_x = 550
            if self.frogger_x < 0 + 50:
                self.frogger_x = 50
            if self.frogger_y > 800 - 50:
                self.frogger_y = 750
            if self.frogger_y < 0 + 50:
                self.frogger_y = 50
            if self.frogger_direction == "right":
                self.frogger_default_sprite.angle = 0
            elif self.frogger_direction == "left":
                self.frogger_default_sprite.angle = 180
            self.frogger_default_sprite.set_position(self.frogger_x, self.frogger_y)

            self.obstacle_list.update()
            self.bigrig_sprite.move()

            # Check for collision with bigrig
            if self.bigrig_sprite.collide_with_sprite(self.frogger_default_sprite):
                self.game_over = True
                # Set roadkill sprite position to Frogger's position
                self.roadkill_sprite.set_position(self.frogger_x, self.frogger_y)
                # Reset frogger sprite to default on collision
                self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")

    def reset_frogger_position(self):
        # Reset frogger position to starting position
        self.frogger_x = 50
        self.frogger_y = 50

    def restart_game(self):
        # Reset game variables
        self.score = 0
        self.game_over = False
        self.reset_frogger_position()
        # Reset frogger sprite to default on restart
        self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")

    def on_key_press(self, symbol, modifiers):
        if not self.game_over:
            if symbol == arcade.key.RIGHT:
                self.hop = True
                self.frogger_x += HOP_DISTANCE
            if symbol == arcade.key.LEFT:
                self.hop = True
                self.frogger_x -= HOP_DISTANCE
            if symbol == arcade.key.UP:
                self.hop = True
                self.frogger_y += HOP_DISTANCE
            if symbol == arcade.key.DOWN:
                self.hop = True
                self.frogger_y -= HOP_DISTANCE
        else:
            if symbol == arcade.key.Y:
                self.restart_game()

    def on_key_release(self, symbol):
                self.hop = False

    def update(self, delta_time):
                if not self.game_over:
                    self.fly_list.update()
                    fly_hit_list = arcade.check_for_collision_with_list(self.frogger_default_sprite, self.fly_list)

                    for fly in fly_hit_list:
                        fly.remove_from_sprite_lists()
                        self.score += 10

GameWindow(600, 800, "FROGGER CLONE")
arcade.run()

