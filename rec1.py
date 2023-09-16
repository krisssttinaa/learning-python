
def binomial(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return binomial(n - 1, k) + binomial(n - 1, k - 1)


# print(binomial(4, 2))


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

##i = 0
##while True:
##    print(i, fibonacci(i))
##    i = i + 1

def product_recursionless(l):
    prod = 1
    for x in l:
        prod = prod * x
    return prod


def product_version1(l):
    if len(l) == 1:
        return l[0]
    return l[0] * product(l[1:])

def product(l):
    if len(l) == 0:
        return 1
    return l[0] * product(l[1:])


# print(product([2, 5, 6, 3, 34]))

def smallest_index(l):
    smallest = 0
    for i in range(1, len(l)):
        if l[i] < l[smallest]:
            smallest = i
    return smallest


def sortit(l):
    if len(l) == 0:
        return []
    small = smallest_index(l)
    return [l[small]] + sortit(l[:small] + l[small + 1:])


print(sortit([11, -3, 0, 2, 5, 6, 3, 34]))



























