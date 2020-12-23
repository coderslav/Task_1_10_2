class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width*self.height


rectangle = Rectangle(5, 10)
print(f"Ш: {rectangle.get_width()}\nД: {rectangle.get_height()}\nS: {rectangle.get_area()}")

