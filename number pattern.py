def generate_pattern(n):
    base_list = list(range(1, n+1))
    matrix = []

    for i in range(n):
        shifted_list = base_list[-i:] + base_list[:-i]
        matrix.append(shifted_list)

    for row in range(n):
        for col in range(n):
            print(matrix[col][row], end=' ')
        print()

generate_pattern(5)

