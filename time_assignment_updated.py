class Time:
    def __init__(self,hours,mins):
        self.hours=hours
        self.mins=mins
    def display_time(self):
        print("Time is {} hours and {} minutes".format(self.hours,self.mins))
        
def dislay_in_minute(*Time):
    time_in_minute_for_first_time=(time1.hours*60)+time1.mins
    time_in_minute_for_second_time=(time2.hours*60)+time2.mins
    print("Total time in minutes:{}".format(time_in_minute_for_first_time+time_in_minute_for_second_time))
def add_time(*Time):
    total_time=time1.hours+time2.hours
    total_min=time1.mins+time2.mins 
    if total_min > 60:
        total_time=total_time+1
        total_min=total_min-60
        print("Total time:{} hours {} mins".format(total_time,total_min))    
def difference_time(*Time):
    hour_difference=abs(time1.hours-time2.hours)
    mins_difference=abs(time1.mins-time2.mins)
    print("Time difference is: {} hours {} mins".format(hour_difference,mins_difference))
          
time1=Time(5,50)
time2=Time(2,15)
time1.display_time()
time2.display_time()
dislay_in_minute()#time2.dislay_in_minute()
add_time(time1,time2)
difference_time(time1,time2)
