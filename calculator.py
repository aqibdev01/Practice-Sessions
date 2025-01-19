print("Welcome to Calculator")

def sum(s1,s2):
    print(s1+s2)
    return s1+s2

def difference(d1,d2):
    print(d1-d2)
    return d1-d2

def multiplication(m1,m2):
    print(m1*m2)
    return m1*m2

def division(v1,v2):
    try:
        print(v1/v2)
        return v1/v2
    except ArithmeticError:
        print("Can't divide with zero!")

def check_operation(opt, opd1, opd2):
    if opt=='+':
        return sum(opd1,opd2)
    elif opt=='-':
        return difference(opd1,opd2)
    elif opt=='*':
        return multiplication(opd1, opd2)
    elif opt=='/':
        return division(opd1,opd2)

def starts():

    try:
        opd1 = int(input("Enter first value: "))
        opt = input("Which operation you want to perform? (+,-,*,/) ")
        opd2 = int(input("Enter second value: "))

        result1 = check_operation(opt, opd1, opd2)
        
        x1 = input("Do you want to perform another operation on resultant? (y/n) ")
        if x1.lower() == 'y':
            opd3 = int(input("Enter the value: "))
            opt = input("Which operation you want to perform? (+,-,*,/) ")
            check_operation(opt, result1, opd3)
        else:
            print("Good Bye")
    except ZeroDivisionError:
        print("Can not divide by zero")
    except ValueError:
        print("Enter a valid number")
        

    x2 = input("Do you want to perform new operations? (y/n) ")
    if x2 == 'y':
        starts()
    else:
        print("Good Bye")


starts()
