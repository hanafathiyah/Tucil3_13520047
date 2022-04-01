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

def less_than(number, fifteen_puzzle):
    cnt = 0
    for i in range(get_position_of_number(number,fifteen_puzzle) + 1, 16):
        if matrix_to_list(fifteen_puzzle)[i] < number:
            cnt += 1
    return cnt

def sum_of_less_than(fiften_puzzle):
    sum = 0
    for i in range(1, 17):
        sum += less_than(i, fiften_puzzle)
    return sum

def print_all_values_of_less_than(fifteen_puzzle):
    for i in range(1,17):
        print(i, less_than(i,fifteen_puzzle))

def print_matrix(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            print(fifteen_puzzle[i][j], end = " ")
        print("")

def procedure_bnb(fifteen_puzzle):
    print_matrix(fifteen_puzzle)
    print_all_values_of_less_than(fifteen_puzzle)
    print(sum_of_less_than(fifteen_puzzle) + x_value(fifteen_puzzle))
    if (sum_of_less_than(fifteen_puzzle) + x_value(fifteen_puzzle)) % 2 != 0:
        print("Unfortunately, you cannot reach the reachable value")