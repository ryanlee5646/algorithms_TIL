import sys
sys.stdin = open("diamond.txt", "r")

T = int(input())

for t in range(T):
    word = input()
    line1 = "..#."
    line2 = ".#.#"
    line3 = "#."

    for i in range(len(word)):
        print(line1, end="")
    print('.')
    for i in range(len(word)):
        print(line2, end="")
    print('.')
    for i in word:
        print("{}{}.".format(line3,i), end="")
    print('#')
    for i in range(len(word)):
        print(line2, end="")
    print('.')
    for i in range(len(word)):
        print(line1, end="")
    print('.')

