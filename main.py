a = int(input(print('Введите число')))
print(a)
s = []
n = 1
m = 2
while a == int(a):
    if a % (n + m) == 0:
        s.append([n, m])
    if n + m < a:
        m += 1
    else:
        n += 1
        m = n + 1
    if a//2  == n - 1:
        break
print(*s)
