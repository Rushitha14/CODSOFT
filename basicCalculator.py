def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

print("ENTER AN OPERATOR\n1.ADD(+)\n2.SUBTRACT(-)\n3.DIVISION(/)\n4.MULTIPLY(*)\n")

choice=int(input("Select operator for the above list(1,2,3,4)"))
n1=float(input("enter the value of n1"))
n2=float(input("enter the value of n2"))

if choice==1:
    result=add(n1,n2)
elif choice==2:
    result=subtract(n1,n2)
elif choice==3:
    result=divide(n1,n2)
elif choice==4:
    result=multiply(n1,n2)
else:
    result="Enter right choice(1-4)"

print("Result:", result)
