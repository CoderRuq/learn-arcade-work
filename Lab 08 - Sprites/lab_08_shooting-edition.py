import random
import arcade

# Game Constraints
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50
BULLET_SPEED = 5

# Window Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y -= 2
        # Check for when a coin goes off-screen.
        if self.top < 0:
            self.reset_position()

    def reset_position(self):
        # Move it back up top, but with a random position.
        self.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 1200)
        self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite Lists.
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Player information.
        self.player_sprite = None
        self.score = 0

    def setup(self):
        # Initialize Sprite Lists, Player.
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create coins.
        for i in range(COIN_COUNT):
            # Create an individual instance of coins.
            coin = Coin("coin_01.png", SPRITE_SCALING_COIN)  # Refactor?
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 1200)

            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        # Draw sprite lists.
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

        # Display score onscreen.
        score_display = f"Score: {self.score}"
        arcade.draw_text(score_display, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        # Keep player along a set Y axis.
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        # Create and add bullet to "bullet_list"
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.angle = 90

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED

        self.bullet_list.append(bullet)

    def update(self, delta_time):
        # Update all coin sprites.
        self.coin_list.update()
        self.bullet_list.update()

        # Generate a list of all coins that player contacts.
        coin_hit_list = \
            arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.coin_list)

        # Loop through each collided coin, reset it, and add 1 to the score.
        for coin in coin_hit_list:  # type: Coin
            # coin.remove_from_sprite_lists()
            coin.reset_position()
            self.score -= 10

        for bullet in self.bullet_list:
            bullet_hit_list = arcade.check_for_collision_with_list(
                bullet, self.coin_list)

            if len(bullet_hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for coin in bullet_hit_list:
                coin.reset_position()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
