import sys

print("The salary and expenses Calculator:")
for _ in range(3):
  salary = input ("Insert the value of your salary:")
  try:
    s = float(salary)
    break
  except Exception as e:
    print("Please enter a valid Number")
else:
  print("couldn't read a valid salary number")
  sys.exit(1)

for _ in range(3):
  expenses = input ("Insert the value of your expenses:")
  try:
    e=float(expenses)
    break
  except Exception as e:
    print("Please enter a valid Number")
else:
  print("couldn't read a valid expense number")
  sys.exit(1)

percentage = (e*100)/s
print("Your spend ",percentage ,"%", "of your salary in your expenses.")
