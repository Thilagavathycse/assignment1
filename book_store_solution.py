class Author:
    def __init__(self,author_name,book_name,author_age,nationality):
        self.author_name=author_name
        self.book_name=book_name
        self.author_age=author_age
        self.nationality=nationality
def count_number_of_book_written_by_specific_author(*Author):
    name_of_the_author=input("Enter the name of an author:")
    book_list_for_particular_author=[]
    for A in Author:
        if name_of_the_author==A.author_name:
            book_list_for_particular_author=book_list_for_particular_author+[A.book_name]
    print("Total number of book written by",name_of_the_author,"is",len(book_list_for_particular_author))
class Book:
    def __init__(self,author_name,book_name,author_age,nationality,price):
        self.book_name = book_name
        self.author_name =author_name
        self.price = price
        self.author=Author(author_name,book_name,author_age,nationality)
    def is_expensive(self):
        if self.price > 1000:
            return 
        else:
            print("Affordabe book name is {} which is  written by {}".format(self.book_name,self.author_name))
def calculate_price(*Book):
    total_rate=0
    for rate in Book:
        total_rate+=book1.price+book2.price+book3.price
    print("Total price of books in store:{}".format(total_rate))
print("welcome to the book world")    
book1=Book("guido van rossum","python",61,"dutch",999)
book2=Book("Martin Odersky","scala",64,"german",1500)
book3=Book("dennis ritchie","c",61,"ameriga",1999)
book4=Book("Bjarne Stroustrup","c++",61,"dutch",1999)
book5=Book("Martin Odersky","generic java",61,"ameriga",1999)
book6=Book("James Gosling","java",61,"canadian",599)
book1.is_expensive()
book2.is_expensive()
book3.is_expensive()
book4.is_expensive()
book5.is_expensive()
book6.is_expensive()
calculate_price(book1,book2,book3,book4,book5,book6)
count_number_of_book_written_by_specific_author(book1.author,book2.author,book3.author,book4.author,book5.author,book6.author)
