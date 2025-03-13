def complex_function_1(data):
    def helper(x):
        return (x * 2) + 3
    return [helper(x) for x in data if x % 2 == 0]

def complex_function_2(matrix):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in matrix]

def complex_function_3(n):
    return (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda k, a=1, b=1: a if k == 0 else f(k - 1, b, a + b))(n)
