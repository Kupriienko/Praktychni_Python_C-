import random
def Vvid (mess):
    x_local = input(mess)
    try:
        i_x_local = int(x_local)
        return i_x_local
    except:
        i_x_local = random.randint(1, 100)
        print("Ви ввели не коректне значення, ми замінемо це на " + i_x_local)
        return i_x_local

r_n = random.randint(1, 100)
t = input('Введіть кількість спроб менше 20: ')
try:
    i_f = int(t)
    if i_f > 20: raise NameError ('Too mach')
except:
    i_f = random.randint(5, 20)
    t = str(i_f)
    print("Ви ввели не коректне значення, тепер у вас %s спроб" % t)

i_x = Vvid('Вгадайте число від 1 до 100, у вас ' + t +' спроб: ')
while True:
    if i_x != r_n:
        i_f -= 1
        if i_f == 0:
            print('Ви програли, це було число ' + str(r_n))
            break
        if i_x > r_n:
            i_x = Vvid('Ви ввели забагато, у вас '+ str(i_f) + ' спроб: ')
        elif i_x < r_n:
            i_x = Vvid('Ви ввели замало, у вас ' + str(i_f) + ' спроб: ')
    else:
        print('Ви перемогли, компютер загадав число ' + str(r_n))
        break
