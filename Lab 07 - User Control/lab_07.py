import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, x, y, change_in_x, change_in_y, r, color):
        # Take the parameters of the init function above, and create instance.
        self.x = x  # X position.
        self.y = y  # Y position.
        self.change_in_x = change_in_x
        self.change_in_y = change_in_y
        self.r = r  # Ball radius.
        self.color = color

    def draw(self):
        """Draw the balls with the instance variables we have."""
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

    def update(self):
        # Move thy self.
        self.x += self.change_in_x
        self.y += self.change_in_y

        # See if the ball hit the edge of the screen. If so, change direction.
        if self.x < self.r:
            self.x = self.r

        if self.x > (SCREEN_WIDTH - self.r):
            self.x = SCREEN_WIDTH - self.r

        if self.y < self.r:
            self.y = self.r

        if self.y > (SCREEN_HEIGHT - self.r):
            self.y = SCREEN_HEIGHT - self.r




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function.
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create ball.
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """Called whenever we need to draw the window."""
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """Called whenever the user presses a key."""
        if key == arcade.key.LEFT:
            self.ball.change_in_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_in_x = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_in_y = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_in_y = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_in_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_in_y = 0

    # def on_mouse_motion(self, x, y, dx, dy):
    #     """Called to update our objects, 60 times a second."""
    #     self.ball.x = x
    #     self.ball.y = y

    # def on_mouse_press(self, x, y, button, modifiers):
    #     """Called when a mouse button is pressed."""
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         pass
    #     elif button == arcade.MOUSE_BUTTON_RIGHT:
    #         pass


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
