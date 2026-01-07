class calculator:
    """Vector calculator."""

    def __init__(self, values: list[float]):
        self.values = values

    def __add__(self, scalar):
        self.values = [v + scalar for v in self.values]
        print(self.values)

    def __mul__(self, scalar):
        self.values = [v * scalar for v in self.values]
        print(self.values)

    def __sub__(self, scalar):
        self.values = [v - scalar for v in self.values]
        print(self.values)

    def __truediv__(self, scalar):
        if scalar == 0:
            print("Error: division by zero")
            return
        self.values = [v / scalar for v in self.values]
        print(self.values)
