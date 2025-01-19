print("Welcome to Calculator")

def sum(s1,s2):
    print(s1+s2)

def difference(d1,d2):
    print(d1-d2)

def multiplication(m1,m2):
    print(m1*m2)

def division(v1,v2):
    print(v1/v2)

# a1 = int(input("Enter the first number to add: "))
# a2 = int(input("Enter the second number to add: "))

# sum(a1,a2)


# b1 = int(input("Enter the first number to subtract: "))
# b2 = int(input("Enter the first number to subtract: "))

# difference(b1,b2)


# c1 = int(input("Enter the first number to multiply: "))
# c2 = int(input("Enter the first number to multiply: "))

# multiplication(c1,c2)

# d1 = int(input("Enter the first number to divide: "))
# d2 = int(input("Enter the first number to divide: "))

# division(d1,d2)

def check_operation(opt, opd1, opd2):
    if opt=='+':
        a = sum(opd1,opd2)
    elif opt=='-':
        a = difference(opd1,opd2)
    elif opt=='*':
        a = multiplication(opd1, opd2)
    elif opt=='/':
        a = division(opd1,opd2)

def starts():
    opd1 = input("Enter first value: ")
    opd2 = input("Enter second value: ")

    opt = input("Which operation you want to perform? (+,-,*,/) ")

    check_operation(opt, opd1, opd2)

    x = input("Do you want to perform another operation on resultant? (y/n) ")
    if x.lower() == 'y':
        opt = input("Which operation you want to perform? (+,-,*,/) ")
        opd1 = input("Enter the value: ")

starts()