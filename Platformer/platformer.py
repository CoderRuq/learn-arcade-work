import arcade

# Window Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Platformer"

# Viewport Margins
# or how far between the character and the edge of the screen.
VIEWPORT_MARGIN_TOP = 100
VIEWPORT_MARGIN_BOTTOM = 50
VIEWPORT_MARGIN_LEFT = 250
VIEWPORT_MARGIN_RIGHT = 250

# Sprite Constants
CHARACTER_SCALE = 1
TILE_SCALE = 0.5
COIN_SCALE = 0.5

# Gameplay Constants
PLAYER_MOVEMENT_SPEED = 5
PLAYER_JUMP_SPEED = 20
GRAVITY = 1.25


class Platformer(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Game elements.
        self.player = None
        self.walls = None
        self.coins = None

        self.player_sprite = None

        self.physics_engine = None

        # Keep track of scrolling.
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """Initial setup of game, can be called anytime to reset state of game."""
        # Initialize Sprite Lists.
        self.player = arcade.SpriteList()
        self.walls = arcade.SpriteList(use_spatial_hash=True)
        self.coins = arcade.SpriteList(use_spatial_hash=True)

        # Set up player.
        image = "images/player_1/player_stand.png"
        self.player_sprite = arcade.Sprite(image, CHARACTER_SCALE)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player.append(self.player_sprite)

        # Create ground tiles.
        for x in range(0, 1250, 64):
            image = "images/tiles/grassMid.png"
            ground = arcade.Sprite(image, TILE_SCALE)
            ground.center_x = x
            ground.center_y = 32  # Ground level.
            self.walls.append(ground)

        # Place some crates on the ground.
        crate_coordinates = [[512, 96], [256, 96], [768, 96]]
        for coordinate in crate_coordinates:
            image = "images/tiles/boxCrate_double.png"
            crate = arcade.Sprite(image, TILE_SCALE)
            crate.position = coordinate
            self.walls.append(crate)

        # Enable Physics.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.walls,
                                                             GRAVITY)

    def on_draw(self):
        arcade.start_render()

        self.walls.draw()
        self.coins.draw()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        """Allow the player to move."""
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Cease player movement upon key press stopping."""
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        # Change viewport as needed.
        did_viewport_change = False

        """Scroll as the character moves at the edge(s)."""
        viewport_boundary_top = self.view_bottom + SCREEN_HEIGHT \
            - VIEWPORT_MARGIN_TOP
        viewport_boundary_bottom = self.view_bottom + VIEWPORT_MARGIN_BOTTOM
        viewport_boundary_left = self.view_left + VIEWPORT_MARGIN_LEFT
        viewport_boundary_right = self.view_left + SCREEN_WIDTH \
            - VIEWPORT_MARGIN_RIGHT

        if self.player_sprite.top > viewport_boundary_top:
            self.view_bottom += self.player_sprite.top \
                                - viewport_boundary_top
            did_viewport_change = True
        if self.player_sprite.bottom < viewport_boundary_bottom:
            self.view_bottom -= viewport_boundary_bottom \
                                - self.player_sprite.bottom
            did_viewport_change = True
        if self.player_sprite.left < viewport_boundary_left:
            self.view_left -= viewport_boundary_left - self.player_sprite.left
            did_viewport_change = True
        if self.player_sprite.right > viewport_boundary_right:
            self.view_left += self.player_sprite.right - viewport_boundary_right
            did_viewport_change = True

        if did_viewport_change:
            # Only scroll in integer increments.
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Scroll
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    window = Platformer()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()