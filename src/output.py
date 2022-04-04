import bnb
import reachablechecker
import utility

def print_all_values_of_less_than(fifteen_puzzle):
    print("i"+"    "+"lower-numbered(i)")
    for i in range(1,17):
        print(str(i)+"\t"+str(reachablechecker.less_than(i,fifteen_puzzle)))

def game_output(fifteen_puzzle):
    print("\n> Initial Arrangement:\n")
    utility.print_matrix(fifteen_puzzle) # 1st output in project specification
    print("")
    print("> The number of lower-numbered tiles that are to the right of tile i in the arrangement:\n")
    print_all_values_of_less_than(fifteen_puzzle) # 2nd output in project specification
    print("")
    print("> Sum of all lower-numbered(i) =", reachablechecker.sum_of_less_than(fifteen_puzzle))
    print("")
    print("> Value of X =", reachablechecker.x_value(fifteen_puzzle))
    print("")
    print("> Sum of all lower-numbered(i) after add by X = ",end = "")
    print(reachablechecker.sum_of_less_than_plus_x(fifteen_puzzle)) # 3rd output in project specification
    if (not reachablechecker.is_reachable(fifteen_puzzle)): # 4th output in project specification
        print("\n> Result: The goal state is not reachable from the initial state.\n")
        exit()
    else:
        print("\n> Result: The goal state is reachable from the initial state.\n")
        print("> Solution:\n")
        bnb.procedure_bnb(fifteen_puzzle)