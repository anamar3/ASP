"""Unit tests for the grounded_rules module. """

import unittest
from src.grounded_rules import ground_rules, extract_constants  

class TestRuleGrounding(unittest.TestCase):
    
    def test_extract_constants(self):
        facts = ["bird(penguin).", "bird(tweety).", "scream(penguin)."]
        expected_constants = {"penguin", "tweety"}
        self.assertEqual(extract_constants(facts), expected_constants)

    def test_ground_rules_single_constant(self):
        facts = ["bird(penguin)."]
        rules = ["flies(X) :- bird(X)."]
        expected_grounded = [
            {"head": "flies(penguin)", "body": ["bird(penguin)."]}
        ]
        self.assertEqual(ground_rules(rules, facts), expected_grounded)

    def test_ground_rules_multiple_constants(self):
        facts = ['bird(penguin).', 'bird(tweety).']
        rules = ['fly(X) :- bird(X).']
        expected_grounded = [{'head': 'fly(penguin)', 'body': ['bird(penguin).']},{'head': 'fly(tweety)', 'body': ['bird(tweety).']}]
        
        self.assertIn({'head': 'fly(penguin)', 'body': ['bird(penguin).']},ground_rules(rules, facts))
        self.assertIn({'head': 'fly(tweety)', 'body': ['bird(tweety).']},ground_rules(rules, facts))


    def test_ground_rules_multiple_conditions(self):
        facts = ["bird(penguin).", "can_swim(penguin)."]
        rules = ["flies(X) :- bird(X), not can_swim(X)."]
        expected_grounded = [
            {"head": "flies(penguin)", "body": ["bird(penguin)", "not can_swim(penguin)."]}
        ]
        self.assertEqual(ground_rules(rules, facts), expected_grounded)

    def test_ground_rules_no_matching_constants(self):
        facts = ["mammal(dog)."]
        rules = ["flies(X) :- bird(X)."]
        expected_grounded = [{'head': 'flies(dog)', 'body': ['bird(dog).']}]
        self.assertEqual(ground_rules(rules, facts), expected_grounded)

if __name__ == "__main__":
    unittest.main()
