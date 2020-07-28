class Range:
    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range

    def get_range(self):
        return '{}-{}'.format(self.min_range, self.max_range)

class Ac:
    def __init__(self, select_ac,min_range, max_range, price_per_km):
        self.select_ac = select_ac
        self.price_per_km = price_per_km
        self.range = Range(min_range, max_range)

    def get_ac_price(self):
        return self.price_per_km

class NonAc:
    def __init__(self, select_ac,min_range, max_range, price_per_km):
        self.select_ac = select_ac
        self.price_per_km = price_per_km
        self.range = Range(min_range, max_range)

    def get_non_ac_price(self):
        return self.price_per_km

class Vehicle:
    def __init__(self, vehicle_type, max_people_limit, min_range, max_range, select_ac, price_per_km):
        self.vehicle_type = vehicle_type
        self.max_people_limit = max_people_limit
        self.select_ac = select_ac
        if select_ac == 'yes':
            self.ac = Ac(select_ac,  min_range, max_range, price_per_km)
        else:
            self.non_ac = NonAc(select_ac,  min_range, max_range, price_per_km)
        self.price_per_km = price_per_km

def display_category():
    print('We have different categories of vehicle:')
    vehicle_type_list = []
    for vehicle in vehicle_obj_list:
        if vehicle.vehicle_type not in vehicle_type_list:
            print('{} (Maximum upto {} people)'.format(vehicle.vehicle_type, vehicle.max_people_limit))
            vehicle_type_list.append(vehicle.vehicle_type)

def customer_selection():
    vehicle_select = input('\nSelect the category from the above list(Eg.micro) : ').lower().strip()
    for vehicle in vehicle_obj_list:
        if vehicle_select == vehicle.vehicle_type:
                if vehicle_select == 'auto':
                    decision=input("auto is not available without AC,do you want to choose another category(yes/no):")
                    ac_select = 'yes'
                    if decision == "no":
                        price_menu(vehicle_select, ac_select)
                        break
                    else:
                        vehicle_select = input('\nSelect the category from the above list(Eg.micro) : ').lower().strip()
                        if vehicle_select == vehicle.vehicle_type:
                            price_menu(vehicle_select, ac_select)
                        
                else:
                    ac_select = input('Do you want Ac vehicle? (yes/no): ').strip().lower()
                price_menu(vehicle_select, ac_select)
                break
    else:
        print('Wrong input, try again')

def price_menu(vehicle_select, ac_select):
    for vehicle in vehicle_obj_list:
        if vehicle_select == vehicle.vehicle_type:
            if vehicle.select_ac == 'yes':
                if ac_select == 'yes':
                    print('Ac {} vehicle range:{}km price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.ac.range.get_range(), vehicle.ac.get_ac_price()))
            elif vehicle.select_ac == 'no':
                if ac_select == 'no':
                    print('Non-Ac {} vehicle range:{}km price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.non_ac.range.get_range(), vehicle.non_ac.get_non_ac_price()))
    preference=input("Do you want to book (yes/no):")
    if preference == "yes":
        print('\nYour ride is booked successfully')
    else:
        customer_selection()
        

auto1 = Vehicle('auto', 3, 0, 15, 'yes', 10)
auto2 = Vehicle('auto', 3, 15, 30, 'yes', 8)
auto3 = Vehicle('auto', 3, 30, 1500, 'yes', 15)
micro1 = Vehicle('micro', 4, 0, 15, 'yes', 12)
micro2 = Vehicle('micro', 4, 15, 1500, 'yes', 10)
micro3 = Vehicle('micro', 4, 0, 15, 'no', 14)
micro4 = Vehicle('micro', 4, 15, 1500, 'no', 12)
xl1 = Vehicle('xl', 10, 0, 15, 'yes', 14)
xl2 = Vehicle('xl', 10, 15, 1500, 'yes', 14)
xl3 = Vehicle('xl', 10, 0, 15, 'no', 15)
xl4 = Vehicle('xl', 10, 15, 1500, 'no', 15)
vehicle_obj_list = [auto1, auto2, auto3, micro1, micro2, micro3, micro4, xl1, xl2, xl3, xl4]

display_category()
customer_selection()



