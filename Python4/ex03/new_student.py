"""Student dataclass with auto-generated fields."""
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random 15-character lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student dataclass with name, surname, active status, login, and ID."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Initialize login and id after dataclass initialization."""
        self.login = self.surname.capitalize()
        self.id = generate_id()


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
