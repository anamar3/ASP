from typing import List

"""Module to process user input for facts, more facts, rules, and constraints."""

def get_facts() -> List[str]:
    """Gets multiple entities for a single fact in the format '<entity> is/are a/an <category>'."""
    
    facts = []  
    print("Enter Facts (format: '<entity> is/are a/an <category>') (empty line to stop):")
    
    category = None  # Store the category (fact)
    
    while True:
        fact = input("Fact: ").strip()
        
        if not fact:
            break  # Stop when the user enters an empty line
        
        parts = fact.split()
        
        if len(parts) >= 3 and (parts[1] in ["is", "are"] and parts[2] in ["a", "an"]):
            entity, fact_category = parts[0], parts[3]
        elif len(parts) >= 3 and parts[1] == "is":
            entity, fact_category = parts[0], parts[2]
        else:
            print("Invalid format! Try again.")
            continue
        
        if category is None:
            category = fact_category  # Set the category from the first input
        elif category != fact_category:
            print(f"Error: All entries must belong to the same category '{category}'. Try again.")
            continue
        
        fact_str = f"{fact_category}({entity})."  # Format fact properly
        
        if fact_str in facts:  
            print(f"Error: '{entity}' has already been added. Try again.")  # Prevent duplicate entries
            continue
        
        facts.append(fact_str)
    
    return facts


def get_more_facts(facts) -> list[str]:
    """Gets additional facts in the format '<entity> <property>' and ensures entity exists in facts."""
    
    more_facts = []
    fact_values = {fact.split("(")[1][:-2] for fact in facts}  # Extract entities from formatted facts
    
    print("Enter More Facts (format: '<entity> <property>') (empty line to stop):")
    
    while True:
        fact = input("More Fact: ").strip()
        if not fact:
            break

        parts = fact.split()
        if len(parts) != 2:
            print("Invalid format! Try again.")
            continue

        entity, prop = parts

        if entity not in fact_values:
            print(f"Error: '{entity}' is not defined in Facts. Try again.")
            continue

        fact_str = f"{prop}({entity})."

        if fact_str in more_facts:
            print(f"Error: '{fact_str}' has already been added. Try again.")
            continue

        if prop.startswith("cannot_") and f"{prop[7:]}({entity})." in more_facts:
            print(f"Error: \"{prop[7:]}({entity})\" is already defined as a fact. Try again.")
            
        s = "cannot_" + prop
        if f"{s}({entity})." in more_facts:
            print(f"Error: \"{s}({entity}).\" is already defined as a fact. Try again.")

        more_facts.append(fact_str)

    return more_facts

def get_rules(facts, more_facts) -> list[str]:
    """Gets rules in the format '<rule>(X) :- <fact>(X), (not) <more_fact>(X), ...'."""
    
    rules = []
    print("Enter Rules (format: '<rule> if <fact> (and not/and) <more_fact>') (empty line to stop):")

    fact = [fact.split('(')[0] for fact in facts]
    more_fact_values = [m_fact.split('(')[0] for m_fact in more_facts]

    while True:
        rule = input("Rule: ").strip()
        if not rule:
            break

        parts = rule.split(" if ")
        if len(parts) != 2:
            print("Invalid format! Try again.")
            continue

        rule_head = parts[0].strip()

        if rule_head in fact or rule_head in more_fact_values:
            print(f"Error: '{rule_head}' is already defined as a fact. Try again.")
            continue

        conditions = parts[1].split(" and ")

        first_condition = conditions[0].strip()
        if first_condition not in fact:
            print(f"Error: First condition '{first_condition}' must be from Facts. Try again.")
            continue
        formatted_conditions = [f"{first_condition}(X)"]

        valid_rule = True
        for condition in conditions[1:]:
            condition = condition.strip()
            if condition.startswith("not "):
                fact_name = condition[4:].strip()
                formatted_condition = f"not {fact_name}(X)"
            else:
                fact_name = condition
                formatted_condition = f"{fact_name}(X)"

            if fact_name not in more_fact_values:
                print(f"Error: '{fact_name}' must be from More Facts. Try again.")
                valid_rule = False

            if formatted_condition in formatted_conditions:
                print(f"Error: Duplicate condition '{condition}'. Try again.")
                valid_rule = False

            formatted_conditions.append(formatted_condition)

        if not valid_rule:
            continue

        if any(existing_rule.split("(")[0] == rule_head for existing_rule in rules):
            print(f"Error: A rule with the name '{rule_head}' already exists. Try again.")
            continue

        formatted_rule = f"{rule_head}(X) :- {', '.join(formatted_conditions)}."
        rules.append(formatted_rule)

    return rules


def get_constraints(facts, rules) -> list[str]:
    """Gets constraints in the format 'if <fact> should <rule>' or 'if <fact> should not <rule>'."""

    constraints = []
    usedRules = []
    print("Enter Constraints (format: 'if <fact> should <rule>' or 'if <fact> should not <rule>') (empty line to stop):")

    fact_keys = [fact.split('(')[0] for fact in facts]
    rule_heads = {rule.split(" :- ")[0][:-3] for rule in rules}  
   
    while True:
        constraint = input("Constraint: ").strip()
        if not constraint or constraint.lower() == "none":
            break

        parts = constraint.split(" should ")
        if len(parts) != 2:
            print("Invalid format! Try again.")
            continue

        if not parts[0].startswith("if "):
            print("Invalid format! Constraints should start with 'if'. Try again.")
            continue

        fact = parts[0][3:].strip()  
        
        should_not = "not " in parts[1]
        rule = parts[1].replace("not ", "").strip()

        if rule in usedRules:
          print("Rule already used. Try again.")
          continue

        usedRules.append(rule)

        if fact not in fact_keys or rule not in rule_heads:
            print("Error: Invalid fact or rule. Try again.")
            continue

        formatted_constraint = f":- {fact}(X), {rule}(X)." if should_not else f":- {fact}(X), not {rule}(X)."
        constraints.append(formatted_constraint)

    return constraints
