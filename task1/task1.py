l = input().split()
n = int(l[0])
m = int(l[1])
l = list(range(n + 1))[1:]
for i in range(len(l)):
    l[i] = str(l[i])
s = ''.join(l[:m])
while s[0] != s[-1]:
    for i in range(m - 1):
        l.append(l[0])
        l.pop(0)
    s += ''.join(l[:m])
print(s[::m])
