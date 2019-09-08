

class Point():
    """This is a doc string for the class"""
    
    def __init__(self, x, y):
        """This is a doc string for the __init__ method"""
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_val):
        self.x = new_val

    def set_y(self, new_val):
        self.y = new_val

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)
    
