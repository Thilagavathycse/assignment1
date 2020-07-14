class TimingClass:
    def __init__(self):
        self.first_time = input("Enter the first time with minutes:").split()
        self.second_time= input("Enter the Second time with minutes: ").split()
    def get_time(self):
        self.total_hour=int(self.first_time[0])+int(self.second_time[0])
        self.total_mins=int(self.first_time[3])+int(self.second_time[3])
        if self.total_mins >= 60:
            self.total_hour=self.total_hour+1
            self.total_mins=self.total_mins-60
            print("Total time {} and {} mins:".format(self.total_hour,self.total_mins))
    def Total_time_cal(self):
         Total_time=(self.total_hour*60)+self.total_mins
         print(Total_time)
         print("Total time {} mins ".format(Total_time))
        
    def difference(self):
        self.total_hour=abs(int(self.first_time[0])-int(self.second_time[0]))
        self.total_mins=abs(int(self.first_time[3])-int(self.second_time[3]))
        print("Time difference is {} and {} mins:".format(self.total_hour,self.total_mins))
time=TimingClass()
time.get_time()
time.Total_time_cal()
time.difference()

