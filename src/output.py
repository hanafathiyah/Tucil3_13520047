from reachablechecker import less_than, sum_of_less_than_plus_x, is_reachable

def print_all_values_of_less_than(fifteen_puzzle):
    for i in range(1,17):
        print(i, less_than(i,fifteen_puzzle))

def print_matrix(fifteen_puzzle):
    for i in range(4):
        for j in range(4):
            print(fifteen_puzzle[i][j], end = " ")
        print("")

def game_output(fifteen_puzzle):
    print_matrix(fifteen_puzzle)
    print_all_values_of_less_than(fifteen_puzzle)
    print(sum_of_less_than_plus_x(fifteen_puzzle))
    if (not is_reachable(fifteen_puzzle)):
        print("Unfortunately, you cannot reach the reachable value")