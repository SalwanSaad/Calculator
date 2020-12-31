import math


def options():
    try:
        process = input("Mathematical process: ")
        if len(process) > 1:
            num1 = int(input("First number: "))
        else:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))

        process2= process.upper()
        if process == '-':
            totall = num1 - num2
            print(f'{num1} - {num2} = {totall}')

        elif process == '+':
            totall = num1 + num2
            print(f'{num1} + {num2} = {totall}')

        elif process == '/':
            totall = num1 / num2
            print(f'{num1} / {num2} = {totall}')

        elif process == '*':
            totall = num1 * num2
            print(f'{num1} * {num2} = {totall}')

        elif process == '%':
            totall = num1 % num2
            print(f'{num1} % {num2} = {totall}')

        elif process2 == 'COS':
            totall = math.cos(num1)
            print(f'Cos({num1}) = {totall}')

        elif process2 == 'SIN':
            totall = math.sin(num1)
            print(f'Sin({num1}) = {totall}')

        elif process2 == 'TAN':
            totall = math.tan(num1)
            print(f'Tan({num1}) = {totall}')

        else:
            print('Please use the following (cos , sin , tan , + , - , * , /)')

    except ZeroDivisionError:
        print('You can not divide the number by zero')

    except ValueError:
        print('Please enter a number')
