from abc import ABC, abstractmethod


class Character(ABC):
    """Base abstract character class."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change character state to dead."""
        pass


class Stark(Character):
    """Stark family character."""

    def die(self):
        """Kill the character."""
        self.is_alive = False
