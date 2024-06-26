import arcade
import random

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
HOP_DISTANCE = 50
FLY_COUNT = 2

DEFAULT_SPEED = 10
speed_multiplier = 1.0

class Movers(arcade.Sprite):
    MOVERS_SPEED = DEFAULT_SPEED * 0.76  

    def reset_pos(self):
        self.center_y = SCREEN_HEIGHT // 2 - 10
        self.center_x = -self.width / 2

    def move(self):
        self.center_x += self.MOVERS_SPEED * speed_multiplier
        if self.right > SCREEN_WIDTH + self.width:
            self.reset_pos()

    def collide_with_sprite(self, sprite):
        return self.collides_with_sprite(sprite)


class Firetruck(arcade.Sprite):
    FIRETRUCK_SPEED = DEFAULT_SPEED / 2 

    def reset_pos(self):
        self.center_y = SCREEN_HEIGHT - 252  
        self.center_x = -self.width / 2

    def move(self):
        self.center_x += self.FIRETRUCK_SPEED * speed_multiplier
        if self.left > SCREEN_WIDTH:
            self.reset_pos()

    def collide_with_sprite(self, sprite):
        return self.collides_with_sprite(sprite)

class Yuvers(arcade.Sprite):
    YELLOW_SPEED = DEFAULT_SPEED * 1.3
    def reset_pos(self):
        self.center_y = SCREEN_HEIGHT - 550
        self.center_x = SCREEN_WIDTH + self.width / 2

    def move(self):
        self.center_x -= DEFAULT_SPEED * speed_multiplier
        if self.left < -self.width:
            self.reset_pos()

    def collide_with_sprite(self, sprite):
        return self.collides_with_sprite(sprite)

