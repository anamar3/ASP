"""This module contains the function to display options to the user."""

from src.grounded_rules import ground_rules
from src.all_models import generate_models
from src.valid_models import evaluate_model


def display_options(facts,rules,constraints) -> None:
    """Prompt user to choose what they want to see."""
    while True:
        print("\nWhat do you want to see?")
        print("1. Facts")
        print("2. Rules")
        print("3. Constraints")
        print("4. Grounded Rules")
        print("5. All Models")
        print("6. Valid Models")
        print("7. Show All")
        print("8. Ask a Question")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()
        
        if choice == "1":
            print("\n--- Facts ---")
            print(facts)

        elif choice == "2":
            print("\n--- Rules ---")
            print(rules)

        elif choice == "3":
            print("\n--- Constraints ---")
            print(constraints)

        elif choice == "4":
            print("\n--- Grounded Rules ---")
            print(ground_rules(rules,facts))

        elif choice == "5":
            print("\n--- All Models ---")
            print(generate_models(facts))

        elif choice == "6":
            print("\n--- Valid Models ---")
            models = generate_models(facts)
            valid_models = [model for model in models if evaluate_model(model, rules, constraints,facts)]
            print(valid_models)

        elif choice == "7":
            print("\n--- All ---")
            print("\n--- Facts ---")
            print(facts)
            print("\n--- Rules ---")
            print(rules)
            print("\n--- Constraints ---")
            print(constraints)
            print("\n--- Grounded Rules ---")
            print(ground_rules(rules,facts))
            print("\n--- All Models ---")
            print(generate_models(facts))
            print("\n--- Valid Models ---")
            models = generate_models(facts)
            valid_models = [model for model in models if evaluate_model(model, rules, constraints,facts)]
            print(valid_models)


        elif choice == "8":
            question = input("Enter your question (format: 'is/are <entity> a valid model?'): ").strip().lower()

            models = generate_models(facts)
            valid_models = [model for model in models if evaluate_model(model, rules, constraints,facts)]
            
            # Validate the question format
            parts = question.split()
            flag = True

            if (
            len(parts) >= 5 and
            parts[0] in ["is", "are"] and
            parts[2] == "a" and
            parts[3] == "valid" and
            parts[4] == "model?"
            ):
              entity = parts[1]  # Extract entity
              for v_model in valid_models:
                  flag = True
                  for key, value in v_model.items():
                        if value and f"{key}({entity})." in facts:
                            continue
                        elif not value and f"{key}({entity})." not in facts:
                            continue
                        else:
                            flag = False
                  if flag:
                      print("Yes, this indeed is a valid model!")
                      break
            else:
                 print("Invalid format! Please use: 'is/are <entity> a valid model?'")
                 
            if not flag:
             print("Nope, this is NOT a valid model!")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
