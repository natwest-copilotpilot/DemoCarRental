"""write test for Criteria.py"""

from src.Criteria import Criteria
import unittest

class CriteriaTest(unittest.TestCase):
    def test_criteria(self):
        criteria = Criteria()
        criteria.cost_criteria(100)
        self.assertEqual(criteria.get_cost_criteria(), 100)

if __name__ == '__main__':
    unittest.main() # this runs our tests
