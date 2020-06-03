import random
r_n = random.randint(1, 100)
t = input('Введіть кількість спроб менше 20: ')
try:
    i_f = int(t)
    if i_f > 20:
        i_f = random.randint(5, 20)
        t = str(i_f)
        print("Ви ввели забагато спроб, тепер у вас %s спроб" % t)
except:
    i_f = random.randint(5, 20)
    t = str(i_f)
    print("Ви ввели не коректне значення, тепер у вас %s спроб" % t)
x = input('Вгадайте число від 1 до 100, у вас %s спроб: ' % t)
try:
    i_x = int(x)
except:
    i_x = random.randint(1, 100)
    x = str(i_x)
    print("Ви ввели не коректне значення, ми замінемо це на " + x)
while True:
    if i_x != r_n:
        i_f -= 1
        if i_f == 0:
            print('Ви програли, це було число ' + str(r_n))
            break
        if i_x > r_n:
            x = input('Ви ввели забагато, у вас %s спроб: ' % i_f)
            try:
                i_x = int(x)
            except:
                i_x = random.randint(1, 100)
                x = str(i_x)
                print("Ви ввели не коректне значення, ми замінемо це на " + x)
        elif i_x < r_n:
            x = input('Ви ввели замало, у вас %s спроб: ' % i_f)
            try:
                i_x = int(x)
            except:
                i_x = random.randint(1, 100)
                x = str(i_x)
                print("Ви ввели не коректне значення, ми замінемо це на " + x)
    else:
        print('Ви перемогли, компютер загадав число ' + x)
        break
