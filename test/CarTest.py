from src.Car import Car
import unittest

class CarTest(unittest.TestCase):
    def test_car(self):
        car = Car("Toyota", "Camry", "ABC123", "A", 100)
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.registration_number, "ABC123")
        self.assertEqual(car.rental_group, "A")
        self.assertEqual(car.cost_per_day, 100)

if __name__ == '__main__':
    unittest.main() # this runs our tests
