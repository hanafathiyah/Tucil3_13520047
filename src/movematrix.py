import imp
from utility import get_empty_cell_idx, get_element_from_position, set_element_in_position

def move_up(fifteen_puzzle):
    fp_move = fifteen_puzzle
    origin_i = get_empty_cell_idx(fp_move)[0]
    origin_j = get_empty_cell_idx(fp_move)[1]
    result_i = origin_i - 1 # move up = i - 1
    result_j = origin_j 
    tmp = get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    set_element_in_position(origin_i, origin_j, fp_move, get_element_from_position(result_i,result_j,fp_move))
    set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_down(fifteen_puzzle):
    fp_move = fifteen_puzzle
    origin_i = get_empty_cell_idx(fp_move)[0]
    origin_j = get_empty_cell_idx(fp_move)[1]
    result_i = origin_i + 1 # move down = i + 1
    result_j = origin_j 
    tmp = get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    set_element_in_position(origin_i, origin_j, fp_move, get_element_from_position(result_i,result_j,fp_move))
    set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_left(fifteen_puzzle):
    fp_move = fifteen_puzzle
    origin_i = get_empty_cell_idx(fp_move)[0]
    origin_j = get_empty_cell_idx(fp_move)[1]
    result_i = origin_i
    result_j = origin_j - 1 # move left = j - 1 
    tmp = get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    set_element_in_position(origin_i, origin_j, fp_move, get_element_from_position(result_i,result_j,fp_move))
    set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_right(fifteen_puzzle):
    fp_move = fifteen_puzzle
    origin_i = get_empty_cell_idx(fp_move)[0]
    origin_j = get_empty_cell_idx(fp_move)[1]
    result_i = origin_i
    result_j = origin_j + 1 # move right = j + 1 
    tmp = get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    set_element_in_position(origin_i, origin_j, fp_move, get_element_from_position(result_i,result_j,fp_move))
    set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

