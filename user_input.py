"""This module is the entry point of the program. 
It allows the user to choose between entering facts manually or providing a file path to an ASP program. 
It then processes the input and displays the options available to the user."""

from src.process_input import get_facts, get_more_facts, get_rules, get_constraints
from src.save_input import save_to_file
from src.loader import load_asp_file
from src.options import display_options
from src.parser import parse_asp_program


def main() -> None:

    choice = input("1. Enter facts manually\n2. Provide a file path\nChoose (1 or 2): ").strip()
    filepath: str

    if choice == "1":
        facts = get_facts()
        more_facts = get_more_facts(facts)
        rules = get_rules(facts, more_facts)
        constraints = get_constraints(facts, rules)
        filepath = input("Enter filename to save ASP program: ").strip()
        save_to_file(filepath, facts, rules, constraints, more_facts)
        print(f"ASP program saved to {filepath}.")
        facts.extend(more_facts)
        display_options(facts,rules,constraints)

    elif choice == "2":
        filepath = input("Enter the path to your ASP file: ").strip()
        facts, rules, constraints = parse_asp_program(load_asp_file(filepath))
        display_options(facts,rules,constraints)

if __name__ == "__main__":
    main()

