"""Parses an ASP program into facts, rules, and constraints."""

def parse_asp_program(lines) -> tuple[list[str], list[str], list[str]]:
    """Parses an ASP program into facts, rules, and constraints."""
    facts = []
    rules = []
    constraints = []
    
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:  # Skip empty lines
            continue
        if ":-" in line:  # Rules or constraints
            if line.startswith(":-"):
                constraints.append(line)
            else:
                rules.append(line)
        else:  
            facts.append(line)
    
    return facts, rules, constraints
