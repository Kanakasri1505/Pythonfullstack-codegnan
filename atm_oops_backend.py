
class ATM:
    def __init__(self):
        self.name = "saranya"
        self.mob_no = "123456"
        self.__pin = "1505"
        self.__balance = 50000
        self.transaction_history = []
        
###---------------------to verify pin-------------------------------
        
    def verify_pin(self):
        remaining_att = 3
        while remaining_att > 0:
            atm_pin = input("Enter your ATM PIN: ")
            if len(atm_pin) == 4 and atm_pin == self.__pin:
                print("WELCOME TO THE BANK!")
                return True

            remaining_att -= 1

            if remaining_att > 0:
                print(f"Invalid PIN entered, you have {remaining_att} attempts left")
            else:
                print("Card is blocked temporarily")
                return False
            
##--------------------------to deposit---------------------------------
            
    def deposit(self):
        amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED: "))
        if amount > 1000 and amount % 100 == 0:
            self.__balance += amount
            self.transaction_history.append(f"Rs {amount} is deposited in your account")
            print(f"Rs {amount} is deposited in your account")

        else:
            print("Amount should be more than 1000 and in multiples of 100")
            
##--------------------------to withdraw--------------------------------------
            
    def withdraw(self):
        amount = int(input("ENTER THE AMOUNT TO BE WITHDRAWN: "))
        if amount <= self.__balance:
            if amount > 1000 and amount % 100 == 0:
                self.__balance -= amount
                self.transaction_history.append(f"Rs {amount} is withdrawn from your account")
                print(f"Rs {amount} is withdrawn from your account")
            else:
                print("Amount should be more than 1000 and in multiples of 100")

        else:
            print("INSUFFICIENT FUNDS!!!!")
            
##------------------------to change pin------------------------------------------
            
    def change_pin(self):
        old_pin = input("Enter current PIN: ")
        if old_pin == self.__pin:
            new_pin = input("Enter new PIN: ")
            if len(new_pin) == 4:
                self.__pin = new_pin
                self.transaction_history.append("PIN CHANGED SUCCESSFULLY")
                print("PIN CHANGED SUCCESSFULLY")
            else:
                print("PIN must be 4 digits")

        else:
            print("INVALID PIN ENTERED!!")
            
##-------------------------to check balance--------------------------------------------
            
    def check_balance(self):
        print(f"YOUR AVAILABLE BALANCE IS Rs {self.__balance}")
        
##------------------------to check trnasaction-----------------------------------------
        
    def show_transaction_history(self):
        for trans in self.transaction_history:
            print(trans)
            
##------------main-----------------------------
            
    def menu(self):
        if self.verify_pin():
            while True:
                print("1. DEPOSIT \n 2. WITHDRAW \n 3. CHANGE PIN \n 4. CHECK BALANCE \n 5. TRANSACTION HISTORY")
                option = int(input("ENTER YOUR OPTION: "))

                if option == 1:
                    self.deposit()

                elif option == 2:
                    self.withdraw()

                elif option == 3:
                    self.change_pin()

                elif option == 4:
                    self.check_balance()

                elif option == 5:
                    self.show_transaction_history()

                else:
                    print("Invalid option")

                choice = int(input("\n 1. GO BACK TO MAIN PAGE \n 2. EXIT \n Enter Choice: " ))

                if choice == 2:
                    print("THANK YOU FOR USING OUR ATM!!!")
                    break


print("PLEASE INSERT YOUR ATM CARD")
atm1 = ATM()
atm1.menu()
