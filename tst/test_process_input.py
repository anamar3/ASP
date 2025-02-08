""" This module contains the unit tests for the functions in process_input.py. """

import unittest
from unittest.mock import patch
from io import StringIO
from src.process_input import get_facts, get_more_facts, get_rules, get_constraints

class TestFactFunctions(unittest.TestCase):

    @patch("builtins.input", side_effect=["cat is an animal", "dog is an animal", ""])
    def test_get_facts_valid_input(self, mock_input):
        """
        Test get_facts with valid input.
        """
        expected_facts = ["animal(cat).", "animal(dog)."]
        result = get_facts()
        self.assertEqual(result, expected_facts)

    @patch("builtins.input", side_effect=["cat is an animal", "dog is a plant", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_facts_invalid_category(self, mock_stdout, mock_input):
        """
        Test get_facts with invalid category input.
        """
        expected_output = "Error: All entries must belong to the same category 'animal'. Try again.\n"
        get_facts()
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["cat is an animal", "cat is an animal", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_facts_duplicate_entry(self, mock_stdout, mock_input):
        """
        Test get_facts with duplicate entry.
        """
        expected_output = "Error: 'cat' has already been added. Try again.\n"
        get_facts()
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["cat is an animal", "dog is an animal", ""])
    def test_get_more_facts_valid_input(self, mock_input):
        """
        Test get_more_facts with valid input.
        """
        facts = ["animal(cat).", "animal(dog)."]
        expected_more_facts = ["has_tail(cat).", "has_tail(dog)."]
        with patch("builtins.input", side_effect=["cat has_tail", "dog has_tail", ""]):
            result = get_more_facts(facts)
            self.assertEqual(result, expected_more_facts)

    @patch("builtins.input", side_effect=["cat has_tail", "fish has_tail", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_more_facts_invalid_entity(self, mock_stdout, mock_input):
        """
        Test get_more_facts with invalid entity.
        """
        facts = ["animal(cat).", "animal(dog)."]
        expected_output = "Error: 'fish' is not defined in Facts. Try again.\n"
        get_more_facts(facts)
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["cat has_tail", "cat has_tail", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_more_facts_duplicate_entry(self, mock_stdout, mock_input):
        """
        Test get_more_facts with duplicate entry.
        """
        facts = ["animal(cat).", "animal(dog)."]
        expected_output = "Error: 'has_tail(cat).' has already been added. Try again.\n"
        get_more_facts(facts)
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["fly if bird and not cannot_fly", ""])
    def test_get_rules_valid_input(self, mock_input):
        """
        Test get_rules with valid input.
        """
        facts = ["bird(cat)."]
        more_facts = ["cannot_fly(cat)."]
        expected_rules = ["fly(X) :- bird(X), not cannot_fly(X)."]
        result = get_rules(facts, more_facts)
        self.assertEqual(result, expected_rules)

    @patch("builtins.input", side_effect=["fly if bird and not cannot_fly", "fly if bird and not cannot_fly", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_rules_duplicate_rule(self, mock_stdout, mock_input):
        """
        Test get_rules with duplicate rule.
        """
        facts = ["bird(cat)."]
        more_facts = ["cannot_fly(cat)."]
        expected_output = "Error: A rule with the name 'fly' already exists. Try again.\n"
        get_rules(facts, more_facts)
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["if bird should fly", ""])
    def test_get_constraints_valid_input(self, mock_input):
        """
        Test get_constraints with valid input.
        """
        facts = ["bird(cat)."]
        rules = ["fly(X) :- bird(X)."]
        expected_constraints = [":- bird(X), not fly(X)."]
        result = get_constraints(facts, rules)
        self.assertEqual(result, expected_constraints)

    @patch("builtins.input", side_effect=["if bird should fly", "if bird should fly", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_constraints_duplicate_rule(self, mock_stdout, mock_input):
        """
        Test get_constraints with duplicate rule.
        """
        facts = ["bird(cat)."]
        rules = ["fly(X) :- bird(X)."]
        expected_output = "Rule already used. Try again.\n"
        get_constraints(facts, rules)
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()