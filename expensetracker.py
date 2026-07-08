import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except: 
    expenses = []
while True:
        print("--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        print("4. Delete Expense")
        inputnumber = int(input("Enter a number:"))
        
        if inputnumber == 1:
            print("Add expense selected")
            amount = int(input("Enter the amount:"))
            category = input("Enter the category:")
            myexpensedict = {"Amount": amount, "Category": category}
            expenses.append(myexpensedict)
            with open ("expenses.json", "w")as file:
                json.dump(expenses, file)
        elif inputnumber ==2:
            print("View expenses selected")
            for index, item in enumerate(expenses):
                print("Expense", index +1, "Amount = ", item["Amount"], "Catergory = ", item["Category"])


        
             
        elif inputnumber ==3:
            print("Goodbye")
            break
        elif inputnumber ==4:
            deletenumberinput = int(input("Enter the number to be deleted: "))
            realposition = deletenumberinput - 1
            del expenses[realposition]
            print("Expense deleted")
            with open ("expenses.json", "w")as file:
                json.dump(expenses, file)
            
        else:
            print("Invalid option, try again:")
 
        

