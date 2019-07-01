#input two numbers and peform the arithmetic operations:-
#Addition
#Subtraction
#Multiplication
#Division
num1=int(input("Enter the 1st no.: "))
num2=int(input("Enter the 2nd no.: "))
print("\n")

#addition
print("add =",num1+num2,"\n")

#Subtraction
print("sub = ",num1-num2,"\n")

#multiplication
print("mul = ",num1*num2,"\n")

#Division
if num2!=0:
    print("###In float format###")
    print("\tdiv = ", num1/num2,"\n")
    print("###In integer format###")
    print("\tquotient = ", int(num1/num2))
    print("\tremainder = ", num1%num2)
else:
    print("***invalid syntax***")


