from sensormodule import *
from sensors import *
import numpy as np
data=np.random.randint(-10,10,10)
time=np.arange(10)
sensor1=sensor(
    "sensor1",
    "09-01-2023",
    "haldia"
)
print(sensor1.name,sensor1.loc,sensor1.rec_date)
sensor1.add_data(data=data,time=time)
print(sensor1.data)
# accelemeter data
acc_data=np.random.randint(-10,10,10)
acc_time=np.arange(10)
acc=Accelemeter("accelemeter","09-01-2023","haldia")
acc.add_data(acc_data,acc_time)
acc.show_sensor_type()
print("accelerometer data",acc.data)
# gyroscop data
gyro_data=np.random.randint(-15,15,10)
gyro_time=np.arange(10)
gyro=Gyro("Gyroscope","10-01-2023","kolkata")
gyro.add_data(gyro_data,gyro_time)
print("gyro data is ",gyro.data)
gyro.show_sensor_type()
# GPS data
class Gps(sensor):
    def __init__(self, name, rec_date, loc,brand) -> None:
        super().__init__(name, rec_date, loc)
        self.brand=brand
gps=Gps("Gps","10-01-2023","kharaghpur","XYZ")
gps_data=np.random.randint(-12,12,10)
gps_time=np.arange(10)
gps.add_data(gps_data,gps_time)
print(gps.name+ " " +gps.rec_date+ " " +gps.loc+ " " +gps.brand)
print("gyro data is ",gyro.data)