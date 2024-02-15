def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'\nAmount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_by_category(expenses, category):
    return filter(map(lambda expense: expense['category'] == category, expenses))


def main():
    expenses = []

    while True:
        print('\nWelcome to Expense Tracker')
        print('1. Add Expenses')
        print('2. List All Expenses')
        print('3. Total Expenses')
        print('4. Filter Expenses by Category')
        print('5. Exit')
        
        choice = input('\nEnter your choice: ')

        match choice:

            case '1':
                amount = float(input("\nEnter amount: "))
                category = input("Enter category: ")
                add_expense(expenses, amount, category)

            case '2':
                print('\nAll Expenses')
                print_expenses(expenses)

            case '3':
                print('\nTotal Expenses: ',total_expenses(expenses))
            
            case '4':
                category = input('Enter category to filter: ')
                print(f'\nExpenses for {category}: ')
                expense_by_category = filter_by_category(expenses, category)
                print_expenses(expense_by_category)

            case '5':
                print('Goodbye!')
                break


if __name__ == '__main__':
    main()