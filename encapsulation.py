class sensor():
    def __init__(self,name,location):
        # pass
        self.name=name
        self.loaction=location
        self._recorded_date="10-01-2023"
        self._version="1.021"
    def get_recorded_date(self):
        print(f"recorded date is {self._recorded_date}")
    def get_version(self):
        print(f"version is {self._version}")
    def set_recorded_date(self,rec_date):
        self._recorded_date=rec_date
        print(f"set recorded date is {self._recorded_date}")
    def set_version(self,version):
        self._version=version
        print(f"set version is {self._version}")
sensor1=sensor("sensor1","haldia")
print(sensor1.name)
print(sensor1.loaction)
print(sensor1._recorded_date)
sensor1.set_recorded_date("09-01-2023")
sensor1.get_recorded_date()
sensor1.set_version("3.01")
sensor1.get_version()