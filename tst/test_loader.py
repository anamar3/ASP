"""Unit tests for the loader module. """

import unittest
import os
import sys
from tempfile import NamedTemporaryFile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.loader import load_asp_file  

class TestLoadAspFile(unittest.TestCase):

    def test_load_valid_file(self):
        # Create a temporary file with valid ASP content
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("a.\n")
            temp_file.write("b.\n")
            temp_file.write("% This is a comment\n")
            temp_file.write("c.\n")
            temp_file.write("\n")  # Empty line
            temp_file.write("d.\n")
            temp_file_name = temp_file.name

        # Load the file and check the result
        expected_program = ["a.", "b.", "c.", "d."]
        self.assertEqual(load_asp_file(temp_file_name), expected_program)

        # Clean up the temporary file
        os.remove(temp_file_name)

    def test_load_empty_file(self):
        # Create a temporary empty file
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file_name = temp_file.name

        # Load the file and check the result
        self.assertEqual(load_asp_file(temp_file_name), [])

        # Clean up the temporary file
        os.remove(temp_file_name)

    def test_load_file_with_only_comments_and_empty_lines(self):
        # Create a temporary file with only comments and empty lines
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("% Comment 1\n")
            temp_file.write("\n")
            temp_file.write("% Comment 2\n")
            temp_file_name = temp_file.name

        # Load the file and check the result
        self.assertEqual(load_asp_file(temp_file_name), [])

        # Clean up the temporary file
        os.remove(temp_file_name)

    def test_load_nonexistent_file(self):
        # Test loading a file that does not exist
        with self.assertRaises(FileNotFoundError):
            load_asp_file("nonexistent_file.asp")

if __name__ == "__main__":
    unittest.main()