class Vehicle(object):
    def __init__(self, vehicle_type, ac, range):
        self.vehicle_type = vehicle_type
        self.ac = ac
        self.range = range


class Micro:
    max_people_limit = 4
    vehicle_type = 'micro'
    is_ac_available = True
    is_non_ac_available = True

    def __init__(self, min_range, max_range, price_with_ac, price_without_ac):
         self.price_with_ac = price_with_ac
         self.price_without_ac = price_without_ac
         self.min_range = min_range
         self.max_range = max_range


class Auto:
    max_people_limit = 3
    vehicle_type = 'auto'
    is_ac_available = True
    is_non_ac_available = False

    def __init__(self, min_range, max_range, price_with_ac, price_without_ac = None):
        self.price_with_ac = price_with_ac
        self.price_without_ac = price_without_ac
        self.min_range = min_range
        self.max_range = max_range


class Xl:
    max_people_limit = 10
    vehicle_type = 'xl'
    is_ac_available = True
    is_non_ac_available = True

    def __init__(self, min_range, max_range, price_with_ac, price_without_ac):
        self.price_with_ac = price_with_ac
        self.price_without_ac = price_without_ac
        self.min_range = min_range
        self.max_range = max_range


def filter_vehicle(vehicle_select):
    user_vehicle = next((vehicle for vehicle in vehicle_obj_list if vehicle.vehicle_type == vehicle_select), None)
    return user_vehicle


def display_category():
    print('We have different categories of vehicle:')
    vehicle_type_list = []
    for vehicle in vehicle_obj_list:
        if vehicle.vehicle_type not in vehicle_type_list:
            print('{} (Maximum upto {} people)'.format(vehicle.vehicle_type, vehicle.max_people_limit))
            vehicle_type_list.append(vehicle.vehicle_type)


def get_user_input():
    while True:
        vehicle_select = input('\nSelect the category from the above list(Eg.micro) : ').lower().strip()
        selected_vehicle = filter_vehicle(vehicle_select)
        if selected_vehicle is None:
            print("Not a valid choice.")
        else:
            break

    while True:
        ac_select = input('Do you want Ac {}? (yes/no): '.format(selected_vehicle.vehicle_type)).strip().lower()
        if ac_select == 'yes':
            if selected_vehicle.is_ac_available:
                return selected_vehicle, ac_select
            else:
                print('We have only Non-Ac {}\'s, suggest you to go with Non-Ac vehicle\n'.format(selected_vehicle.vehicle_type))
                ac_select = 'no'
                return selected_vehicle, ac_select
        elif ac_select == 'no':
            if selected_vehicle.is_non_ac_available:
                return selected_vehicle, ac_select
            else:
                print('We have only Ac {}\'s, suggest you to go with Ac vehicle\n'.format(selected_vehicle.vehicle_type))
                ac_select = 'yes'
                return selected_vehicle, ac_select


def price_menu(selected_vehicle, ac_select):
    for vehicle in vehicle_obj_list:
        if selected_vehicle.vehicle_type == vehicle.vehicle_type:
            if ac_select == 'yes':
                print('Ac {} vehicle range: {}-{} price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.min_range, vehicle.max_range, vehicle.price_with_ac))
            elif ac_select == 'no':
                print('Non-Ac {} vehicle range: {} price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.min_range, vehicle.max_range, vehicle.price_without_ac))
    print('\nYour ride is booked successfully')


auto1 = Auto(0, 15, 10)
auto2 = Auto(15, 30, 8)
auto3 = Auto(30, 1500, 15)
micro1 = Micro(0, 15, 12, 14)
micro2 = Micro(15, 1500, 10, 12)
xl1 = Xl(0, 15, 14, 15)
xl2 = Xl(15, 1500, 14, 15)
vehicle_obj_list = [auto1, auto2, auto3, micro1, micro2, xl1, xl2]

display_category()
selected_vehicle, ac_select = get_user_input()
price_menu(selected_vehicle, ac_select)

