#The given list contains 5 items
list1=["abc",[2,3,("xyz","the avengers")],1,2,3]
#second list of list1 contains 3  items,i am assigning it to different variable
sec_list_item1,sec_list_item2,sec_list_item3=list1[1]
"""print(sec_list_item1,sec_list_item2,sec_list_item3)
sec_list_item3 has 2 items,second item is "the avengers" i want to split it to get avengers"""
splitted_item=sec_list_item3[1].split()#split operation on "the avengers " item
print(splitted_item[1])
