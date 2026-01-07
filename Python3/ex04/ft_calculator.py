class calculator:
    """Vector operations calculator."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Dot product."""
        result = sum(a * b for a, b in zip(v1, v2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Add vectors."""
        print(f"Add Vector is : {[float(a + b) for a, b in zip(v1, v2)]}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Subtract vectors."""
        print(f"Sous Vector is: {[float(a - b) for a, b in zip(v1, v2)]}")
