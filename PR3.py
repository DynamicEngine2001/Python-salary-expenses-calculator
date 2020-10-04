print("The salary and expenses Calculator:")
try :
    salary = input ("Insert the value of your salary:")
    s = float(salary)
    expenses = input ("Insert the value of your expenses:")
    e=float(expenses)
    percentage = (e*100)/s
    print("Your spend ",percentage ,"%", "of your salary in your expenses.")
except :
    print("Enter A valid Number !")
