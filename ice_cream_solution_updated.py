
class IceCream:
    def __init__(self,types,flavours,toppings):
        self.types=types
        self.flavours=flavours
        self.toppings=toppings
    def print_menu(self):
        print("****----****MENU CARD****----****")
        print("ITEM"+"      "+"RATE")
        for (k,v),(k2,v2) in zip (types.items(),flavours.items()):
            print(k,v)
            print(k2,v2)
    def user_choice(self):
        type=input("Enter an item :").lower()
        flavour=input("Enter a flavour:")
        quantity=int(input("enter the quantity in number"))
        if flavour=="chocolate":
            toppings={"choco chips":100,"caramel":90,"nuts":100}
            print("{} has toppings".format(flavour))
            for k,v in toppings.items():
                print(repr(k)+":"+repr(v))
            topping_choice=input("enter the topping choice or type or type NO ").lower()
            if topping_choice=="no":
                print("Total cost:{}".format(quantity*types[type]+flavours[flavour]))
            else:
                print("Total cost:{}".format(quantity*types[type]+flavours[flavour]))
        else:
            print("total cost:{}".format(quantity*types[type]+flavours[flavour]))
                
    """def total_cost(self):
         if flavour!="chocolate":
             print("total cost:{}".format(quantity*types[choice]+flavours[flavour]))"""
types={"stick":80,"cone":85,"cup":100}
flavours ={"chocolate":10,"vanilla":15,"strawberry":20}
toppings={"choco chips":45,"caramel":10,"nuts":18}
ice=IceCream(types,flavours,toppings)
ice.print_menu()
ice.user_choice()
