class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def move(self):
        pass  # This will be overridden by subclasses
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} has started")
        else:
            print(f"{self.brand} {self.model} is already running")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped")
        else:
            print(f"{self.brand} {self.model} is already stopped")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color
        self.fuel_level = 100
    
    def move(self):
        print(f"The {self.color} {self.brand} {self.model} is driving 🚗")
    
    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"Refueled to {self.fuel_level}%")
    
    def honk(self):
        print("Beep! Beep! 🚗")

class Plane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan
        self.altitude = 0
    
    def move(self):
        print(f"The {self.brand} {self.model} is flying ✈️")
    
    def take_off(self):
        if self.is_running:
            self.altitude = 10000
            print(f"{self.brand} {self.model} has taken off to {self.altitude} feet")
        else:
            print("Cannot take off - engine not running")
    
    def land(self):
        if self.altitude > 0:
            self.altitude = 0
            print(f"{self.brand} {self.model} has landed safely")
        else:
            print("Already on the ground")

class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length
        self.speed = 0
    
    def move(self):
        print(f"The {self.brand} {self.model} is sailing ⛵")
    
    def anchor(self):
        if self.speed > 0:
            self.speed = 0
            print(f"{self.brand} {self.model} has dropped anchor")
        else:
            print("Already anchored")
    
    def set_speed(self, speed):
        self.speed = speed
        print(f"Speed set to {speed} knots")

# Example usage
if __name__ == "__main__":
    # Create instances of different vehicles
    my_car = Car("Toyota", "Camry", 2023, "blue")
    my_plane = Plane("Boeing", "747", 2020, 68.4)
    my_boat = Boat("Beneteau", "Oceanis", 2022, 45)
    
    # Demonstrate polymorphism with move()
    vehicles = [my_car, my_plane, my_boat]
    
    print("Let's see how different vehicles move:")
    for vehicle in vehicles:
        vehicle.move()
    
    print("\nLet's try some vehicle-specific actions:")
    
    # Car specific actions
    my_car.start()
    my_car.honk()
    my_car.refuel(20)
    
    # Plane specific actions
    my_plane.start()
    my_plane.take_off()
    my_plane.land()
    
    # Boat specific actions
    my_boat.start()
    my_boat.set_speed(15)
    my_boat.anchor()
