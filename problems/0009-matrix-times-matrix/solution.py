def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    if len(b) != len(a[0]):
        return -1

    result = []

    for a_row in range(len(a)):
        row = []
        for b_col in range(len(b[0])):
            element = 0
            for a_col in range(len(a[a_row])):
                element += a[a_row][a_col] * b[a_col][b_col]
            row.append(element)
        result.append(row)

    return result
