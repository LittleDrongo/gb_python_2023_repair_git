
def print_operation_table(operation, rows, cols):
    table = [[1] * (cols) for _ in range(rows)]
    
    for i in range(1, rows):
        table[i][0] = i + 1
    for j in range(1, cols):
        table[0][j] = j + 1

    for i in range(1, rows):
        for j in range(1, cols):
            table[i][j] = operation(table[i][0], table[0][j])

    for row in table:
        print(' '.join(map(str, row)))
