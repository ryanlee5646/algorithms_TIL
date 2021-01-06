# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

T = int(input())

for t in range(T):
    card_num = []
    card_count = []
    Count = [0] * 10
    N = input() #카드 수
    card_list = list(map(int, list(str(input()))))

    for card in card_list:
        Count[card] += 1
    card_count.append(max(Count)) # 카드숫자의 개수중 가장 큰 개수를 빈리스트에 추가
    for num, count in enumerate(Count):
        if count == max(Count): # 가장 많은 개수를 가진 카드숫자 빈리스트에 추가
            card_num.append(num)
    print(f"#{t+1} {max(card_num)} {card_count[0]} ") # 카드숫자중 큰 걸 출력
