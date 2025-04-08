from testhelper import test

def is_square_magic(square):
    n = len(square)
    if any(len(row) != n for row in square):
        return False
    
    magic_sum = sum(square[0])

    for i in range(n):
        if sum(square[i]) != magic_sum or sum(square[j][i] for j in range(n)) != magic_sum:
            return False

    if sum(square[i][i] for i in range(n)) != magic_sum or sum(square[i][n-1-i] for i in range(n)) != magic_sum:
        return False

    return True

valid_square = [[4, 9, 2], 
                [3, 5, 7], 
                [8, 1, 6]]

invalid_square = [[4, 9, 2], 
                  [8, 1, 6],
                  [3, 5, 7]]

test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))