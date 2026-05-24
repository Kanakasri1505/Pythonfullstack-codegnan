user_info={"name":"saranya",
           "mob_no":"123456",
           "Atm_pin":"1505",
           "balance":50000}

print("PLEASE INSERT YOUR ATM CARD")
remaining_att=3
Transaction_hist=[]

while remaining_att > 0:
    Atm_pin=input("enter your ATM pin: ")
    if len(Atm_pin)==4 and Atm_pin==user_info['Atm_pin']:
        print("WELCOME TO THE BANK!")
        option=int(input("1.DEPOSIT \n 2.WITHDRAW \n 3.CHANGE PIN \n 4.CHECK BALANCE \n 5.TRANSACTION HISTORY "))
        
        if option == 1:
            deposit=int(input("ENTER THE AMOUNT TO BE DEPOSITED:"))
            if (deposit > 1000) and (deposit % 100==0) :
                user_info['balance'] += deposit
                Transaction_hist.append(f"RS {deposit} is deposited in your account")
                print(f" RS {deposit} is deposited in your account")
            else:
                print("amount should be more then 1000 or change cannot be deposited")
                
        elif option == 2:
            withdraw=int(input("ENTER THE AMOUNT TO BE WITHDRAWN:"))
            if (withdraw <= user_info['balance']):
                if (withdraw > 1000) and (withdraw % 100 == 0):
                    user_info['balance'] -= withdraw
                    Transaction_hist.append(f"RS {withdraw} is withdrawn from your account")
                    print(f"RS {withdraw} is withdrawn from your account")
                else:
                    print("amount should be more than 1000 or change cannot be withdrawn")
            else:
                print("INSUFFICIENT FUNDS!!!!")

        elif option ==3:
             Atm_pin=input("enter your ATM pin to continue pin change: ")
             if len(Atm_pin)==4 and Atm_pin==user_info['Atm_pin']:
                 new_pin=input("ENTER NEW PIN:")
                 user_info['Atm_pin']=new_pin
                 Transaction_hist.append("PIN CHANGED SUCCESSFULLY")
             else:
                print("INVALID PIN ENTERED!!")

        elif option == 4:
            Balance=user_info['balance']
            print(f" YOUR AVAILABLE BALANCE IS RS {Balance}")

        elif option == 5:
            print(Transaction_hist)
            
        choice=int(input(" 1. GO BACK TO MAIN PAGE \n 2.EXIT"))
        if choice == 2:
            print("THANK YOU FOR USING OUR ATM!!!")
    
                  
    else:
        print("ENTER 4 DIGIT PIN")
        remaining_att -= 1

        if remaining_att > 0:
            print(f"Invalid pin entered,you have {remaining_att} attempts left")
        else:
            print("Card is blocked Temporarily")
        
