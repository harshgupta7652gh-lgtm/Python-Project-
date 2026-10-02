a=float(input("enter the no.: "))
op=input("enter the operator: ")
b=float(input("enter the no.: "))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b!=0:
        print(a/b)
    else:
        print("result is undefined")
elif op=="%":
    print(a%b)
elif op=="**":
    print(a**b)
else:
    print("invalid operator")

    
