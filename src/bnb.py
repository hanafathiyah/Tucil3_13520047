import imp
from operator import rshift
from turtle import left, right
from unittest import result
from nodepuzzle import NodePuzzle
from utility import copy_matrix, matrix_to_list, print_matrix, is_a_result
from movematrix import is_enable_to_move_left, is_enable_to_move_right, is_enable_to_move_up, is_enable_to_move_up, is_enable_to_move_down, move_left, move_right, move_up, move_down

def count_g(fifteen_puzzle):
    cnt = 0
    for i in range(16):
        if(matrix_to_list(fifteen_puzzle)[i] != i+1 and matrix_to_list(fifteen_puzzle)[i] != 16):
            cnt += 1
    return cnt

def procedure_bnb(fifteen_puzzle):
    simpul_expand = []
    initial_node = NodePuzzle(fifteen_puzzle, count_g(fifteen_puzzle), 1)
    simpul_expand.append(initial_node)
    simpul_hidup = []
    number = 1
    #depth = 0
    while not is_a_result(simpul_expand[len(simpul_expand)-1]):
        if is_enable_to_move_up(simpul_expand[len(simpul_expand)-1]):
            up = copy_matrix(move_right(fifteen_puzzle))   
            up_node = NodePuzzle(up, count_g(up))        
        if is_enable_to_move_right(simpul_expand[len(simpul_expand)-1]):
            right = copy_matrix(move_right(fifteen_puzzle))     
        if is_enable_to_move_down(simpul_expand[len(simpul_expand)-1]):
            right = copy_matrix(move_down(fifteen_puzzle))        
        if is_enable_to_move_left(simpul_expand[len(simpul_expand)-1]):
            left = copy_matrix(move_left(fifteen_puzzle))         
  
        simpul_expand.append(simpul_hidup[0])