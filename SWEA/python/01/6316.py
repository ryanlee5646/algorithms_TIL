# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
# 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는
# 프로그램을 작성하십시오.
a = list(range(1,11))
even = list(filter(lambda x: x%2==0,a))
mul = list(map(lambda x:x **2,even))
print(mul)