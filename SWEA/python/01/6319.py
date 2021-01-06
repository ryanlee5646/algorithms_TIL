# 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# eye -> eye 입력하신 단어는 회문(Palindrome)입니다.

#1
def Palindrome (word=input()):
    result = ''
    for i in word[::-1]:
        result+=i
    if result == word:
        print(result)
    return '입력하신 단어는 회문(Palindrome)입니다.'
print(Palindrome())
#2
def Palindrome (word=input()):
    if word == word[::-1]:
        print(word)
    return  '입력하신 단어는 회문(Palindrome)입니다.'
print(Palindrome())

