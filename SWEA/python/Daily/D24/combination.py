data = [1,2,3,4,5]
N = len(data)
combi = []
# 조합
for a in range(N):
    for b in range(N):
        if a < b:
            for c in range(N):
                if a < c and b < c:
                    combi.append([data[a],data[b],data[c]])
print(combi)

# 중복 조합
mul_combi = []
for a in range(N):
    for b in range(N):
        if a <= b:
            for c in range(N):
                if a <= c and b <= c:
                    mul_combi.append([data[a],data[b],data[c]])

print(mul_combi)

