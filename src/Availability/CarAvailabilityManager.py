import threading

class CarAvailabilityManager:
    def __init__(self):
        self.car_availability = {}  # Dictionary to track car availability by registration number
        self.lock = threading.Lock()

    def add_car(self,car, from_date, to_date):
        with self.lock:
            self.car_availability[car.registration_number] = {
                'available': True,
                'from_date': from_date,
                'to_date': to_date,
            }

    def remove_car(self, car_registration_number):
        with self.lock:
            self.car_availability.pop(car_registration_number, None)

    def update_car_availability(self, car_registration_number, from_date, to_date):
        with self.lock:
            self.car_availability[car_registration_number]['from_date'] = from_date
            self.car_availability[car_registration_number]['to_date'] = to_date


    def get_available_cars(self, from_date, to_date):
        with self.lock:
            available_cars = []
            for car_registration_number, car_availability in self.car_availability.items():
                if car_availability['available'] and car_availability['from_date'] <= from_date and car_availability['to_date'] >= to_date:
                    available_cars.append(car_registration_number)
            return available_cars