from asyncio.windows_events import NULL
import imp
from operator import rshift
from re import U
from turtle import left, right
from unittest import result
from node import LiveNode
from nodepuzzle import NodePuzzle
from utility import copy_matrix, is_lower_than, matrix_to_list, print_matrix, is_a_result
from movematrix import is_enable_to_move_left, is_enable_to_move_right, is_enable_to_move_up, is_enable_to_move_up, is_enable_to_move_down, move_left, move_right, move_up, move_down

def count_g(fifteen_puzzle):
    cnt = 0
    for i in range(16):
        if(matrix_to_list(fifteen_puzzle)[i] != i+1 and matrix_to_list(fifteen_puzzle)[i] != 16):
            cnt += 1
    return cnt

def print_bnb(current_node_analyze, all_node):
    while(current_node_analyze.parent != None):
        print_matrix(current_node_analyze.info)
        current_node_analyze = all_node[current_node_analyze.parent]

def procedure_bnb(fifteen_puzzle):
    initial_node = NodePuzzle(fifteen_puzzle)
    cnt_node = 1 
    g_function = count_g(initial_node)
    
    live_node = LiveNode(is_lower_than)

    solution = None

    live_node.add_in(initial_node)

    while(not live_node.is_empty()):
        current_node = live_node.get_first()
        live_node.delete_first()

        if(is_a_result(current_node.info)):
            solution = current_node
            break