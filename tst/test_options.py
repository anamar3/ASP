""" This module contains unit tests for the options module. """

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from src.options import display_options

class TestDisplayOptions(unittest.TestCase):

    def setUp(self):
        # Define sample facts, rules, and constraints
        self.facts = ['bird(penguin).', 'cannot_fly(penguin).']
        self.rules = ['fly(X) :- bird(X), not cannot_fly(X).']
        self.constraints = [':- bird(X), not fly(X).']

    @patch("builtins.input", side_effect=["1", "9"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_facts(self, mock_stdout, mock_input):
        """
        Test option 1 (Display Facts).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Facts ---", output)
        self.assertIn("bird(penguin).", output)
        self.assertIn("cannot_fly(penguin).", output)

    @patch("builtins.input", side_effect=["2", "9"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_rules(self, mock_stdout, mock_input):
        """
        Test option 2 (Display Rules).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Rules ---", output)
        self.assertIn("fly(X) :- bird(X), not cannot_fly(X).", output)

    @patch("builtins.input", side_effect=["3", "9"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_constraints(self, mock_stdout, mock_input):
        """
        Test option 3 (Display Constraints).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Constraints ---", output)
        self.assertIn(":- bird(X), not fly(X).", output)

    @patch("builtins.input", side_effect=["4", "9"])
    @patch("options.ground_rules", return_value=["{'head': 'fly(penguin)', 'body': ['bird(penguin)', 'not cannot_fly(penguin).']}"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_grounded_rules(self, mock_stdout, mock_ground_rules, mock_input):
        """
        Test option 4 (Display Grounded Rules).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Grounded Rules ---", output)
        self.assertIn("{'head': 'fly(penguin)', 'body': ['bird(penguin)', 'not cannot_fly(penguin).']}", output)

    @patch("builtins.input", side_effect=["5", "9"])
    @patch("options.generate_models", return_value=[[{'cannot_fly': True, 'bird': True}, {'cannot_fly': False, 'bird': True}, {'cannot_fly': True, 'bird': False}, {'cannot_fly': False, 'bird': False}]])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_all_models(self, mock_stdout, mock_generate_models, mock_input):
        """
        Test option 5 (Display All Models).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- All Models ---", output)
        self.assertIn("{'bird': True, 'cannot_fly': True}", output)
        self.assertIn("{'bird': True, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': True}", output)
        self.assertIn("{'bird': False, 'cannot_fly': False}", output)


    @patch("builtins.input", side_effect=["6", "9"])
    @patch("options.generate_models", return_value=[{'cannot_fly': True, 'bird': True}, {'cannot_fly': False, 'bird': True}, {'cannot_fly': True, 'bird': False}, {'cannot_fly': False, 'bird': False}])
    @patch("options.evaluate_model", side_effect=[False, True, True, True])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_valid_models(self, mock_stdout, mock_evaluate_model, mock_generate_models, mock_input):
        """
        Test option 6 (Display Valid Models).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Valid Models ---", output)
        self.assertIn("{'bird': True, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': True}", output)
        self.assertNotIn("{'bird': True, 'cannot_fly': True}", output)

    @patch("builtins.input", side_effect=["7", "9"])
    @patch("options.ground_rules", return_value=[{'head': 'fly(penguin)', 'body': ['bird(penguin)', 'not cannot_fly(penguin).']}])
    @patch("options.generate_models", return_value=[{'bird': True, 'cannot_fly': True}, {'bird': True, 'cannot_fly': False}, {'bird': False, 'cannot_fly': True}, {'bird': False, 'cannot_fly': False}])
    @patch("options.evaluate_model", side_effect=[True, False, False, True, True])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_all(self, mock_stdout, mock_evaluate_model, mock_generate_models, mock_ground_rules, mock_input):
        """
        Test option 7 (Display All).
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("--- Facts ---", output)
        self.assertIn("bird(penguin).", output)
        self.assertIn("cannot_fly(penguin).", output)
        self.assertIn("--- Rules ---", output)
        self.assertIn("fly(X) :- bird(X), not cannot_fly(X).", output)
        self.assertIn("--- Constraints ---", output)
        self.assertIn(":- bird(X), not fly(X).", output)
        self.assertIn("--- Grounded Rules ---", output)
        self.assertIn("{'head': 'fly(penguin)', 'body': ['bird(penguin)', 'not cannot_fly(penguin).']}", output)
        self.assertIn("--- All Models ---", output)
        self.assertIn("{'bird': True, 'cannot_fly': True}", output)
        self.assertIn("{'bird': True, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': True}", output)
        self.assertIn("{'bird': False, 'cannot_fly': False}", output)
        self.assertIn("--- Valid Models ---", output)
        self.assertIn("{'bird': True, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': False}", output)
        self.assertIn("{'bird': False, 'cannot_fly': True}", output)

    @patch("builtins.input", side_effect=["8", "is tweety a valid model?", "9"])
    @patch("options.generate_models", return_value=[{'bird': True, 'cannot_fly': True}, {'bird': True, 'cannot_fly': False}, {'bird': False, 'cannot_fly': True}, {'bird': False, 'cannot_fly': False}])
    @patch("options.evaluate_model", side_effect=lambda *args: True)
    @patch("sys.stdout", new_callable=StringIO)
    def test_ask_question_valid_model(self, mock_stdout, mock_evaluate_model, mock_generate_models, mock_input):
        """
        Test option 8 (Ask a Question) with a valid model.
        """
        self.facts.append("bird(tweety).")
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("Yes, this indeed is a valid model!", output)

    @patch("builtins.input", side_effect=["8", "is penguin a valid model?", "9"])
    @patch("options.generate_models", return_value=[{'bird': True, 'cannot_fly': True}, {'bird': True, 'cannot_fly': False}, {'bird': False, 'cannot_fly': True}, {'bird': False, 'cannot_fly': False}])
    @patch("options.evaluate_model", side_effect=[False, True, True, True])
    @patch("sys.stdout", new_callable=StringIO)
    def test_ask_question_invalid_model(self, mock_stdout, mock_evaluate_model, mock_generate_models, mock_input):
        """
        Test option 8 (Ask a Question) with an invalid model.
        """
        self.facts.append("bird(tweety).")
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("Nope, this is NOT a valid model!", output)

    @patch("builtins.input", side_effect=["10", "9"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        """
        Test invalid choice.
        """
        display_options(self.facts, self.rules, self.constraints)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid choice. Please try again.", output)

if __name__ == "__main__":
    unittest.main()
