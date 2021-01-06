#'42FB'를 숫자로
data = '42FB'
hex_1 = {
    'A' : 10, 'B' : 11, 'C' : 12, 
    'D': 13, 'E' : 14, 'F' : 15
    }
j = len(data)
result = 0
for i in (data):
    j -= 1
    if i.isdigit():
        result += int(i)*(16**j)
    else:
        result += hex_1[i] *(16**j)
print(result)

