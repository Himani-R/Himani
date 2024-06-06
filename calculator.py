num1 = int(input("enter the value: "))
num2= int(input("enter the value: "))
opr=input("enter the op..")   #operator check krega ki kya h 
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)

elif opr=="*":
    print(num1*num2)
elif opr=="%":
    print(num1%num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operation")