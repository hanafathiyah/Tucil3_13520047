import utility

def move_up(fifteen_puzzle):
    fp_move = utility.copy_matrix(fifteen_puzzle)
    origin_i = utility.get_empty_cell_idx(fp_move)[0]
    origin_j = utility.get_empty_cell_idx(fp_move)[1]
    result_i = origin_i - 1 # move up = i - 1
    result_j = origin_j 
    tmp = utility.get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    utility.set_element_in_position(origin_i, origin_j, fp_move, utility.get_element_from_position(result_i,result_j,fp_move))
    utility.set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_down(fifteen_puzzle):
    fp_move = utility.copy_matrix(fifteen_puzzle)
    origin_i = utility.get_empty_cell_idx(fp_move)[0]
    origin_j = utility.get_empty_cell_idx(fp_move)[1]
    result_i = origin_i + 1 # move down = i + 1
    result_j = origin_j 
    tmp = utility.get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    utility.set_element_in_position(origin_i, origin_j, fp_move, utility.get_element_from_position(result_i,result_j,fp_move))
    utility.set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_left(fifteen_puzzle):
    fp_move = utility.copy_matrix(fifteen_puzzle)
    origin_i = utility.get_empty_cell_idx(fp_move)[0]
    origin_j = utility.get_empty_cell_idx(fp_move)[1]
    result_i = origin_i
    result_j = origin_j - 1 # move left = j - 1 
    tmp = utility.get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    utility.set_element_in_position(origin_i, origin_j, fp_move, utility.get_element_from_position(result_i,result_j,fp_move))
    utility.set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def move_right(fifteen_puzzle):
    fp_move = utility.copy_matrix(fifteen_puzzle)
    origin_i = utility.get_empty_cell_idx(fp_move)[0]
    origin_j = utility.get_empty_cell_idx(fp_move)[1]
    result_i = origin_i
    result_j = origin_j + 1 # move right = j + 1 
    tmp = utility.get_element_from_position(origin_i,origin_j,fp_move)
    # swap
    utility.set_element_in_position(origin_i, origin_j, fp_move, utility.get_element_from_position(result_i,result_j,fp_move))
    utility.set_element_in_position(result_i, result_j, fp_move, tmp)
    return fp_move

def is_enable_to_move_up(fifteen_puzzle):
    return utility.get_empty_cell_idx(fifteen_puzzle)[0] > 0

def is_enable_to_move_down(fifteen_puzzle):
    return utility.get_empty_cell_idx(fifteen_puzzle)[0] < 3

def is_enable_to_move_right(fifteen_puzzle):
    return utility.get_empty_cell_idx(fifteen_puzzle)[1] < 3

def is_enable_to_move_left(fifteen_puzzle):
    return utility.get_empty_cell_idx(fifteen_puzzle)[0] > 0