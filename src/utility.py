from bnb import count_g

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

def copy_matrix(fifteen_puzzle):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = fifteen_puzzle[i][j]
    return result

def print_matrix(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            print(fifteen_puzzle[i][j], end = " ")
        print("")

def is_a_result(fifteen_puzzle):
    i = 0
    same = True
    while i < 16 and same:
        if(matrix_to_list(fifteen_puzzle)[i] != i+1):
            same = False
        else:
            i += 1
    return same

def is_lower_than(node_x, node_y):
    return node_x.depth + count_g(node_x.root) <= node_y.depth + count_g(node_y.root)
