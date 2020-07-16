class Planet_Class:
    def __init__(self,planet,diameter,moons,years):
        self.planet=planet
        self.diameter=diameter
        self.moons=moons
        self.years=years
        self.largest=largest_planet
    def Radious(self):
        radius=self.diameter/2
        print("Radius:",radius)
    def number_of_days(self):
        year_or_days=self.years.endswith("years")
        if year_or_days:
            l1=self.years.split()#This list has splitted value of years
            year_or_days=float(l1[0])*365.25
            print("No of days present in "+self.planet+ " is {} days".format(year_or_days))
        else:
            print(self.years)
def largest_planet(Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune):
   largest=max(Mercury.diameter,Venus.diameter,Earth.diameter,Mars.diameter,Jupiter.diameter,Saturn.diameter,Uranus.diameter,Neptune.diameter)
   print(largest)
Mercury=Planet_Class("Mercury",4879,0,"88 days")
Venus=Planet_Class("Venus",12100,0,"225 days")
Earth=Planet_Class("Earth",12755,1,"365 days")
Mars=Planet_Class("Mars",6786,2,"687 days")
Jupiter=Planet_Class("Jupiter",142800,79,"12 earth years")
Saturn=Planet_Class("Saturn",120537,82,"29.5 earth years")
Uranus=Planet_Class("Uranus",51819,27,"84 earth years")
Neptune=Planet_Class("Neptune",49529,14,"165 earth years")
Neptune.Radious()
Jupiter.number_of_days()
largest_planet(Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune)
