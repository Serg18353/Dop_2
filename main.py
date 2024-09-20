a = int(input(print('Введите число')))
print(a)
s = []
n = 1
m = 1
while a == int(a):
    if n + m != a:
        n += 1
    else:
        n + m == a
        s.append([n, m])
        m += 1
        n = 1

    if a // 2 < m:
        break
print(*s)
