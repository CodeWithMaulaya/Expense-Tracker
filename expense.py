
expenses = []

def add_expenses():
    
    category = input("choose category(Food, transportation, fee, Data, Others ): ")
    try:
        amount = float(input("Enter amount(GHS): "))
    except:
        print("Input cannot be text")
    description = input("Description: ")
    try:
        expenses.append({"Category":category, "Amount": amount , "Description":description})
    except:
        print("Nothing is added")

def view_expenses():
    print("-"*60)
    print(f"\tCATEGORY\tAMOUNTt(GHS)\t\tDESCRIPTION")
    print("-"*60)
    for expenditure in expenses:
        print(f"\t{expenditure['Category']}\t\t{expenditure['Amount']}\t\t\t{expenditure['Description']}")
    print("-"*60)

def total_expenses():
    total_expenditure = sum(expenditure["Amount"] for expenditure in expenses)
    print("Total spent:", total_expenditure)
    print("")

def search_category():
    search = input("Search Category...... ")
    print(f"\tCATEGORY\tAMOUNT(GHS)\t\tDESCRIPTION")
    found = False
    for expenditure in expenses:
        if expenditure["Category"].lower() == search.lower():
            print(f"\t{expenditure['Category']}\t\t{expenditure['Amount']}\t\t\t{expenditure['Description']}")
            found = True
    if not found:
        print("No expenditure in this category")
    print("")



print("="*20+" EXPENSE TRACKER "+ "="*20)
while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spent")
    print("4. Search category")
    print("5. Exit")
    choice = ''
    try:
        choice = int(input("Choice: "))
    except:
        print("Input cannot be character(s)")

    if choice == 5:
        print("Thank you!")
        print("Track well, spend wisely.")
        break
    elif choice == 1:
        print("-"*20 + " Add Expenses "+ "-"*20)
        add_expenses()
        print("Expenses saved!")
        print()
    elif choice == 2:
        view_expenses()
    elif choice ==3:
        total_expenses()
    elif choice == 4:
        search_category()
    else:
        print("Invalid choice")
        print("")

        







