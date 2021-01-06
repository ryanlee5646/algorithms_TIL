# ANCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

def ancii(a=int(input())):
    result = chr(a)
    return f'ANCII {a} => {result}'   
print(ancii())