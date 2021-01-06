import sys
sys.stdin = open("elec_bus2.txt","r")

# 처음 출발점에서 끝까지 갓을때 횟수를 기본값으로 해주고
# 출발점에서 갈수있는 최대거리에서 뒤로 한칸씩 이동했을때 갈수있는 최대횟수랑 비교해줌(While문으로 재귀 사용)
# 가장 밖에 있는 재귀 함수는 최대 충전횟수만큼 인덱스를 추가해줌

def Back(here, remain, count):
    global low
    remain -= 1
    if here == N-1:
        if count <= low:
            low = count
        return
    if count > low:
        return
    if remain == 0:
        Back(here+1, charge[here], count+1)
        return
    if remain > charge[here]:
        Back(here+1,remain,count)
        return
    Back(here + 1, charge[here], count + 1) # 충전하기
    Back(here + 1, remain, count) # 충전안하고 가기

T = int(input())
for t in range(1, T + 1):
    charge = list(map(int, input().split()))  # 충전소
    N = charge.pop(0)  # 충전소 횟수 here이 N이되면 종료
    low = 987654321  # 충전 횟수
    Back(1, charge[0], 0)
    print("#{} {}".format(t,low))





























    #
    # remain -=1
    # global low
    # if here >= N-2:
    #     if count <= low:
    #         low = count
    #     return
    # if count >= low:
    #     return
    # if remain==0:
    #     Back(here + 1, charge[here], count + 1)
    #     return
    # if remain>=charge[here]:
    #     Back(here+1, remain, count)
    #     return
    # Back(here+1,charge[here],count+1)
    # Back(here+1, remain, count)
    #




