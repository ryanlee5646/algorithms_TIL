# 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
# 입력: 12, 34, 56, 78  출력: [12, 34, 56, 78]
#                            (12, 34, 56, 78)

num = list(map(int, input().split(',')))
num_tuple = tuple(num)
print(f'{num}\n{num_tuple}' )