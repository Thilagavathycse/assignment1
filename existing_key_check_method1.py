my_dict={}
n=int(input("number of elements"))
for i in range(n):
    keys=input("enter key:")
    value=input("enter values:")
    my_dict.update({keys:value})
key_to_ckeck=input("enter the key")
if key_to_ckeck in my_dict:
    print("key found")
else:
    print("not found")
    
