# def GetSome(count):
#
#     if count == 0 : return
#     print(f'재귀 호출 {count}')
#     GetSome(count-1)
#
# GetSome(3)

def GetSome(count):

    if count == 0 : return
    GetSome(count-1)
    print(f'재귀 호출 {count}')

GetSome(3)