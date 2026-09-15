class Vehicle:
    def move(self):
        print("Vehicle is moving")


class EngineVehicle(Vehicle):
    def start_engine(self):
        print("Engine started")


class Bicycle(Vehicle):
    pass