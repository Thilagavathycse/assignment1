#f=open("mydetails_for_assignment.txt","x")
f=open("mydetails_for_assignment.txt","w")
f.write("i am thilagavathy,my dob is 4.10.1998")
f.close()
f=open("mydetails_for_assignment.txt","a")
f.write("i am BE(CSE) graduate")
f.close()
f=open("mydetails_for_assignment.txt","r")
print(f.readlines())
f.close()