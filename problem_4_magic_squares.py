from testhelper import test

def is_square_magic(square):
    magic_sum = sum(square[0])
    
    for i in range(3):
        if sum(square[i]) != magic_sum or sum(square[j][i] for j in range(3)) != magic_sum:
            return False
    
    if sum(square[i][i] for i in range(3)) != magic_sum or sum(square[i][2-i] for i in range(3)) != magic_sum:
        return False
    
    return True

def create_magic_square():
    return [[4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]]

valid_square = create_magic_square()
invalid_square = [[4, 9, 2], 
                  [8, 1, 6],
                  [3, 5, 7]]

test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))

row_sums = [sum(row) for row in valid_square]
col_sums = [sum(valid_square[i][j] for i in range(3)) for j in range(3)]
print("Row sums:", row_sums)
print("Column sums:", col_sums)