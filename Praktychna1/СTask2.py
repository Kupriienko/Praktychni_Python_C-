"""
Записати мовою С++ (Я запишу мовою Python). Чому дорівнюють z1.z2 при b=2)
"""
while True:
    print('Введіть сторону квадрата. Q для виходу: ')
    s = input()
    if s.upper() == 'Q':
        break
    print('Введіть радіус кола. Q для виходу: ')
    r = input()
    if r.upper() == 'Q':
        break
    try:
        float(s)
        float(r)
    except:
        print("Ви ввели не коректні значення")
        continue
    sq_a = float(s)*float(s)
    circle_a = 3.14*float(r)**2
    print('Площа квадрата = %s, площа кола = %s' % (sq_a, circle_a))
    if sq_a > circle_a:
        print('Площа квадрата більша за площу кола')
    else:
        print('Площа кола більша за площу квадрата')