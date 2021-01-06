

checker=[0]*5
def part(now_index):

    if now_index==5:
        print(checker)
        return

        checker[now_index]=0
        part(now_index+1)
        checker[now_index]=1
        part(now_index + 1)
part(0)
