def Power1(a,b): #O(n)
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a*Power2(a, b-1)

def Power2(a, b): #O(logn)
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b & 1:
        return a*Power2(a, b-1)
    else:
        temp = Power2(a, b//2)
        return temp*temp

def Power3(a,b): #O(logn)
    ans = 1
    while b > 0:
        if b&1:
            ans*=a #b가 홀수이면
        a = a*a
        b//=2
    return ans

print(Power1(2,900))
print(Power2(2,20000))
print(Power3(2,20000))