'''
In Python OOP, a static variable (also called a class variable) is a variable that belongs to the class itself, not to any single object.
All objects (instances) of the class share the same value of this variable.
If you change it, the change is reflected for all objects.
'''






# static variable

# Bank - customer 1(name, email, phone, account number, bank details(address, ifsccode, emai))

# johan   - 2months - Jiya
# close-savings - business account 


# class Student:
#     # static variable
#     school_name="ABC High School"

#     def __init__(self,name,roll):
#         # instance variables
#         self.name= name
#         self.roll=roll


# s1= Student('Johan',1234)
# print(s1.name,s1.roll,s1.school_name) 

# s2= Student("Priya",5678)
# print(s2.name,s2.roll,s2.school_name)


# # ABC high school, XYZ high school
# Student.school_name= "XYZ High School"

# # John mother decide change him to new school called KLM
# s1.school_name= "KLM High School"

# print(s1.school_name, s2.school_name)



'''
Goal:
We need a class to represent employees in a company.
Each employee has name, ID, salary (instance variables).
But the company name and the total number of employees hired are static variables (shared across all employees).
'''
class Employee:
    # static variables
    company_name="Amzon"
    total_employees=100


    def __init__(self,name,emp_id,salary):
        # instance
        self.n= name
        self.em_i= emp_id
        self.s= salary

       # update static variable
        Employee.total_employees+=1

    def __str__(self):
        return f"Name :{self.n} Id {self.em_i} salary {self.s}"
    

    @staticmethod
    def company_info():
        # static method accessing static variable
        print(f"Company :{Employee.company_name} Total Employees {Employee.total_employees}")


# hired 
E1= Employee("Yamuna",1567,1000)
E2= Employee("Johan", 2345, 900)

print(E1.company_info(), E2.company_info())