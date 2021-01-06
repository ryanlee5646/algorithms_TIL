# "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

grade = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
total_score = list(set(map(lambda x: grade.count('A')*4 + grade.count('B')*3+ grade.count('C')*2 + grade.count('D') , grade  )))
print(total_score[0])