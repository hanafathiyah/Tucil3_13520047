import imp
import time
import utility
import node
import nodepuzzle
import movematrix

def count_g(fifteen_puzzle):
    cnt = 0
    for i in range(16):
        if(utility.matrix_to_list(fifteen_puzzle)[i] != i+1 and utility.matrix_to_list(fifteen_puzzle)[i] != 16):
            cnt += 1
    return cnt

def print_bnb(current_node_analyze, all_node):
    while(current_node_analyze.parent != None):
        utility.print_matrix(current_node_analyze.info)
        current_node_analyze = all_node[current_node_analyze.parent]

def opposite_node(move_direction):
    if (move_direction == 'left'):
        return 'right'
    if (move_direction == 'right'):
        return 'left'
    if (move_direction == 'up'):
        return 'down'
    if (move_direction == 'down'):
        return 'up'

def get_solution(solution_found):
    solution = []

    parent = solution_found.parent
    previous = solution_found

    while(parent != None):
        solution.insert(0,previous) # reverse add
        previous = parent
        parent = parent.parent     

    return solution

def procedure_bnb(fifteen_puzzle):

    initial_node = nodepuzzle.NodePuzzle(fifteen_puzzle)

    print("0: Initial Arrangement")
    utility.print_matrix(fifteen_puzzle)
    print()

    cnt_node = 1 

    live_node = node.LiveNode(utility.is_lower_than)

    solution = None

    live_node.add_in(initial_node)

    time_begin = time.process_time_ns()

    while(not live_node.is_empty()):
        current_node = live_node.get_first()
        live_node.delete_first()

        if(utility.is_a_result(current_node.info)):
            solution = current_node
            break

        # moving
        if (movematrix.is_enable_to_move_up(current_node.info) and current_node.move != 'down'):
            result_node = nodepuzzle.NodePuzzle(movematrix.move_up(current_node.info), parent=current_node,depth=current_node.depth+1,move='up')
            cnt_node += 1
            live_node.add_in(result_node)
        
        if (movematrix.is_enable_to_move_right(current_node.info) and current_node.move != 'left'):
            result_node = nodepuzzle.NodePuzzle(movematrix.move_right(current_node.info), parent=current_node,depth=current_node.depth+1,move='right')
            cnt_node += 1
            live_node.add_in(result_node)
        
        if (movematrix.is_enable_to_move_down(current_node.info) and current_node.move != 'up'):
            result_node = nodepuzzle.NodePuzzle(movematrix.move_down(current_node.info), parent=current_node,depth=current_node.depth+1,move='down')
            cnt_node += 1
            live_node.add_in(result_node)
        
        if (movematrix.is_enable_to_move_left(current_node.info) and current_node.move != 'right'):
            result_node = nodepuzzle.NodePuzzle(movematrix.move_left(current_node.info), parent=current_node,depth=current_node.depth+1,move='left')
            cnt_node += 1
            live_node.add_in(result_node)
    
    array_result = get_solution(solution)

    time_end = time.process_time_ns()

    for i in range(len(array_result)):
        print(str(i+1)+": Move "+"< "+str(array_result[i].move).title()+" >")
        utility.print_matrix(array_result[i].info)
        print()
    
    print("All moves:", end = " ")
    for i in range(len(array_result)):
        print(str(array_result[i].move).title()[0], end = " ")
    print()

    print("Total moves:", len(array_result))
    print("Time spent:",(time_end - time_begin)/10000000, "ms") # 6th output in project specification
    print("Total nodes:", cnt_node) # 7th output in project specification
    