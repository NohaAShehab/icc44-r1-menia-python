


# def askdivnums(num1, num2):
#     if num2 ==0:
#         raise  ValueError("cannot divide by zero")
#     print(f"{num1}/ {num2}= ", end=' ')
#     res = num1/num2
#     print(res)
#
#
#
# askdivnums(3,0)


def sumnums(num1: int, num2: int):
    if isinstance(num1, int )and isinstance(num2, int):
        return num1 + num2

    raise TypeError('num1 and num2 should be integers')


print(sumnums(3094,444.44))