import list
print('\n---Write (show) to show the available options---')

enter = ''
while enter != 'QUIT':
    select = input('>> ')
    select2 = select.upper()

    if select2 == 'SHOW':
        print(''' 
            O = To show the available mathematical operations
            Q = To quit   
            ''')

    elif select2 == 'O':
        print('you can use the following operators (cos , sin , tan , + , - , * , /)')
        list2 = list.options()
    elif select2 == 'Q':
        print('Thank you')
        break

