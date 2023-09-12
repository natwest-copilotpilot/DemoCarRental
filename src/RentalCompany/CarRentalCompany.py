import threading

class CarRentalCompany:
    def __init__(self):
        self.cars = []
        self.lock = threading.Lock()

    def add_car(self, car):
        self.cars.append(car)

    def matching_cars(self, criteria):
        if criteria.get_cost_criteria() is not None:
            with self.lock:
              return [car for car in self.cars if car.cost_per_day <= criteria.get_cost_criteria()]

    def rent_car(self, renter, car):
        pass

    def return_car(self, renter, car):
        pass