# Level1 크레인 인형뽑기

def solution(board, moves):
    doll = 0
    basket = []
    for move in moves:
        for y in range(len(board)):
            # 1 바구니에 2개 이상 인형이 있으면 끝에 인형 2개를 비교
            if len(basket) > 1:
                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    doll += 2
            # 2 해당 위치에 인형이 있으면 추가
            if board[y][move-1]:
                basket.append(board[y][move-1])
                # 3 뽑은 인형 위치는 0으로 초기화
                board[y][move-1] = 0
                break
    return doll