t = int(input())
a = list(map(int, input().split()))
s = 0
for c in a:
    if c == t:
        s += 1
print(s)
