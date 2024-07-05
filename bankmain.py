class BankAccount:
    def __init__(self, owner_name, balance, address, accountnumber):
        self._owner_name = owner_name
        self.__balance = float(balance)
        self.__address = address
        self.__accountnumber = accountnumber
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount :
            self.__balance -= amount
            return self.__balance
        else:
            return print(f"Sorry {self._owner_name}, but you have insufficient funds for this withdraw.")
    def get_balance(self):
        return print(f"Hello {self._owner_name}, Your current balance is : ${self.__balance}")
    def get_info(self):
        infolst = ((f"Welcome {self._owner_name}, here is your account info."), (f"Your account numbers is : {self.__accountnumber }"), (f"Your billing address is : {self.__address}"), (""), (f"Your current balance with SimpleBank is : $ {round(self.__balance, 2)}"))
         
        return infolst
    def get_name(self):
        return self._owner_name
    def get_number(self):
        return self.__accountnumber
    def updated_balance(self):
        return self.__balance

def negativecheck(input):
    a = input
    if a < 0:
        print("Please try again with a postitive number.")
        quit()
    else:
        print(f"Thank you, processing now...")
        

users = [BankAccount("Susan George", 5326.57, "Palm Springs, California(CA), 92262", "#4594"), BankAccount("Willie Finkel", 2624.94, "Cape Coral, Florida(FL), 33990", "#4587"), BankAccount("Jeannette George", 225.13, "Rock Island, Illinois(IL), 61201", "#7703")]

def main():
    user_name = str(input("Hello Welcome to SimpleBank, please enter your full name."))
    user_anum =  str(input(f"Thank you {user_name}, now please enter your account number : "))
    for i in users:
        if user_name != i.get_name() and user_anum != i.get_number():
            continue
        elif user_name == i.get_name() and user_anum == i.get_number():
            print(f"Welcome back to SimpleBank,{user_name}")
            usr = i
            break
        print("Sorry but we are unable to find your account, please try again")
        quit()
    choice = 0
    while True:
        print("\nSimpleBank")
        print("--------------------")
        print("1. Deposit ")
        print("2. Withdraw")
        print("3. Account Info")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        choice = int(choice)
        if choice == 1:
            u_deposit = float(input("How much would like to desposit? : $ " ))
            negativecheck(u_deposit)
            usr.deposit(u_deposit)
            print(f"Current balance : $ {round(usr.updated_balance(), 2)}") 
            
        elif choice == 2:
            usr.get_balance()
            u_withdraw = float(input("Please enter how much you would like to withdraw : $ "))
            negativecheck(u_withdraw)
            usr.withdraw(u_withdraw)
            print(f"Your balance is now $ {round(usr.updated_balance(), 2)}")                      
        elif choice == 3:
           for i in usr.get_info():
               print(i)
        elif choice == 4:
            print(f"Thanks again for using SimpleBank, farewell and come back again!")
            quit()

if __name__ == "__main__":
    main()