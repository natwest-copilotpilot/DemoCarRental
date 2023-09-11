from src.Renter import Renter
import unittest

class RenterTest(unittest.TestCase):
    def test_renter(self):
        renter = Renter("Smith", "John", "ABC123",  "01/01/2020")
        self.assertEqual(renter.last_name, "Smith")
        self.assertEqual(renter.first_name, "John")
        self.assertEqual(renter.driving_license_number, "ABC123")
        self.assertEqual(renter.date_of_birth, "01/01/2020")

if __name__ == '__main__':
    unittest.main() # this runs our tests
