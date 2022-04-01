import imp
from readfile import read_file

def main():
    print("Welcome to 15-Puzzle Game")
    fifteen_puzzle_file_name = input("Enter the 15-Puzzle file name: ")
    fifteen_puzzle = read_file(fifteen_puzzle_file_name)
