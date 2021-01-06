# def calc_sum(precision, *params):
#     if precision == 0:
#         total = 0
#     elif  0 < precision < 1:
#         total = 0.0

#     for val in params:
#         total += val
#     return total

# ret_val = calc_sum(0.1, 1, 2)
# print("calc_sum(0.1, 1, 2) 함수가 반환한 값: {0}".format(ret_val))

# def use_keyword_arg_unpacking(**params):
#     for k in params.keys():
#         print("{0}: {1}".format(k, params[k]))

# print("use_keyword_arg_unpacking()의 호출")
# use_keyword_arg_unpacking(a=1, b=2, c=3)

# def test_scope(a):
#     result = a + 1
#     print("\n\ttest_scope() 안에서의 a의 값: {0}".format(a))
#     print("\ttest_scope() 안에서의 result의 값: {0}\n".format(result))
#     return result

# x=5
# print("test_scope() 호출 전 x의 값: {0}".format(x))
# ret_val = test_scope(x)
# print("test_scope() 함수가 반환한 값: {0}".format(ret_val))
# print("test_scope() 호출 후 x의 값: {0}".format(x))

# def change_global_var():
#     global x
#     x += 1

# x = 5
# change_global_var()
# print("전역변수 x의 값: {0}".format(x))

# def calc(operator_fn, x, y):
#     return operator_fn(x, y)

# def plus(op1, op2):
#     return op1 + op2

# def minus(op1, op2):
#     return op1 - op2

# ret_val = calc(plus, 10, 5)
# print("calc(plus, 10, 5)의 결과 값: {0}".format(ret_val))

# ret_val = calc(minus, 10, 5)
# print(f"calc(minus, 10, 5)의 결과 값: {ret_val}")

# def calc(operator_fn, x, y):
#     return operator_fn(x, y)

# ret_val = calc(lambda a, b: a+b, 10, 5)
# print(f"calc(lambda a, b: a+b, 10, 5)의 결과 값: {ret_val}")

# ret_val = calc(lambda a, b: a - b, 10, 5)
# print(f"calc(lambda a, b: a -b, 10, 5)의 결과 값: {ret_val}")

def outer_func():
    id = 0

    def inner_func():
        nonlocal id
        id += 1
        return id
    return inner_func

make_id = outer_func()
print(f"make_id() 호출의 결과: {make_id()}")
print(f"make_id() 호출의 결과: {make_id()}")
print(f"make_id() 호출의 결과: {make_id()}")