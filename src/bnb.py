from asyncio.windows_events import NULL
import imp
from operator import rshift
from re import U
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

def insert_into_simpul_hidup(node, simpul_hidup):
    for i in range(len(simpul_hidup)):
        if simpul_hidup[i].c <= node.c:
            continue
        else:
            simpul_hidup.insert(i,node)
            break

def print_bnb(current_node_analyze, all_node):
    while(current_node_analyze.parent != None):
        print_matrix(current_node_analyze.info)
        current_node_analyze = all_node[current_node_analyze.parent]

def procedure_bnb(fifteen_puzzle):
        node_number = 0
        all_node = []
        simpul_e = []
        simpul_hidup = []
        all_node.append(NodePuzzle(node_number, fifteen_puzzle, None, 0))
        simpul_hidup.append(NodePuzzle(node_number, fifteen_puzzle, None, 0))
        simpul_e.append(simpul_hidup[0])
        current_node_analyze = simpul_e[len(simpul_e)-1]
        while (not is_a_result(current_node_analyze.info)):
            simpul_hidup.remove(simpul_hidup[0])
            if(is_enable_to_move_up(current_node_analyze.info)):
                node_number += 1
                up_node = NodePuzzle(node_number, copy_matrix(move_up(current_node_analyze.info)),current_node_analyze.node_number,current_node_analyze.depth+1)
                all_node.append(up_node)
                insert_into_simpul_hidup(up_node, simpul_hidup)
            if(is_enable_to_move_right(current_node_analyze.info)):
                node_number += 1
                right_node = NodePuzzle(node_number, copy_matrix(move_right(current_node_analyze.info)),current_node_analyze.node_number,current_node_analyze.depth+1)
                all_node.append(right_node)
                insert_into_simpul_hidup(right_node, simpul_hidup)
            if(is_enable_to_move_down(current_node_analyze.info)):
                node_number += 1
                down_node = NodePuzzle(node_number, copy_matrix(move_down(current_node_analyze.info)),current_node_analyze.node_number,current_node_analyze.depth+1)
                all_node.append(down_node)
                insert_into_simpul_hidup(right_node, simpul_hidup)
            if(is_enable_to_move_left(current_node_analyze.info)):
                node_number += 1
                left_node = NodePuzzle(node_number, copy_matrix(move_left(current_node_analyze.info)),current_node_analyze.node_number,current_node_analyze.depth+1)
                all_node.append(left_node)
                insert_into_simpul_hidup(left_node, simpul_hidup)
            simpul_e.append(simpul_hidup[0])
            current_node_analyze = simpul_e[len(simpul_e)-1]
        print_bnb(current_node_analyze, all_node)    



            
