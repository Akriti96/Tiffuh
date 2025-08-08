# ATM Machine (2 ATM requirement)
# blueprint
'''
- insert- pinnumber
- create pin
- menu 1. balance, withdraw, check, change pin, exit
'''

class ATM:
    def __init__(self):
        print("Welcome to SBI Bank ATM")
        self.menu()

    def menu(self):
        user_input= int(input("Hii How Can I help You? \n" \
        "1. Press 1 to create pin " \
        "2. Press 2 to change pin " \
        "3. Press 3 to Check Balance " \
        "4. Press 4 to withdraw " \
        "5. Anything else to exit :  "))

        if user_input == 1:
            self.create_pin()
         
        elif user_input == 2:
            self.change_pin()
           
        elif user_input == 3:
            self.check_balance()
   
        elif user_input ==4 :
            self.withdraw()
      
        elif user_input == 5:
            print("exit")
        else:
            print("Wrong option picked")
            self.menu()
          

    def create_pin(self):
        self.pin= int(input("Create a new pin: "))

        # user_balance= int(input("Enter the balance"))
        self.balance= 10 
        print(f"Your ATM pin is generated succefully and the pin is {self.pin} and balance is $ {self.balance}")
        self.menu()

    def change_pin(self):
        old_pin= int(input("Enter the old pin: "))
        if old_pin == self.pin:
            new_pin= int(input("Enter the new pin: "))
            self.pin= new_pin
            print(f"Your New ATM pin is generated succefully and the pin is {self.pin}")
            self.menu()

        else:
            print("Your Have entered worng pin")
            self.menu()

    def check_balance(self):
        user_pin= int(input("Enter the pin: "))
        if user_pin == self.pin:
            print(f"Your bank balance is: {self.balance}")
            self.menu()
        else:
            print("InCorrect Pin")
            self.menu()
        
    def withdraw(self):
        user_pin= int(input("Enter the pin: "))
        if user_pin == self.pin:
            amount= int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance= self.balance-amount
                print(f"With draw successful , balance is ${self.balance}")
            else:
                print("Enough balance")
            self.menu()
        else:
            print("InCorrect Pin")
            self.menu()

# object 
A1= ATM()


