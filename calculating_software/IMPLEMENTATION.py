print("welcome to basic arithmetic calculator")
num_1=int(input("Enter the first number"))
operator=input("Enter the operator")
num_2=int(input("Enter the second number"))
if operator == "+" :   
   answer = num_1 + num_2
elif operator == "-" :
   answer= num_1 - num_2
elif operator == "*" :
    answer = num_1 * num_2
else:
    answer= num_1 / num_2
print("your answer is",answer)

