import arcade

# Grid Properties
TILE_WIDTH, TILE_HEIGHT = (20, 20)
GRID_MARGIN = 5
ROWS, COLUMNS = (10, 10)

# Window Properties
# N.B. how the window size is calculated by the grid properties.
SCREEN_WIDTH = (ROWS * TILE_WIDTH) + \
               (GRID_MARGIN * (ROWS + 1))
SCREEN_HEIGHT = (COLUMNS * TILE_HEIGHT) + \
                (GRID_MARGIN * (COLUMNS + 1))

BACKGROUND_COLOR = arcade.color.BLACK


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """Render screen. Must put drawing elements AFTER 'start_render()'."""
        arcade.start_render()

        for row in range(ROWS):
            for column in range(COLUMNS):
                arcade.draw_rectangle_filled(
                    center_x=GRID_MARGIN + (TILE_WIDTH/2) +
                    (GRID_MARGIN * (column * 5)),
                    center_y=GRID_MARGIN + (TILE_HEIGHT/2) +
                    (GRID_MARGIN * (row * 5)),
                    width=TILE_WIDTH,
                    height=TILE_HEIGHT,
                    color=arcade.color.WHITE
                )

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()