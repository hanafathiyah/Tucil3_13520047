import convertfile
import readfile
import output
import os

def main():
    os.system("cls")
    print("Welcome to The 15-Puzzle Game\n")
    fifteen_puzzle_file_name = input("Input the 15-Puzzle's game file: ")
    fifteen_puzzle_in_file = readfile.read_file(fifteen_puzzle_file_name)

    if(fifteen_puzzle_in_file == []):
        exit()

    fifteen_puzzle = convertfile.convert_file_to_int_matrix(fifteen_puzzle_in_file)
    output.game_output(fifteen_puzzle)