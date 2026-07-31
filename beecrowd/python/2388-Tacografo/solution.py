intervalos = int(input())
dist = 0
for i in range(intervalos):
    temp, velo = map(int,input().split())
    dist += velo*temp
print(dist)
