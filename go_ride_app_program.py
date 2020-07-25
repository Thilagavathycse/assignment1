class Driver:
    def __init__(self,name,age,driving_license_number,driving_license_validity_period):
        self.name=name
        self.age=age
        self.driving_license_number=driving_license_number
        self.driving_license_validity_period=driving_license_validity_period
class Car:
    def __init__(self,name,age,driving_license_number,driving_license_validity_period,car_category,car_number,colour,company,model):
        self.car_category=car_category
        self.car_number=car_number
        self.colour=colour
        self.company=company
        self.model=model
        self.driver=Driver(name,age,driving_license_number,driving_license_validity_period)
name=input("Enter  name:")
age=input("Enter age:")
driving_license_number=input("Enter driing license number:")
driving_license_validity_period=input("Enter license validity period:")
car_category=input("Enter the car catagory either MICRO or XL:")
car_number=input("Enter car number:")  
colour=input("Enter the color of the car:")
company=input("Enter the company name:")
model=input("Enter the model of car:")
car1=Car(name,age,driving_license_number,driving_license_validity_period,car_category,car_number,colour,company,model)


        
        

