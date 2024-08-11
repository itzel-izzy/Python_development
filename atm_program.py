# ATM class to handle all operations related to an ATM machine
class ATM:
    # Constructor to initialize the ATM with a PIN and an optional balance
    def __init__(self, pin, balance=0):
        self.pin = pin  # Store the PIN
        self.balance = balance  # Initialize balance (default is 0)
        self.transaction_history = []  # List to store transaction history

    # Method to check if the entered PIN matches the stored PIN
    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    # Method to check the current account balance
    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    # Method to deposit cash into the account
    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount  # Add the deposit amount to the balance
            self.transaction_history.append(f"Deposited: ${amount:.2f}")  # Record the transaction
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")  # Validate the deposit amount

    # Method to withdraw cash from the account
    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Subtract the withdrawal amount from the balance
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")  # Record the transaction
            print(f"Successfully withdrew ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")  # Check if there are enough funds for withdrawal
        else:
            print("Withdrawal amount must be positive.")  # Validate the withdrawal amount

    # Method to change the account PIN
    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin  # Update the PIN
            self.transaction_history.append("PIN changed.")  # Record the PIN change
            print("PIN successfully changed.")
        else:
            print("Incorrect old PIN.")  # Validate the old PIN

    # Method to show the transaction history
    def show_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)  # Display each transaction
        else:
            print("No transactions made yet.")  # Handle the case of no transactions

# Main program to simulate ATM operations
def main():
    # Create an ATM object with a default PIN and initial balance
    atm = ATM(pin="1234", balance=1000.00)

    # Loop to display the ATM menu and handle user input
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                atm.check_balance()  # Display the balance if the PIN is correct
            else:
                print("Incorrect PIN.")

        elif choice == "2":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw_cash(amount)  # Withdraw cash if the PIN is correct
            else:
                print("Incorrect PIN.")

        elif choice == "3":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                amount = float(input("Enter amount to deposit: "))
                atm.deposit_cash(amount)  # Deposit cash if the PIN is correct
            else:
                print("Incorrect PIN.")

        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.change_pin(old_pin, new_pin)  # Change PIN if the old PIN is correct

        elif choice == "5":
            entered_pin = input("Enter your PIN: ")
            if atm.check_pin(entered_pin):
                atm.show_transaction_history()  # Show transaction history if the PIN is correct
            else:
                print("Incorrect PIN.")

        elif choice == "6":
            print("Exiting...")  # Exit the program
            print("Thank you for using our ATM service!")  # Thank you message
            break

        else:
            print("Invalid choice. Please select a valid option.")  # Handle invalid menu choice


if __name__ == "__main__":
    main()  # Run the main program
