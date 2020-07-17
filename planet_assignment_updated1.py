class Planet:
    one_earth_year=365.25
    def __init__(self,planet,diameter,moons,years):
        self.planet=planet
        self.diameter=diameter
        self.moons=moons
        self.years=years.lower()
    def calculate_radious_from_diameter(self):
        print("Radius of the {} is:{}".format(self.planet,self.diameter/2))
    def is_year(self):
        is_year=self.years.endswith("years")
        if is_year:
            year_list=self.years.split()#This list has splitted value of years
            no_of_days=float(year_list[0])*self.one_earth_year
            print("No of days present in "+self.planet+ " is {} days".format(no_of_days))
        else:
            print(self.years)
def largest_planet(*Planet):
   largest=max(mercury.diameter,venus.diameter,earth.diameter,mars.diameter,jupiter.diameter,saturn.diameter,uranus.diameter,neptune.diameter)
   for planets in Planet:
       if (planets.diameter == largest):
           print("The largest planet is {}".format(planets.planet))
mercury=Planet("Mercury",4879,0,"88 days")
venus=Planet("Venus",12100,0,"225 days")
earth=Planet("Earth",12755,1,"365 days")
mars=Planet("Mars",6786,2,"687 days")
jupiter=Planet("Jupiter",142800,79,"12 earth Years")
saturn=Planet("Saturn",120537,82,"29.5 earth years")
uranus=Planet("Uranus",51819,27,"84 earth years")
neptune=Planet("Neptune",49529,14,"165 earth years")
neptune.calculate_radious_from_diameter()
jupiter.is_year()
largest_planet(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)
