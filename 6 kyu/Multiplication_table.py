def multiplication_table(size):
    return [[i * j for i in range(1, size + 1)] for j in range(1, size + 1)]


print(multiplication_table(3))
