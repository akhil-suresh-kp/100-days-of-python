def calculator_project():
    num1 = int(input('Enter first number: '))
    switch = True
    while switch: 
        print('Operators: + - * /')
        op = input('Enter the operator: ')
        num2 = int(input('Enter the next number: '))
        result = 0
        if op == '+':
            result = num1 + num2
            print(f'{num1} {op} {num2} = {result}')
        elif op == '-':
            result = num1 - num2
            print(f'{num1} {op} {num2} = {result}')
        elif op == '*':
            result = num1 * num2
            print(f'{num1} {op} {num2} = {result}')
        elif op == '/':
            result = num1 / num2
            print(f'{num1} {op} {num2} = {result}')

        resume_opn = input(f'Type y to continue calculating with {result}, else type n to start a new operation: ')
        if resume_opn == 'y':
            num1 = result
            continue
        else:
            print('\n'*20)
            calculator_project()

calculator_project()