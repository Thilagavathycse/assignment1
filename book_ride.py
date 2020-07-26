
class TransportationService:
    def __init__(self,category,range_in_km):
        self.category=category
        self.range_in_km=range_in_km
class TransportationserviceCost:
    def __init__(self,category,range_in_km,price_with_or_without_ac):
        self.price_with_or_without_ac=price_with_or_without_ac
        self.service=TransportationService(category,range_in_km)
def print_price_menu(*TransportationserviceCost):
    for t in TransportationserviceCost:
            if t.service.category == "auto" and t.price_with_or_without_ac=="ac":
                if t.service.range_in_km<15:
                    print(t.service.range_in_km*10)
                elif t.service.range_in_km>=15 and t.service.range_in_km <=30:
                    print(service.range_in_km*8)
                else:
                    print(service.range_in_km*15)
                    break
            else:
                print("auto is not available without ac")
                break
                
    if t.service.category == "micro" and t.price_with_or_without_ac=="ac":
        if t.service.range_in_km<15:
            print("the rate is {}".format(12*t.service.range_in_km))
        elif t.service.range_in_km>=15:
            print("the rate is {}".format(10*t.service.range_in_km))
    elif t.service.category == "micro" and t.price_with_or_without_ac=="non ac":
        if t.service.range_in_km<15:
            print("the rate is {}".format(14*t.service.range_in_km))
        else:
            print("the rate is {}".format(12*t.service.range_in_km))

    if t.service.category == "xl" and t.price_with_or_without_ac=="ac":
        if t.service.range_in_km>15:
            print("The rate is {}".format(14*t.service.range_in_km))
    elif t.service.category == "xl" and t.price_with_or_without_ac==" non ac":
            print("The rate is {}".format(15*t.service.range_in_km))

while True:
    category_type=input("Enter the category").lower()
    if category_type in ["auto","micro","xl"]:
        break
    else:
        print("not available")
km_range=int(input("Enter the range"))
ac_or_non_ac=input("Ac or non ac").lower()
cost=TransportationserviceCost(category_type,km_range,ac_or_non_ac)
#cost.service.get()
print_price_menu(cost)
        
         

            
