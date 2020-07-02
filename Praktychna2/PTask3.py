'''
На сковорідку одночасно можна покласти k котлет. Кожну котлету
потрібно з кожного боку обсмажувати m хвилин безперервно. За
який найменший час вдасться підсмажити з обох сторін n котлет?
Вхідні дані:
Програма отримує на вході три числа: k, m и n.
Вихідні дані:
Програма повинна вивести на екран число: найменшу к-сть хвилин
'''


def min_time(k, m, n):
    m_t = (n / k) * (2 * m) if n % k == 0 else (n // k) * (2 * m) + 2 * m
    # / звичайне ділення, % залишок від ділення, // ціла частина від ділення
    print('За %s хвилин вдасться приготувати %s котлет' % (m_t, n))


k = int(input('Введіть к-сть котлет, які одночасно можна покласти на сковорідку: '))
m = int(input('Введіть к-сть хвилин, за які котлета має підсмажтись з одного боку: '))
n = int(input('Введіть к-сть котлет : '))
min_time(k, m, n)
