def Calculator(a,operator,b):
    if(operator=='+'):
        return a+b
    if(operator=='-'):
        if(a>b):
            return a-b
        if(b>a):
            return b-a
    if(operator=='/'):
        return a/b
    if(operator=='*'):
        return a*b


x = int(input("enter your first number"))
op = eval(input("enter the operator"))
y = int(input("enter your second number"))

print(Calculator(x,op,y))

