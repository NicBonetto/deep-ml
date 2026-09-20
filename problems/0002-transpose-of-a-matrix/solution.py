def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    num_rows = len(a)
    num_columns = len(a[0])
    result = []

    for col in range(num_columns):
        new_row = []
        for row in range(num_rows):
            new_row.append(a[row][col])
        result.append(new_row)
    return result