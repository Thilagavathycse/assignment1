dictionary={"Spain":"Europe","japan":"Asia","India":"Asia","Italy":"Europe","Thailand":"Asia","Sudan":"Africa"}
Desired_country=input(" Desired continent:")
for key,value in dictionary.items():
    if value==Desired_country:
        print(key)
