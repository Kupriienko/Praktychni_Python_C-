while True:
    print('Q to exit')
    print('Введіть вартість вашої покупки, більше 1000 для знижки: ')
    cost = input()
    if cost.upper() == 'Q':
        break
    try:
        float(cost)
    except:
        print("Ви ввели не коректні значення")
        continue
    if float(cost) > 1000:
        zn = float(cost) * 0.1
        n_cost = float(cost)-zn
        print("Через те що вартісь вашої покупки більше 1000, нова ціна вашої покупки " + str(n_cost) + " гривень")
    else:
        print("ціна вашої покупки " + str(cost) + " гривень")

