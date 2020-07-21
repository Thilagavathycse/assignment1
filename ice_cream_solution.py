def print_menu():
    types={"stick":80,"cone":85,"cup":100}
    flavours ={"chocolate":80,"vanilla":100,"strawberry":120}
    print("***MENU***")
    for (k,v), (k2,v2) in zip(types.items(), flavours.items()):
        print("type {} : rate {}".format(k,v))
        print("flavour {} : rate {}".format(k2,v2))
    def get_user_choice_and_print_total_cost():
        choice=input("enter your choice").lower()
        flavour=input("enter the flavour").lower()
        quantity=int(input("enter the quantity"))
        print("you want {} and flavour {} and quantity {}".format(choice,flavour,quantity))
        if flavour=="chocolate":
            toppings={"choco chips":100,"caramel":90,"nuts":100}
            print("{} has toppings".format(flavour))
            for k,v in toppings.items():
                print(repr(k)+":"+repr(v))
            topping_choice=input("enter the topping choice").lower()
            print("Total cost:{}".format(quantity*types[choice]+flavours[flavour]+toppings[topping_choice]))
        
        else:
             print("total cost:{}".format(quantity*types[choice]+flavours[flavour]))
    get_user_choice_and_print_total_cost()
print_menu()
            

    
    
    
