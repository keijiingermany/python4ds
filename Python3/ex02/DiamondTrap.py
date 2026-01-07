from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King with conflicting heritage."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Set eye color."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set hair color."""
        self.hairs = color

    def get_eyes(self):
        """Get eye color."""
        return self.eyes

    def get_hairs(self):
        """Get hair color."""
        return self.hairs
