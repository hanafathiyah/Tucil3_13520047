import imp
from reachablechecker import less_than, sum_of_less_than_plus_x, is_reachable
from utility import print_matrix
from bnb import procedure_bnb

def print_all_values_of_less_than(fifteen_puzzle):
    print("i"+"\t"+"Kurang(i)")
    for i in range(1,17):
        print(str(i)+"\t"+str(less_than(i,fifteen_puzzle)))

def game_output(fifteen_puzzle):
    print("\nMatrix posisi awal 15-puzzle")
    print_matrix(fifteen_puzzle) # 1st output in project specification
    print("")
    print("Nilai dari fungsi Kurang(i)")
    print_all_values_of_less_than(fifteen_puzzle) # 2nd output in project specification
    print("")
    print("Nilai dari sigma(i = 1 to 16) Kurang(i) + X")
    print(sum_of_less_than_plus_x(fifteen_puzzle)) # 3rd output in project specification
    if (not is_reachable(fifteen_puzzle)): # 4th output in project specification
        print("Unfortunately, the puzzle is unsolvable. You cannot reach the final result")
        exit()
    else:
        procedure_bnb(fifteen_puzzle)