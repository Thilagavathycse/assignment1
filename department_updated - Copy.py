class Department:
    def __init__(self,department_name,student_names,student_id,subject_taken,courses_offered):
        self.department_name=department_name
        self.student_names=student_names
        self.student_id=student_id
        self.subject_taken=subject_taken
        self.courses_offered=courses_offered
    def display_name(self):
        print("Name of the department is:{}".format(self.department_name))
        print("name of the students in the above department is:",*self.student_names)
    def more_than_three_subject_department(self):
        length_of_subject_taken1=len(self.subject_taken[0])
        length_of_subject_taken2=len(self.subject_taken[1])
        if length_of_subject_taken1 >= 3 or length_of_subject_taken2 >= 3:
            print("More than three subject taking student blong to this department:",self.department_name)
        else:
            print("There is no one else taking three subjects")
def find_and_print_overlapping_courses(*Department):
    from collections import Counter
    courses_offered_list=list((depart1.courses_offered)+(depart2.courses_offered)+(depart3.courses_offered))
    courses_offered_list_in_lower=list(map(lambda x:x.lower(),courses_offered_list))
    overlapping_courses=[k for k,v in Counter(courses_offered_list_in_lower).items() if v>1]
    print("Overlapping courses are:",*overlapping_courses, sep=" ")
depart1=Department("CSE",["thilaga","sangeetha"],["id1","id2"],[["pds","c++","oop"],["pds"]],["pds","c++","OOP"])
depart2=Department("ECE",["Usha","Kaali"],["id3","id4"],[["oop","pds","communication system"],["Communication system"]],["pds","oop","Communication system"])
depart3=Department("IT",["Mano","Monika"],["id3","id4"],[["oop","pds","communication system","python"],["communication system","python"]],["python","pds","oop","COMMUNICATION SYSTEM"])
depart1.display_name()
depart2.display_name()
depart3.display_name()
depart1.more_than_three_subject_department()
depart2.more_than_three_subject_department()
depart3.more_than_three_subject_department()
find_and_print_overlapping_courses(depart1,depart2,depart3)

