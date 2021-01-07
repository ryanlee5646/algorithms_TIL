from collections import namedtuple

# 파이썬에는 구조체가 없을 뿐더러 클래스 또한 데이터 타입을 지정할 수 없어, 구조체와 같은 형태를 정의하려면 네임드 튜플(namedtuple)을 사용해야한다.
MyStruct = namedtuple("MyStruct", "field1 field2 field3")

m = MyStruct("foo", "bar", "baz")



''' 파이썬 3.7부터 dataclass를 지원하며, @dataclass 데코레이션(자바에서는 동일한 문법을 어노테이션(Annotation)이라 부른다)으로 타입 힌트와 함께 
    활용함으로써 class를 이용해 구조체 형태로 정의할 수 있다.
'''

# 파이썬(Python) 3.7+
from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10

print(apple.price)