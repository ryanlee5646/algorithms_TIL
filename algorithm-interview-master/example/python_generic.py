from typing import TypeVar

# 파이썬 제네릭(Genereic)
T = TypeVar('T')
U = TypeVar('U')

def are_equal(a:T, b:U):
    print(type(a))
    return a == b
are_equal(10, 10.0)
# print(are_equal(10, 10.0))



