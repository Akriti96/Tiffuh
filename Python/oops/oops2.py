# How objects access attributes
''''class Person:
    def __init__(self):
        self.name="Tiffuh"
        self.country= "USA"

    def greet(self):
        if self.country== "USA":
            print("Hello", self.name)
        else:
            print("Hola",self.name)

    # magical functions 
    def __str__(self):
        return f"hello {self.name} welcome to {self.country}"

# # p1
# p1= Person()
# # p2= Person()
# p2=p1
# p1.name="Johan"



# print(id(p1),id(p2))
# print(p2.name)
'''


# class Person():
#     def __init__(self,name, gender):
#         self.name= name
#         self.gender= gender


# def greet(person):
#     print(f"My name is {person.name} annd Im a {person.gender}")
#     return person


# p= Person("Johan","male")
# print(id(p))

# x= greet(p)
# print(id(x))

# encapsulation in python -- core fundamental concepts
# 5 attributes -- name, gender, country, email, phonenumber  
# person class  is public class -- (private attributes -- email, phobenumber)
'''class Person:
    def __init__(self):
        self.n= "Johan"
        self.g= "male"
        self.c= "USA"
        self.__e= "j@gamil.com"   # protected attribute
        self. p= "1234"

    def __str__(self):
        return f" Hello {self.n} Welcome to Data science program"
    
    def display(self):
        print(self.__e)   # access the email by public method
    

    
p1= Person()
print(p1)
p1.display()'''

'''class private:
    def __init__(self):
        self.__salary= 10000 # private attribute

    def __employee(self):      # private method
        return self.__salary
           

ob= private()
# print(ob.__salary)
print(ob.__employee())'''


class BankAccount:
    def __init__(self):
        self.balance= 10

    def __show_balance(self):
        print(f"Balance is $ {self.balance}")  # private method

    def __update_balance(self,amount):       # private method
        self.balance+= amount

    def deposit(self,amount):
        if amount >0:
            self.__update_balance(amount)   # accsing private method internally
            self.__show_balance()
        else:
            print("invalid amount")

        

a1= BankAccount()
# a1.__show_balance()  # wont work
a1.deposit(150)
