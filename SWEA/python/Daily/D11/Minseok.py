import sys
sys.stdin = open("Minseok.txt", "r")

T = int(input())

for t in range(1, T+1):
    student, submit = map(int, input().split())
    submit_student = list(map(int, input().split()))
    student_num = [i for i in range(1, student+1)]
    not_submit = []
    for i in student_num:
        if i not in submit_student:
            not_submit.append(i)
    print('#{}'.format(t), end=' ')
    for j in not_submit:
        print(j, end=' ')
    print("")
