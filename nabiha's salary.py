#this function is used to get the salary details from the user
def get_salary_details():
    salary = float(input("Enter your salary for the month: ")) 
    month = input("Enter the name of the month: ") 
    return salary, month
#this function is used to get the percentages of the rent, savings and electricity 
def get_percentages():
    savings_percentage = float(input("Enter the percentage of your salary that goes to rent: ")) / 100
    rent_percentage = float(input("Enter the percentage of your salary that goes to savings: ")) / 100
    electricity_percentage = float(input("Enter the percentage of your salary that goes to electricity: ")) / 100
    return {
        "savings": savings_percentage,
        "rent": rent_percentage,
        "electricity": electricity_percentage
        }
   #this dictionary is used to store the percentages of the rent, savings and electricity    

   #this function is used to calculate the allocations, total expenses, remainder, yearly rent and yearly electricity
def calculate_allocations(salary, percentages):
    allocations = {category: salary * percentages[category] for category in percentages} 
    total_expenses = sum(allocations.values()) 
    remainder = salary - total_expenses 
    yearly_rent = allocations['Rent'] * 12 
    yearly_electricity = allocations['Electricity'] * 12 
    return allocations, total_expenses, remainder, yearly_rent, yearly_electricity
    #i used two dictionaries to store the allocations and the percentages 

def extra_calculations(salary, savings_amount): #this function is used to calculate the square of the salary and the leftover from the random savings
    random_savings = 50 
    leftover_from_random_savings = random_savings / savings_amount if savings_amount else 0 
    return salary ** 2, leftover_from_random_savings 
# this function is used to display the results of the salary report
def display_results(month, salary, allocations, total_expenses, remainder, yearly_rent, yearly_electricity, squared_salary, leftover_from_random_savings):
    print(f"\nSalary Report for {month}")
    print(f"Total Salary: ${salary:.2f}")
    for category, amount in allocations.items():
         print(f"{category}: ${amount:.2f}") 
         print(f"Total Expenses: ${total_expenses:.2f}")
         print(f"Remaining Salary: ${remainder:.2f}")
         print(f"Yearly Rent Estimate: ${yearly_rent:.2f}")
         print(f"Yearly Electricity Estimate: ${yearly_electricity:.2f}")
         print(f"Salary Squared (Just for Fun!): {squared_salary:.2f}")
         print(f"Leftover from Additional Savings: ${leftover_from_random_savings:.2f}")