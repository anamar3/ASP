"""Generates all possible truth assignments for facts."""

from itertools import product

def generate_models(facts) -> list[dict[str, bool]]:
    """Generates all possible truth assignments for facts."""
    fact_names = sorted(list(set(fact.split("(")[0] for fact in facts)))
    models = list(product([True, False], repeat=len(fact_names)))
    return [dict(zip(fact_names, model)) for model in models]
