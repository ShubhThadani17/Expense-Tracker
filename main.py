import json
import os 
import sys 

class tracker:
    def __init__(self,file="data.json"):
        self.file=file
        self.data=self.load_data()

    def load_data(self):
        if os.path.exists(self.file):
            return []
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except:
            return []
        
    def save_data(self):
        with open(self.file, "w") as file:
            json.dump(self.data, file)
    
    def add(self):
        try:
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            expense = {"name": name,"amount": amount}
            self.data.append(expense)
            self.save_data()
            print("Expense added.")
            
        except ValueError:
            print("amount invalid")
    
    def view_expenses(self):
        if not self.data:
            print("No expenses found.")
            return
        
        for exp in self.data:
            print(f"{exp['name']} - ₹{exp['amount']}")

    def total_spending(self):
        if(self.data):
            sum=0
            for exp in self.data:
                sum+=exp['amount']
            print(f"Total spending: ₹{sum}")
    
    def delete_expense(self):
        if (not self.data):
            print("No expenses to delete.")
            return
        self.view_expenses()
        try:
            choice = int(input("Enter number to delete: "))
            if 1 <= choice <= len(self.data):
                removed = self.data.pop(choice - 1)
                self.save_data()
                print(f"Deleted: {removed['name']} - ₹{removed['amount']}")
            else:
                print("Invalid number.")

        except ValueError:
            print("Please enter a valid number.")
    
    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Total Spending")
            print("4. Delete Expense")
            print("5. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.total_spending()
            elif choice == "4":
                self.delete_expense()
            elif choice == "5":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    track = tracker()
    track.run()