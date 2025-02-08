""" This module contains tests for the user_input module. """

import sys
import os

# Ensure the src directory is added to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest
from unittest.mock import patch, MagicMock

# Import from user_input.py (not main.py)
from user_input import main
from process_input import get_facts, get_more_facts, get_rules, get_constraints
from save_input import save_to_file
from loader import load_asp_file
from parser import parse_asp_program
from options import display_options

class TestMain(unittest.TestCase):

    @patch("builtins.input", side_effect=[
    "1",            # Choose manual input
    "dog is a mammal",  # First fact
    "cat is a mammal",  # Second fact
    "",             # End of first fact entry
    "dog barks",  # First additional property
    "cat meows",  # Second additional property
    "",             # End of more facts
    "sleep if mammal and barks",  # First rule
    "",             # End of rules
    "",  # First constraint
    "",             # End of constraints
    "output.txt"    # Output file name
])

    @patch("user_input.save_to_file")  
    @patch("user_input.display_options")  
    def test_main_manual_input(self, mock_display_options, mock_save_to_file, mock_input):
        """Test the main function when the user chooses to enter facts manually."""
        main()
        mock_save_to_file.assert_called_once_with(
            '', ['mammal(dog).', 'mammal(cat).', 'barks(dog).', 'meows(cat).'], ['sleep(X) :- mammal(X), barks(X).'], [], ['barks(dog).', 'meows(cat).']
        )

        mock_display_options.assert_called_once_with(
            ['mammal(dog).', 'mammal(cat).', 'barks(dog).', 'meows(cat).'], ['sleep(X) :- mammal(X), barks(X).'], []
        )

    @patch("builtins.input", side_effect=["2", "test_file.txt"])
    @patch("user_input.load_asp_file", return_value="file content")  
    @patch("user_input.parse_asp_program", return_value=(['bird(penguin).', 'cannot_fly(penguin).'], ['fly(X) :- bird(X), cannot_fly(X).'], [':- bird(X), not fly(X).']))
    @patch("user_input.display_options")  
    def test_main_file_input(self, mock_display_options, mock_parse_asp_program, mock_load_asp_file, mock_input):
        """Test the main function when the user chooses to provide a file path."""
        main()
        mock_load_asp_file.assert_called_once_with("test_file.txt")
        mock_parse_asp_program.assert_called_once_with("file content")
        mock_display_options.assert_called_once_with(
            ['bird(penguin).', 'cannot_fly(penguin).'], ['fly(X) :- bird(X), cannot_fly(X).'], [':- bird(X), not fly(X).']
        )

if __name__ == "__main__":
    unittest.main()
