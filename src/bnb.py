def get_empty_cell_idx(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            if fifteen_puzzle[i][j] == 16:
                return i,j

def x_value(fifteen_puzzle):
    if((get_empty_cell_idx(fifteen_puzzle)[0] + get_empty_cell_idx(fifteen_puzzle)[1]) % 2 == 0):
        return 0
    else:
        return 1

def procedure_bnb(fifteen_puzzle):
    print(x_value(fifteen_puzzle))