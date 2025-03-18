from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class of a character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and an alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method for die"""
        pass


class Stark(Character):
    """Class representing House Stark"""

    def die(self):
        """Kills the member of the stark family
        by setting is_alive attribute to Flase"""
        self.is_alive = False
