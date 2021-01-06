# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
# rsp = ["가위", "바위", "보"]
# man_1 = input()
# man_2 = input()
# if man_1 == rsp[0]:
#     if man_2 == rsp[1]:
#         print('Result: Man1 Lose!')
#     elif man_2 == rsp[2]:
#         print('Result: Man1 Win!')
#     else:
#         print('Result: Draw!')
# elif man_1 == rsp[1]:
#     if man_2 == rsp[2]:
#         print('Result: Man1 Lose!')
#     elif man_2 == rsp[0]:
#         print('Result: Man1 Win!')
#     else:
#         print('Result: Draw!')
# else :
#     if man_2 == rsp[0]:
#         print('Result: Man1 Lose!')
#     elif man_2 == rsp[1]:
#         print('Result: Man1 Win!')
#     else:
#         print('Result: Draw!')

# rsp = ["가위", "바위", "보"]


game = ["가위", "바위", "보"]

a = input()
b = input()

if (a == game[0] and b == game[2]) or (a == game[1] and b == game[0]) or (a == game[2] and b == game[1]):
    print("Result : Man1 win!")
else:
    print("Result : Man2 win!")