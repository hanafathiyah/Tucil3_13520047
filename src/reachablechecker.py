from numpy import true_divide
from utility import matrix_to_list, get_position_of_number

def get_empty_cell_idx(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            if fifteen_puzzle[i][j] == 16:
                return i,j

# find x value
def x_value(fifteen_puzzle):
    if((get_empty_cell_idx(fifteen_puzzle)[0] + get_empty_cell_idx(fifteen_puzzle)[1]) % 2 == 0):
        return 0
    else:
        return 1

def less_than(number, fifteen_puzzle):
    cnt = 0
    for i in range(get_position_of_number(number,fifteen_puzzle) + 1, 16):
        if matrix_to_list(fifteen_puzzle)[i] < number:
            cnt += 1
    return cnt

def sum_of_less_than(fifteen_puzzle):
    sum = 0
    for i in range(1, 17):
        sum += less_than(i, fifteen_puzzle)
    return sum

def sum_of_less_than_plus_x(fifteen_puzzle):
    return sum_of_less_than(fifteen_puzzle) + x_value(fifteen_puzzle)

def is_reachable(fifteen_puzzle):
    if(sum_of_less_than_plus_x(fifteen_puzzle) % 2 == 0):
        return True
    else:
        return False