class Bluvers(arcade.Sprite):
    def __init__(self, filename, scale=1):
        super().__init__(filename, scale=scale)
        self.reset_pos()

    def reset_pos(self):
        self.center_y = SCREEN_HEIGHT - 170
        self.center_x = SCREEN_WIDTH + self.width / 2

    def move(self):
        self.center_x -= DEFAULT_SPEED * speed_multiplier
        if self.left < -self.width:
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
        self.highest_score = 0 
        self.in_goal_zone = False
        self.frogger_x = 50
        self.frogger_y = 50
        self.hop = False

        self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png", scale=0.55, center_x=300,
                                                    center_y=80)
        self.roadkill_sprite = arcade.Sprite("Frogger/Roadkill.png", scale=0.55)

        self.roadkill_sprite.center_x = -500
        self.roadkill_sprite.center_y = -500

        self.frogger_list.append(self.frogger_default_sprite)
        self.frogger_list.append(self.roadkill_sprite)

        self.bigrig_sprite = Movers("obstacles/bigrig.png")
        self.obstacle_list.append(self.bigrig_sprite)
        self.bigrig_sprite.reset_pos()

        self.firetruck_sprite = Firetruck("obstacles/firetruck.png")
        self.obstacle_list.append(self.firetruck_sprite)
        self.firetruck_sprite.reset_pos()

        self.yuver_sprite = Yuvers("obstacles/yellow_car.png")
        self.obstacle_list.append(self.yuver_sprite)
        self.yuver_sprite.reset_pos()

        self.bluvers_sprite2 = Bluvers("obstacles/blue_car.png")
        self.bluvers_sprite2.center_y = SCREEN_HEIGHT - 150
        self.obstacle_list.append(self.bluvers_sprite2)

        if self.frogger_y >= (4.5 / 5) * SCREEN_HEIGHT:
            self.in_goal_zone = True
            self.goal_reached = True
            self.goal_timer += delta_time
            if self.goal_timer >= 1:
                self.goal_reached = False
                self.goal_timer = 0
                self.reset_frogger_position()
                self.score += 1000
                speed_multiplier *= 1.1

                self.fly_list = arcade.SpriteList()
                for _ in range(FLY_COUNT):
                    fly_sprite = arcade.Sprite("fly/fly.png", scale=0.45,
                                               center_x=random.randrange(SCREEN_WIDTH),
                                               center_y=random.randrange(SCREEN_HEIGHT))
                    self.fly_list.append(fly_sprite)

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.game_over = False
        self.goal_reached = False
        self.goal_timer = 0

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT, SCREEN_WIDTH, 100, arcade.color.FERN_GREEN)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200, SCREEN_WIDTH, 230, arcade.color.DIRT)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 9, SCREEN_WIDTH, SCREEN_HEIGHT // 5,
                                     arcade.color.FERN_GREEN)

      
        arcade.draw_line(0, SCREEN_HEIGHT - 200, SCREEN_WIDTH, SCREEN_HEIGHT - 200, arcade.color.WHITE, 5)

        for i in range(1, 4):
            y = i * SCREEN_HEIGHT // 5
            arcade.draw_line(0, y, SCREEN_WIDTH, y, arcade.color.YELLOW, 3)
            arcade.draw_line(0, y + 3, SCREEN_WIDTH, y + 3, arcade.color.YELLOW, 3)
        self.fly_list.draw()
        self.obstacle_list.draw()
        self.frogger_default_sprite.draw()

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, 20, SCREEN_WIDTH, 40, arcade.color.ALMOND)

        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20, color=arcade.color.BLUE_VIOLET, font_size=20)

        
        arcade.draw_text(f"Highest Score: {self.highest_score}", SCREEN_WIDTH - 10, 20, arcade.color.RED,
                         font_size=20, anchor_x="right")

        if self.game_over:
            arcade.draw_text("Game Over. Try again? (Y/N)", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE,
                             font_size=24, anchor_x="center", anchor_y="center")

            self.roadkill_sprite.draw()

        if self.goal_reached:
            arcade.draw_text("GOAL!!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE,
                             font_size=36, anchor_x="center", anchor_y="center")

    def on_update(self, delta_time):
        global speed_multiplier
        if not self.game_over:
            if self.frogger_x > 600 - 50:
                self.frogger_x = 550
            if self.frogger_x < 0 + 50:
                self.frogger_x = 50
            if self.frogger_y > 800 - 50:
                self.frogger_y = 750
            if self.frogger_y < 0 + 50:
                self.frogger_y = 50
            self.frogger_default_sprite.set_position(self.frogger_x, self.frogger_y)

            self.obstacle_list.update()
            self.bigrig_sprite.move()
            self.bluvers_sprite2.move()
            self.firetruck_sprite.move()
            self.yuver_sprite.move()

            if self.bigrig_sprite.collide_with_sprite(self.frogger_default_sprite):
                self.game_over = True
                self.roadkill_sprite.set_position(self.frogger_x, self.frogger_y)
                self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")

            if self.firetruck_sprite.collide_with_sprite(self.frogger_default_sprite):
                self.game_over = True
                self.roadkill_sprite.set_position(self.frogger_x, self.frogger_y)
                self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")

            if self.bluvers_sprite2.collide_with_sprite(self.frogger_default_sprite):
                self.game_over = True
                self.roadkill_sprite.set_position(self.frogger_x, self.frogger_y)
                self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")

            if self.yuver_sprite.collides_with_sprite(self.frogger_default_sprite):
                self.game_over = True
                self.roadkill_sprite.set_position(self.frogger_x, self.frogger_y)
                self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png")


            if self.frogger_y >= (4.5 / 5) * SCREEN_HEIGHT:
                self.goal_reached = True
                self.goal_timer += delta_time
                if self.goal_timer >= 1:
                    self.goal_reached = False
                    self.goal_timer = 0
                    self.reset_frogger_position()
                    self.score += 1000
                    speed_multiplier *= 1.1

                   
                    self.fly_list = arcade.SpriteList()
                    for _ in range(FLY_COUNT):
                        fly_sprite = arcade.Sprite("fly/fly.png", scale=0.45,
                                                   center_x=random.randrange(SCREEN_WIDTH),
                                                   center_y=random.randrange(SCREEN_HEIGHT))
                        self.fly_list.append(fly_sprite)

           
            if self.score > self.highest_score:
                self.highest_score = self.score

    def reset_frogger_position(self):
        self.frogger_x = SCREEN_WIDTH // 2
        self.frogger_y = SCREEN_HEIGHT // 9 + 40

    def restart_game(self):
        self.score = 0
        self.game_over = False
        self.reset_frogger_position()

     
        self.frogger_default_sprite = arcade.Sprite("Frogger/frogger_default.png", scale=0.55)

        global speed_multiplier
        speed_multiplier = 1.0

        self.obstacle_list = arcade.SpriteList()
        self.bigrig_sprite = Movers("obstacles/bigrig.png")
        self.obstacle_list.append(self.bigrig_sprite)
        self.bigrig_sprite.reset_pos()

        
        self.bluvers_sprite2.reset_pos()

        self.obstacle_list.append(self.bluvers_sprite2)

        self.obstacle_list.append(self.yuver_sprite)
        self.obstacle_list.append(self.firetruck_sprite)

        self.firetruck_sprite.reset_pos()

        self.fly_list = arcade.SpriteList()
        for _ in range(FLY_COUNT):
            fly_sprite = arcade.Sprite("fly/fly.png", scale=0.45, center_x=random.randrange(SCREEN_WIDTH),
                                       center_y=random.randrange(SCREEN_HEIGHT))
            self.fly_list.append(fly_sprite)

        self.goal_reached = False
        self.goal_timer = 0

    def on_key_press(self, symbol, modifiers):
        if not self.game_over:
            if symbol == arcade.key.RIGHT:
                self.frogger_x += HOP_DISTANCE
            elif symbol == arcade.key.LEFT:
                self.frogger_x -= HOP_DISTANCE
            elif symbol == arcade.key.UP:
                self.frogger_y += HOP_DISTANCE
                self.score += 10
            elif symbol == arcade.key.DOWN:
                self.frogger_y -= HOP_DISTANCE
        else:
            if symbol == arcade.key.Y:
                self.restart_game()

    def on_key_release(self, symbol):
        pass

    def update(self, delta_time):
        if not self.game_over:
            self.fly_list.update()
            fly_hit_list = arcade.check_for_collision_with_list(self.frogger_default_sprite, self.fly_list)

            for fly in fly_hit_list:
                fly.remove_from_sprite_lists()
                self.score += 100


GameWindow(600, 800, "FROGGER CLONE")
arcade.run()

