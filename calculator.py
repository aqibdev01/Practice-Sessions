print("Welcome to Calculator")

def sum(s1,s2):
    print(s1+s2)

def difference(d1,d2):
    print(d1-d2)

def multiplication(m1,m2):
    print(m1*m2)

def division(v1,v2):
    print(v1/v2)

def check_operation(opt, opd1, opd2):
    if opt=='+':
        sum(opd1,opd2)
    elif opt=='-':
        difference(opd1,opd2)
    elif opt=='*':
        multiplication(opd1, opd2)
    elif opt=='/':
        division(opd1,opd2)

def starts():
    opd1 = int(input("Enter first value: "))
    opd2 = int(input("Enter second value: "))

    opt = str(input("Which operation you want to perform? (+,-,*,/) "))

    result = check_operation(opt, opd1, opd2)

    x = input("Do you want to perform another operation on resultant? (y/n) ")
    if x.lower() == 'y':
        opt = input("Which operation you want to perform? (+,-,*,/) ")
        opd1 = int(input("Enter the value: "))
        check_operation(opt, result, opd1)
    else:
        print("Good Bye")

starts()