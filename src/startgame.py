import imp
from convertfile import convert_file_to_int_matrix
from readfile import read_file

def main():
    print("Welcome to 15-Puzzle Game")
    fifteen_puzzle_file_name = input("Enter the 15-Puzzle file name: ")
    fifteen_puzzle_in_file = read_file(fifteen_puzzle_file_name)
    if(fifteen_puzzle_in_file == []):
        exit()
    print(fifteen_puzzle_in_file)
    fifteen_puzzle = convert_file_to_int_matrix(fifteen_puzzle_in_file)
    print(fifteen_puzzle)