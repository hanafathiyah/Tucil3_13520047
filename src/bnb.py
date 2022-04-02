import imp
from unittest import result
from utility import get_element_from_position, get_empty_cell_idx, matrix_to_list, set_element_in_position, print_matrix
from movematrix import move_up

def count_g(fifteen_puzzle):
    cnt = 0
    for i in range(16):
        if(matrix_to_list(fifteen_puzzle)[i] != i+1 and matrix_to_list(fifteen_puzzle)[i] != 16):
            cnt += 1
        return cnt

def procedure_bnb(fifteen_puzzle):
    result = move_up(fifteen_puzzle)
    print_matrix(result)
    print("Hello World")
