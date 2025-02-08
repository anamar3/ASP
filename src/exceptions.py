"""This module contains the exceptions that are raised in the program."""

class ContradictingConstraints(Exception):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return f"Contradicting constraints!"
    
class WrongFact(Exception):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return f"Should start with a fact from Facts!"
    
class InvalidSyntax(Exception):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return f"Problem with the syntax!"
