# Chapter IV problem III budget analysis by Vincenzo Scotto Di Uccio

budget = float(input(" What is your budget for this month: "))

input_1 = float(input(" What are your expenses for this month: "))

expenses = 0


while input_1 > 0:
    expenses = expenses + input_1
    input_1 = float(input(" What are your expenses for this month: "))
if budget > expenses:
    print(" Good job, you have extract money !")
elif budget == expenses:
    print(" Perfect ! You had just enough money!")
else:
    print(" I am sorry, you do not have enough money.")
    
    
