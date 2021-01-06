Data = 123

def GetSome(n,k):
    if n < k:
        print(n, end ='')
        return
    else:
        GetSome(n//k,k)
        print(n%k, end='')

GetSome(3,2)