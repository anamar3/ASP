"""Module for saving data to a file."""

def save_to_file(filename, facts, rules, constraints, more_facts) -> None:
    """Saves data in the correct order."""
    with open(filename, "w") as file:
        file.write("% Facts\n")
        for fact in facts:
                file.write(f"{fact}\n")
        file.write("\n")

        file.write("% Rules\n")
        for rule in rules:
            file.write(f"{rule}\n")
        file.write("\n")

        file.write("% Constraints\n")
        for constraint in constraints:
            file.write(f"{constraint}\n")
        file.write("\n")

        file.write("% More Facts\n")
        for m_fact in more_facts:
            file.write(f"{m_fact}\n")
