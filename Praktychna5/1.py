'''
Масив А містить довільні цілі цисла. Всі елементи масиву А
переписати в масиви В та С використовуючи таке правило: вибрати
з масиву А два максимально наближених значення, менше з них
записати в масив В а більше в масив С.
Вивести на екран значення з масивів В та С
'''
def one_step(s):
    modul = lambda x: x if x > 0 else -1 * x
    m_i , m_j = 0, 1
    m = modul(s[1] - s[0])
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if modul(s[i]-s[j]) < m:
                m = modul(s[i]-s[j])
                m_i, m_j = i, j
    return s.pop(m_i), s.pop(m_j-1)

def m_max(s):
    m = s[0]
    for i in s:
        if i > m:
            m = i
    s.pop(s.index(m))

'''
Якщо у вхідному масиві непарна кількість 
значень, то перед початком основного циклу
викидуєм максимальне значення.
'''

a = [30,2,18,56,3,6,8,2,7,8,9,10,0]
if len(a) % 2 > 0:
    m_max(a)
b=[]
c=[]
val1,val2=0,0

while len(a)>1:
    val1, val2 = one_step(a)
    if val2 > val1:
        b.append(val1)
        c.append(val2)
    else:
        b.append(val2)
        c.append(val1)
print(b)
print(c)