import random
import arcade


# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_STONE = .15
COIN_COUNT = 50
STONE_COUNT = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"

class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.rock_list = None
        self.Game_Over = False

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin3.wav")
        self.horrible_death_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):



        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.rock_list = arcade.SpriteList(use_spatial_hash=True)

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        player = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player_sprite = arcade.Sprite(player, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

        for x in range(0-8, 14):

            stone = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING_STONE)

            stone.center_x = random.randrange(SCREEN_WIDTH)
            stone.center_y = random.randrange(SCREEN_HEIGHT)
            self.rock_list.append(stone)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()
        self.rock_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)
        if self.Game_Over == True:
            arcade.draw_text("GAME OVER", start_x=250, start_y=400, color= arcade.color.RADICAL_RED,font_size = 30)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):


        if self.Game_Over == False:

            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.collect_coin_sound)

        collision = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)
        if len(collision) > 0:
            arcade.play_sound(self.horrible_death_sound)
            self.Game_Over == True


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
