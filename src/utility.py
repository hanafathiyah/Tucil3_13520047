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

def get_element_from_position(i,j,fifteen_puzzle):
    return fifteen_puzzle[i][j]

def set_element_in_position(i,j,fifteen_puzzle,el):
    fifteen_puzzle[i][j] = el

def get_empty_cell_idx(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            if fifteen_puzzle[i][j] == 16:
                return i,j

def print_matrix(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            print(fifteen_puzzle[i][j], end = " ")
        print("")