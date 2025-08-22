# Parent Class
'''class Animal:
    def __init__(self,name):
        self.animalName= name
        self.age= 20

    def speak(self):
        print(f"{self.animalName} makes a sound")


# Child Class
class Dog(Animal):
    def speak(self):
        print(f"{self.animalName} Barks")
        print(f" The life time of the animal is {self.age} years" )



class Tiger:
    pass


class Lion:
    pass


dog= Dog("Tommy")'''
# dog.speak()



# Parent
class Employee:
    company_name="Amazon"

    def __init__(self,name,emp_id,salary):
        # instance
        self.n= name
        self.em_i= emp_id
        self.s= salary

    def display_info(self):
        print(f"Name :{self.n} id {self.em_i} salary {self.s}")


# child class
class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)  # calling the parent constructor 
        self.teamSize= team_size

    def manger_display_info(self):
       super().display_info()  # reuse the parents method
       print(f"Team size {self.teamSize}")

# develepor 
class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)  # calling the parent constructor 
        self.Programming_langugae= language

    def develpoer_display_info(self):
       super().display_info()  # reuse the parents method
       print(f"Programming lang {self.Programming_langugae}")


# M1= Manager("Reehan",201,9000,10)
# M1.manger_display_info()

d1= Developer("Yamuna", 1234, 9000,"Python")
d1.n= "tiffuh"

print("After changed")
d1.develpoer_display_info()


# Session will be creating poly- projects  (hands oops ) (interview based- python - oops)