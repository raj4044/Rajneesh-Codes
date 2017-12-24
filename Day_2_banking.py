balance=0

user_input=input("""Welcome! What do you want to do?
1. Display Balance
2. Deposit
3. Withdrawal
4. Exit""")

while user_input != '4' :
    if user_input=='1':
        print("Your balance : ", balance)
        user_input=input("""Welcome! What do you want to do?
    1. Display Balance
    2. Deposit
    3. Withdrawal
    4. Exit""")
    elif user_input=='2':
        D_amount=int(input("Amount to deposit : "))
        balance=balance+D_amount
        user_input=input("""Welcome! What do you want to do?
    1. Display Balance
    2. Deposit
    3. Withdrawal
    4. Exit""")
    else:
        W_amount=int(input("Amount to withdraw : "))
        balance=balance-W_amount
        user_input=input("""Welcome! What do you want to do?
    1. Display Balance
    2. Deposit
    3. Withdrawal
    4. Exit""")
