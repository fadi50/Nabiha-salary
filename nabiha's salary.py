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