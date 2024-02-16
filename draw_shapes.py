# by Kami Bigdely
# Extract superclass.
class Shape:
    """Represents a generic shape"""

    def __init__(self, x, y, visible=True):
        self.x = x
        self.y = y
        self.visible = visible

    def set_visible(self, is_visible):
        """Set visible property"""
        self.visible = is_visible

    def get_center(self):
        """Return the x and y coordinates of the center of the shape"""
        return self.x, self.y


class Circle(Shape):
    """Represents a circle inherits from shape"""

    def __init__(self, x, y, r, visible=True):
        super().__init__(x, y, visible)
        self.r = r

    def display(self):
        """Print message informing the user the circle was drawn."""
        print('drew the circle.')


class Rectangle(Shape):
    """Represents a rectangle inherits from shape"""

    def __init__(self, x, y, width, height, visible=True):
        # left-bottom corner.
        super().__init__(x, y, visible)
        self.width = width
        self.height = height

    def display(self):
        """Prints a message informing the use that the rectangle was drawn if visible property is true."""
        if self.visible:
            print('drew the rectangle.')

    def get_center(self):
        return self.x + self.width/2, \
            self.y + self.height/2


if __name__ == "__main__":
    circle = Circle(0, 0, 10, False)
    circle.set_visible(True)
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.set_visible(False)
    rect.display()  # does not display because it's hidden.
    rect.set_visible(True)
    rect.display()
    print('center point', rect.get_center())
