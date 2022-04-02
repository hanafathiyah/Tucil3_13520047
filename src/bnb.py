import imp
from turtle import left
from unittest import result
from utility import matrix_to_list, print_matrix
from movematrix import move_left, move_right, move_up, move_down

def count_g(fifteen_puzzle):
    cnt = 0
    for i in range(16):
        if(matrix_to_list(fifteen_puzzle)[i] != i+1 and matrix_to_list(fifteen_puzzle)[i] != 16):
            cnt += 1
        return cnt

def procedure_bnb(fifteen_puzzle):
    up = move_up(fifteen_puzzle)
    print_matrix(up)
    print()
    left = move_left(fifteen_puzzle)
    print_matrix(left)
    print()
    right = move_right(fifteen_puzzle)
    print_matrix(right)
    print()
    down = move_down(fifteen_puzzle)
    print_matrix(down)
    print("Hello World")
