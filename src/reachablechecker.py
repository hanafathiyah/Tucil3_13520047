import utility

# find x value
def x_value(fifteen_puzzle): # count x_value
    if((utility.get_empty_cell_idx(fifteen_puzzle)[0] + utility.get_empty_cell_idx(fifteen_puzzle)[1]) % 2 == 0): # even
        return 0 
    else: # odd
        return 1 

def less_than(number, fifteen_puzzle): # count lower-numbered tiles
    cnt = 0
    for i in range(utility.get_position_of_number(number,fifteen_puzzle) + 1, 16):
        if utility.matrix_to_list(fifteen_puzzle)[i] < number:
            cnt += 1
    return cnt

def sum_of_less_than(fifteen_puzzle): # count sum of lower-numbered tiles
    sum = 0
    for i in range(1, 17):
        sum += less_than(i, fifteen_puzzle)
    return sum

def sum_of_less_than_plus_x(fifteen_puzzle): # count sum of lower-numbered tiles + X
    return sum_of_less_than(fifteen_puzzle) + x_value(fifteen_puzzle)

def is_reachable(fifteen_puzzle): # check reachable
    if(sum_of_less_than_plus_x(fifteen_puzzle) % 2 == 0):
        return True
    else:
        return False