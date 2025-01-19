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
    opd1 = int(input("Enter first value: "))
    opd2 = int(input("Enter second value: "))

    opt = input("Which operation you want to perform? (+,-,*,/) ")
    result = check_operation(opt, opd1, opd2)

    
    if type(result) is int:
        x = input("Do you want to perform another operation on resultant? (y/n) ")
        if x.lower() == 'y':
            opt = input("Which operation you want to perform? (+,-,*,/) ")
            opd1 = int(input("Enter the value: "))
            result = check_operation(opt, result, opd1)

            x = input("Do you want to perform another calculation? (y/n) ")
            if x.lower() == 'y':
                starts()
            else:
                print("Good Bye")
        
        else:
            x = input("Do you want to perform another calculation? (y/n) ")
            if x.lower() == 'y':
                starts()
            else:
                print("Good Bye")
        
    else:
        print("Resultant was infinite you can perform second operation on it")
        x = input("Do you want to perform another calculation? (y/n) ")
        if x.lower() == 'y':
            starts()
        else:
            print("Good Bye")

starts()
