from sensormodule import *
class Accelemeter(sensor):
    def show_sensor_type(self):
        print(f"this is the {self.name} and the location is {self.loc}")
class Gyro(Accelemeter):
    def show_sensor_type(self):
        print(f"this is {self.name} and the location is {self.loc}")
class Gps(sensor):
    def __init__(self, name, rec_date, loc,brand) -> None:
        super().__init__(name, rec_date, loc)
        self.brand=brand