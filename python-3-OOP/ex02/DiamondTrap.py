from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King to inherit from Baratheon and Lannister"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize King with Baratheon attributes"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, new_color):
        self.eyes = new_color

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, new_color):
        self.hairs = new_color
