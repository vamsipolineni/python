class Bank:

    def __init__(self, customername, balance=0.0):
        self.name = customername
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Amount should be greater than 0")
        return self._balance

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient Funds or invalid amount")
        return self._balance

    def balance(self):
        return self._balance


name = input("Enter your name: ")
b = Bank(name)

while True:
    print("\nPress 'd' - Deposit | 'w' - Withdraw | 'b' - Balance | 'e' - Exit")
    choice = input("Enter your choice: ").lower()

    if choice == 'e':
        print("Thank you for banking!")
        break

    elif choice == 'b':
        print(f"Account balance: {b.balance()}")

    elif choice in ('d', 'w'):
        while True:
            amt_input = input("Enter your amount: ")
            try:
                amt = float(amt_input)
                break  # valid amount, exit the loop
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if choice == 'd':
            b.deposit(amt)
        elif choice == 'w':
            b.withdraw(amt)

    else:
        print("Invalid choice. Try again.")