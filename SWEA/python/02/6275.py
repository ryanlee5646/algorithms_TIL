# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
# 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b = 'aeiou'
for i in b:
    a = a.replace(i,'')
print(a)