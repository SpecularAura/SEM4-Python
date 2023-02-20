from arithmetic_op import *


def PerformOperations(a, b):
    print(f'{a} + {b}:', addop(a,b))
    print(f'{a} - {b}: { diffop(a,b)}')
    print(f'{a} ^ 2: { squareop(a)}')
    print(f'{a} % {b}: { moduloop(a, b)}')

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))
PerformOperations(a, b)