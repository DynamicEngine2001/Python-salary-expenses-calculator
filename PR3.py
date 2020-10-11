print("The salary and expenses Calculator...")
try :
    salary = float(input ("Insert the value of your salary:"))
    expenses = float(input ("Insert the value of your expenses:"))
    percentage = (expenses*100)/salary
    print("You spend ",percentage ,"%", "of your salary in your expenses.")
except :
    print("Enter A valid Number :")
