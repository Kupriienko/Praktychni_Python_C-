while True:
    print('Введіть рядок. Q для виходу: ')
    x = input()
    if x.upper() == 'Q':
        break
    x_rep = x.replace(' ', '')
    print('Рядок \" %s \" є паліндром' % x) if x_rep == x_rep[::-1] else print('Рядок \" %s \" не є паліндром' % x)