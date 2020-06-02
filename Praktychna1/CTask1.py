'''
Записати мовою С++. Чому дорівнюють z1.z2 при b=2
'''

import math
b = 2
z1 = math.sqrt(2*b+2*math.sqrt(b**2-4))/(math.sqrt(b**2-4)+b+2)
z2 = 2/math.sqrt(b+2)
print('z1 = %s, z2 = %s' % (z1, z2))
