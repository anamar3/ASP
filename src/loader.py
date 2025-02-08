"""This module provides functions to load ASP programs from files."""

def load_asp_file(filename) -> list[str]:
    """Reads an ASP program from a file."""
    with open(filename, "r") as file:
        lines = file.readlines()
    program = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("%"):  # Ignore empty lines and comments
            program.append(line)
    return program
