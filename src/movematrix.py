import imp
from utility import get_empty_cell_idx, get_element_from_position, set_element_in_position
def move_up(fifteen_puzzle):
    fp_move_up = fifteen_puzzle
    origin_i = get_empty_cell_idx(fp_move_up)[0]
    origin_j = get_empty_cell_idx(fp_move_up)[1]
    result_i = origin_i - 1 # move up = i - 1
    result_j = origin_j 
    tmp = get_element_from_position(origin_i,origin_j,fp_move_up)
    # swap
    set_element_in_position(origin_i, origin_j, fp_move_up, get_element_from_position(result_i,result_j,fp_move_up))
    set_element_in_position(result_i, result_j, fp_move_up, tmp)
    return fp_move_up