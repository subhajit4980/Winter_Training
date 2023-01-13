# # class in python
# class Superheroes():
#     def __init__(self,name,superpower) -> None:
#         self.name=name
#         self.superpower=superpower
#     def get_superpower(self):
#         print(f"I am {self.name} and my superpower is {self.superpower}")

# ironman=Superheroes(name="subahjit",superpower="coding")
# ironman.get_superpower()
class sensor():
    def __init__(self,name,rec_date,loc) -> None:
        # pass
        self.name=name
        self.rec_date=rec_date
        self.loc=loc
        self.data={}


    def add_data(self,data,time):
        # pass
        self.data['data']=data
        self.data['time']=time
        print("data point added successfully")
    def clear_data(self):
        # pass
        self.data={}
        print("data removed successfully")
import numpy as np
sensor1=sensor(
    "sensor1",
    "09-01-2023",
    "haldia"
)
print(sensor1.name,sensor1.loc,sensor1.rec_date)
data=np.random.randint(-10,10,10)
time=np.arange(10)
sensor1.add_data(data=data,time=time)
print(sensor1.data)
class Accelemeter(sensor):
    def show_sensor_type(self):
        print(f"this is the {self.name} and the location is {self.loc}")
acc_data=np.random.randint(-10,10,10)
acc_time=np.arange(10)
acc=Accelemeter("accelemeter","09-01-2023","haldia")

acc.add_data(acc_data,acc_time)
acc.show_sensor_type()
print("accelerometer data",acc.data)
class Gyro(Accelemeter):
    def show_sensor_type(self):
        print(f"this is {self.name} and the location is {self.loc}")
gyro_data=np.random.randint(-15,15,10)
gyro_time=np.arange(10)

gyro=Gyro("Gyroscope","10-01-2023","kolkata")
gyro.add_data(gyro_data,gyro_time)
print("gyro data is ",gyro.data)
gyro.show_sensor_type()
class Gps(sensor):
    def __init__(self, name, rec_date, loc,brand) -> None:
        super().__init__(name, rec_date, loc)
        self.brand=brand
gps=Gps("Gps","10-01-2023","kharaghpur","XYZ")

print(gps.name+ " " +gps.rec_date+ " " +gps.loc+ " " +gps.brand)