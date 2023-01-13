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
