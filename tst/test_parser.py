""" Unit tests for the parser module. """ 

import unittest
from src.parser import parse_asp_program  

class TestParseAspProgram(unittest.TestCase):

    def test_parse_facts(self):
        # Test parsing a list of facts
        lines = ["a.", "b.", "c."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, ["a.", "b.", "c."])
        self.assertEqual(rules, [])
        self.assertEqual(constraints, [])

    def test_parse_rules(self):
        # Test parsing a list of rules
        lines = ["a :- b.", "c :- d, e."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, ["a :- b.", "c :- d, e."])
        self.assertEqual(constraints, [])

    def test_parse_constraints(self):
        # Test parsing a list of constraints
        lines = [":- b.", ":- c, d."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, [])
        self.assertEqual(constraints, [":- b.", ":- c, d."])

    def test_parse_mixed_program(self):
        # Test parsing a program with facts, rules, and constraints
        lines = ["a.", "b :- c.", ":- d.", "e."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, ["a.", "e."])
        self.assertEqual(rules, ["b :- c."])
        self.assertEqual(constraints, [":- d."])

    def test_parse_empty_input(self):
        # Test parsing an empty list of lines
        lines = []
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, [])
        self.assertEqual(constraints, [])

    def test_parse_whitespace_lines(self):
        # Test parsing lines with whitespace (should be ignored)
        lines = ["  ", "\t", "\n"]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, [])
        self.assertEqual(constraints, [])

    def test_parse_complex_rules(self):
        # Test parsing complex rules with multiple conditions
        lines = ["a :- b, c, d.", "e :- f."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, ["a :- b, c, d.", "e :- f."])
        self.assertEqual(constraints, [])

    def test_parse_complex_constraints(self):
        # Test parsing complex constraints with multiple conditions
        lines = [":- b, c, d.", ":- e, f."]
        facts, rules, constraints = parse_asp_program(lines)
        self.assertEqual(facts, [])
        self.assertEqual(rules, [])
        self.assertEqual(constraints, [":- b, c, d.", ":- e, f."])

if __name__ == "__main__":
    unittest.main()
