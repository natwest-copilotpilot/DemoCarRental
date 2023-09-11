"""write a test for the CarAvailabilityManager class"""

import unittest
from src.Car import Car
from src.Availability.CarAvailabilityManager import CarAvailabilityManager
import threading


class TestCarAvailabilityManager(unittest.TestCase):

    def setUp(self):
        self.car_manager = CarAvailabilityManager()
        self.lock = threading.Lock()

    def test_add_car(self):
        car1 = Car("Toyota", "Camry", "ABC123", "Group A", 50.0)
        self.car_manager.add_car(car1, "2023-09-01", "2023-09-10")
        self.assertEqual(len(self.car_manager.car_availability), 1)

    def test_remove_car(self):
        car1 = Car("Toyota", "Camry", "ABC123", "Group A", 50.0)
        self.car_manager.add_car(car1, "2023-09-01", "2023-09-10")
        self.car_manager.remove_car("ABC123")
        self.assertEqual(len(self.car_manager.car_availability), 0)

    def test_update_car_availability(self):
        car1 = Car("Toyota", "Camry", "ABC123", "Group A", 50.0)
        self.car_manager.add_car(car1, "2023-09-01", "2023-09-10")
        self.car_manager.update_car_availability("ABC123", "2023-09-05", "2023-09-15")
        self.assertEqual(self.car_manager.car_availability["ABC123"]["from_date"], "2023-09-05")
        self.assertEqual(self.car_manager.car_availability["ABC123"]["to_date"], "2023-09-15")

    def test_get_available_cars(self):
        car1 = Car("Toyota", "Camry", "ABC123", "Group A", 50.0)
        car2 = Car("Honda", "Civic", "XYZ789", "Group B", 60.0)
        self.car_manager.add_car(car1, "2023-09-01", "2023-09-10")
        self.car_manager.add_car(car2, "2023-09-05", "2023-09-15")

        def find_available_cars():
            with self.lock:
                available_cars = self.car_manager.get_available_cars("2023-09-03", "2023-09-12")
                return available_cars

        # Create two threads to find available cars simultaneously
        thread1 = threading.Thread(target=find_available_cars)
        thread2 = threading.Thread(target=find_available_cars)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        self.assertEqual(len(self.car_manager.car_availability), 2)  # Both cars are still in the system

if __name__ == '__main__':
    unittest.main()
