'''
Скласти програму переведення дробового числа у грошовий
формат, наприклад 12,5 має записуватись як 12 грн. 50 коп
'''
def grn_kop(x, grnkop = 0):
    if x == '':
        return x
    n = grnkop if grnkop == 0 or grnkop == 1 else 0
    m = (('гривень', 'копійок'), ('гривня', 'копійка'), ('гривні', 'копійки'), ('гривень', 'копійок'))
    x_int = int(x[-2:])
    if x_int > 4 and x_int < 20:
        return m[0][n]
    elif x[-1] == '1':
        return m[1][n]
    elif int(x[-1]) > 1 and int(x[-1]) < 5:
        return m[2][n]
    else:
        return m[3][n]

def kop_convert(s):
    if s == '':
        return s
    if len(s) == 1:
        return s+'0'
    elif s[0] == '0':
        return s[1]
    else:
        return s

while True:
    print('Введіть дробове число. Q для виходу: ')
    x = input()
    if x.upper() == 'Q':
        break
    try:
        float(x) # Перевіряємо чи число
    except:
        print("Ви ввели не число")
        continue
    sp_x = x.split('.')
    if len(sp_x) == 2:
        print(sp_x[0] + ' ' + grn_kop(sp_x[0], 0) + ' ' + kop_convert(sp_x[1]) + ' ' + grn_kop(kop_convert(sp_x[1]),1))
    else:
        print(sp_x[0] + ' ' + grn_kop(sp_x[0], 0))
