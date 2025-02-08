""" Unit tests for the save_input module. """

import unittest
import os
from src.save_input import save_to_file  

class TestSaveToFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_filename = "test_output.txt"

    def tearDown(self):
        # Clean up the temporary file after each test
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_to_file(self):
        # Test saving facts, rules, constraints, and more facts
        facts = ["a.", "b.", "c."]
        rules = ["p(X) :- q(X).", "r(Y) :- s(Y)."]
        constraints = [":- q(X), r(X)."]
        more_facts = ["d.", "e."]

        # Call the function
        save_to_file(self.test_filename, facts, rules, constraints, more_facts)

        # Verify the file content
        with open(self.test_filename, "r") as file:
            content = file.read()

        expected_content = (
            "% Facts\n"
            "a.\n"
            "b.\n"
            "c.\n"
            "\n"
            "% Rules\n"
            "p(X) :- q(X).\n"
            "r(Y) :- s(Y).\n"
            "\n"
            "% Constraints\n"
            ":- q(X), r(X).\n"
            "\n"
            "% More Facts\n"
            "d.\n"
            "e.\n"
        )
        self.assertEqual(content, expected_content)

    def test_save_to_file_empty_input(self):
        # Test saving empty lists
        facts = []
        rules = []
        constraints = []
        more_facts = []

        # Call the function
        save_to_file(self.test_filename, facts, rules, constraints, more_facts)

        # Verify the file content
        with open(self.test_filename, "r") as file:
            content = file.read()

        expected_content = (
            "% Facts\n"
            "\n"
            "% Rules\n"
            "\n"
            "% Constraints\n"
            "\n"
            "% More Facts\n"
        )
        self.assertEqual(content, expected_content)

    def test_save_to_file_mixed_input(self):
        # Test saving mixed input (some lists empty, others not)
        facts = ["a.", "b."]
        rules = []
        constraints = [":- q(X)."]
        more_facts = ["c."]

        # Call the function
        save_to_file(self.test_filename, facts, rules, constraints, more_facts)

        # Verify the file content
        with open(self.test_filename, "r") as file:
            content = file.read()

        expected_content = (
            "% Facts\n"
            "a.\n"
            "b.\n"
            "\n"
            "% Rules\n"
            "\n"
            "% Constraints\n"
            ":- q(X).\n"
            "\n"
            "% More Facts\n"
            "c.\n"
        )
        self.assertEqual(content, expected_content)

if __name__ == "__main__":
    unittest.main()