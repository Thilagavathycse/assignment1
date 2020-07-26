import re
class Driver:
    def __init__(self,name,age,driving_license_number,driving_license_validity_period):
        self.name=name
        self.age=age
        self.driving_license_number=driving_license_number
        self.driving_license_validity_period=driving_license_validity_period
    def display_driver_details(self):
        print("Name of the driver or owner is {} age  {} driving license number is {} and validity period {}".format(self.name,self.age,self.driving_license_number,self.driving_license_validity_period))

class Car:
    def __init__(self,name,age,driving_license_number,driving_license_validity_period,car_category,car_number,colour,company,model):
        self.car_category=car_category
        self.car_number=car_number
        self.colour=colour
        self.company=company
        self.model=model
        self.driver=Driver(name,age,driving_license_number,driving_license_validity_period)
    def display_car_details(self):
        print("car category {} car number {} car color is {} and car model is {}".format(self.car_category,self.car_number,self.colour))
name=input("Enter  name:")
age=input("Enter age:")
while True:
    driving_license_number=input("Enter driving license number:").lower()
    if re.match(r"([A-Z]{2}[0-9]{2})((19|20)[0-9][0-9])([0-9]{7})",driving_license_number):
        print("true")
        
    else:
        print("please enter a valid license number")
    driving_license_validity_period=input("Enter license validity period in (dd-mm-yyyy):")
    if re.match(r"(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](202[1-9])",driving_license_validity_period):
        print("true")
    
    else:
        print("please enter the valid date !")
        break

car_category=input("Enter the car catagory either MICRO or XL:")
car_number=input("Enter car number:")  
colour=input("Enter the color of the car:")
company=input("Enter the company name:")
model=input("Enter the model of car:")
car1=Car(name,age,driving_license_number,driving_license_validity_period,car_category,car_number,colour,company,model)
car1.driver.display_driver_details()
car1.display_car_details()

        
        

