"""Grounded rules generation."""

from typing import List, Dict

def ground_rules(rules, facts) -> List[Dict[str, List[str]]]:
    """Generates grounded versions of rules using constants."""
    grounded_rules = []
    constants = extract_constants(facts)
    for rule in rules:
        head, body = rule.split(":-")
        for constant in constants:
            grounded_head = head.replace("X", constant).strip()
            grounded_body = [b.strip().replace("X", constant) for b in body.split(",")]
            grounded_rules.append({"head": grounded_head, "body": grounded_body})
    return grounded_rules


def extract_constants(facts)-> set[str]:
    """Extracts all constants from facts."""
    constants = set()
    for fact in facts:
        if "(" in fact:
            args = fact.split("(")[1].split(")")[0].split(",")
            constants.update(arg.strip() for arg in args)  # Strip whitespace
    return constants
