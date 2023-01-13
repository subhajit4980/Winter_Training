class Acceleraor(sensor):
    def show_sensor_type(self):
        print(f"this is the {self.name}")
acc_data=np.random.randint(-10,10,10)
acc_time=np.arange(10)
acc=Acceleraor("accelemeter","09-01-2023","haldia")

acc.add_data(acc_data,acc_time)
print("accelerometer data",acc.data)