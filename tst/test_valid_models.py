""" This module contains tests for the functions in the valid_models module. """

import unittest
from src.valid_models import (
    checkFactExists,
    checkIfAllConditionsApply,
    checkRulesAndConstraintsValid,
    evaluate_model,
)

class TestEvaluateModel(unittest.TestCase):

    def test_checkFactExists(self):
        # Test if a fact exists in the list of facts
        facts = ["a(X).", "b(X).", "c(X)."]
        self.assertTrue(checkFactExists(facts, "a"))
        self.assertFalse(checkFactExists(facts, "d"))

    def test_checkValidModel_no_constraints(self):
        # Test if a model is valid no given constraints
        model = {'bird': True, 'cannot_fly': True}
        rules = ["fly(X) :- bird(X), not cannot_fly(X)."]
        constraints = []
        facts = ['bird(penguin).', 'cannot_fly(penguin).']
        self.assertTrue(evaluate_model(model, rules, constraints, facts))

    def test_contradictingBodiesOfConst(self):
        # Test if two rule bodies contradict each other
        rules = ['fly(X) :- bird(X), not cannot_fly(X), sing(X).', 'scream(X) :- bird(X), sing(X).'] 
        constraints = [':- bird(X), not fly(X).', ':- bird(X), fly(X).']
        self.assertFalse(checkRulesAndConstraintsValid(rules, constraints))


    def test_checkRulesAndConstraintsValid(self):
        # Test if rules and constraints are valid (no contradictions)
        rules = ['fly(X) :- bird(X), not cannot_fly(X), sing(X).', 'scream(X) :- bird(X), sing(X).']
        constraints = [':- bird(X), not fly(X).', ':- bird(X), not scream(X).']
        self.assertTrue(checkRulesAndConstraintsValid(rules, constraints))
        

    def test_evaluate_model_valid_with_constraints(self):
        # Test evaluating a valid model
        model = {'bird': True, 'sing': False}
        rules = ["fly(X) :- bird(X), sing(X)."]
        constraints = [":- bird(X), fly(X)."]
        facts = ['bird(penguin).', "sing(penguin)."]
        self.assertTrue(evaluate_model(model, rules, constraints, facts))

    def test_evaluate_model_invalid(self):
        # Test evaluating an invalid model
        model = {'bird': True, 'cannot_fly': True}
        rules = ["fly(X) :- bird(X), cannot_fly(X)."]
        constraints = [":- bird(X), fly(X)."]
        facts = ['bird(penguin).', "cannot_fly(penguin)."]
        self.assertFalse(evaluate_model(model, rules, constraints, facts))

    def test_evaluate_model_invalid_syntax(self):
        # Test evaluating a model with an invalid syntax
        model = {'bird': True, 'cannot_fly': False}
        rules = ['fly(X) :- bird(X), cannot_fly(X).']
        constraints = []
        facts = ["bird(penguin).", "cannot_fly(penguin)."]
        self.assertFalse(evaluate_model(model, rules, constraints, facts))

    def test_evaluate_model_invalid_fact(self):
        # Test evaluating a model with an invalid fact
        model = {'bird': True, 'cannot_fly': False}
        rules = ['fly(X) :- cannot_fly(X), bird(X).']
        constraints = []
        facts = ["bird(penguin).", "cannot_fly(penguin)."]
        self.assertFalse(evaluate_model(model, rules, constraints, facts))    

if __name__ == "__main__":
    unittest.main()