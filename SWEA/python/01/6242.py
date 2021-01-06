# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
blood_types = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {}
for blood_type in blood_types:
    if blood_type in result:
        result[blood_type] += 1
    else:
        result[blood_type] = 1
print(result)