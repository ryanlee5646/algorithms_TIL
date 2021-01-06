import random

name = ['장지수', '국은영', '이재혁', '이새봄']
place = ['대학부 앞', '대학부 뒤', '북카페 왼쪽', '북카페 오른쪽']

random.shuffle(place)

for i in zip(name,place):
    print(i)

