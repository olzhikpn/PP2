def naoborot(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for a in naoborot(n):
    print(a)