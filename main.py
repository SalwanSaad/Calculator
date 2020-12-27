print('Hi please enter the first number and the second number and then choose the mathematical process(- ,+ ,* ,/)\n')

try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    process = input("Mathematical process: ")

    if process == '-':
        sub = num1-num2
        print(f'{num1} - {num2} = {sub}')

    elif process == '+':
        sub = num1+num2
        print(f'{num1} + {num2} = {sub}')

    elif process == '/':
        sub = num1/num2
        print(f'{num1} / {num2} = {sub}')

    elif process == '*':
        sub = num1*num2
        print(f'{num1} * {num2} = {sub}')

    else:
        print('Please use the following (- ,+ ,* ,/)')

except ZeroDivisionError:
    print('You can not divide the number by zero')

except ValueError:
    print('Please enter a number')