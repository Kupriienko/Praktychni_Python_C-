'''
Рахуємо гроші. До введеного числа додати напис гривень,
гривня, гривні; згідно з правилами української мови.
'''
while True:
    print('Введіть кільксть гривень. Q для закінчення: ')
    x = input()
    if x.upper() == 'Q':
        break
    try:
        int(x) # Перевіряємо чи число
        x_int = int(x[-2:]) # Аналізуємо дві останні цифри числа
    except:
        print("Ви ввели не число")
        continue
    if x_int > 4 and x_int < 20:
        print('Ваш ввід: %s гривень' % x)
    elif x[-1] == '1':
        print('Ваш ввід: %s гривня' % x)
    elif int(x[-1]) > 1 and int(x[-1]) < 5:
        print('Ваш ввід: %s гривні' % x)
    else:
        print('Ваш ввід: %s гривень' % x)
