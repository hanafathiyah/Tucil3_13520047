# change matrix of fifteen puzzle into one dimension list
def matrix_to_list(fifteen_puzzle):
    list_puzzle = [0 for i in range(16)]
    idx = 0
    for i in range(4):
        for j in range(4):
            list_puzzle[idx] = fifteen_puzzle[i][j]
            idx += 1
    return list_puzzle

def get_position_of_number(number,fifteen_puzzle):
    list_puzzle = matrix_to_list(fifteen_puzzle)
    for i in range(16):
        if (list_puzzle[i] == number):
            return i