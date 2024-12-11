def show_balance():
    print(f'Your balce is ₹{balance:.2f}') 


def deposit():
    pass

def withdraw():
    pass


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4) : ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not valid choice!!!")
    
print("Thank you!! Have nice day")
    