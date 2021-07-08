import arcade

# Game Constants.
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
MOVEMENT_SPEED = 5

# Window Properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 150


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,
                         "Sprites with Walls Examples")
        self.view_left = 0
        self.view_bottom = 0
        self.physics_engine = None

        self.player_sprite = None
        self.player_list = None
        self.wall_list = None

        self.score = 0

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0  # Reset the score.

        self.player_sprite = arcade.Sprite("character1.png",  # Filepath to image.
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.wall_list)

        # Manually create, position boxes.
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # Create a row of boxes using a loop.
        for x in range(173, 650, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        coordinate_list = [[400, 500], [470, 500], [400, 570], [470, 570]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):  # Tie controls to player.
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):  # Halt player.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.physics_engine.update()

        # Move the screen depending on how the players exceeds boundaries.
        boundary_changed = False

        # Scroll to the Left.
        boundary_left = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < boundary_left:
            self.view_left -= boundary_left - self.player_sprite.left
            boundary_changed = True

        # Scroll to the Right.
        boundary_right = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > boundary_right:
            self.view_left += self.player_sprite.right - boundary_right
            boundary_changed = True

        # Scroll to the Up.
        boundary_top = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > boundary_top:
            self.view_bottom += self.player_sprite.top - boundary_top
            boundary_changed = True

        # Scroll to the Down.
        boundary_bottom = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < boundary_bottom:
            self.view_bottom -= boundary_bottom - self.player_sprite.bottom
            boundary_changed = True

        # Ensure boundary values are integers.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If boundary values were changed, make the view port match.
        if boundary_changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
