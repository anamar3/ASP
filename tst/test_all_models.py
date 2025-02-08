"""Unit tests for the generate_models function in all_models.py """

import unittest
from src.all_models import generate_models  

class TestGenerateModels(unittest.TestCase):

    def test_empty_facts(self):
        # Test with an empty list of facts
        facts = []
        models = generate_models(facts)
        self.assertEqual(models, [{}])  # Only one model: empty assignment

    def test_multiple_facts(self):
        # Test with a multiple facts
        facts = ['bird(penguin).', 'cannot_fly(penguin).']
        models = generate_models(facts)
        expected = [{'bird': True, 'cannot_fly': True}, {'bird': True, 'cannot_fly': False}, {'bird': False, 'cannot_fly': True}, {'bird': False, 'cannot_fly': False}]
        
        self.assertIn({'bird': True, 'cannot_fly': True} ,models)
        self.assertIn({'bird': False, 'cannot_fly': True} ,models)
        self.assertIn({'bird': True, 'cannot_fly': False} ,models)
        self.assertIn({'bird': False, 'cannot_fly': False} ,models)


    def test_one_fact(self):
        # Test with one facts
        facts = ['bird(penguin).']
        models = generate_models(facts)
    
        self.assertIn({'bird': False} ,models)
        self.assertIn({'bird': True} ,models)

    def test_duplicate_facts(self):
        # Test with duplicate facts (should be treated as unique)
        facts = ['bird(penguin).', 'bird(tweety).']
        models = generate_models(facts)
    
        self.assertEqual([{'bird': True},{'bird': False}] ,models)

   

if __name__ == "__main__":
    unittest.main()