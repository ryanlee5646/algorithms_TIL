def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    zero = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:
            count += 1
    return rank[count + zero], rank[count]