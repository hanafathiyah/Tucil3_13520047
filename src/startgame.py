import convertfile
import readfile
import output

def main():

    print("Welcome to 15-Puzzle Game")

    fifteen_puzzle_file_name = input("Enter the 15-Puzzle file name: ")
    fifteen_puzzle_in_file = readfile.read_file(fifteen_puzzle_file_name)

    if(fifteen_puzzle_in_file == []):
        exit()

    fifteen_puzzle = convertfile.convert_file_to_int_matrix(fifteen_puzzle_in_file)
    output.game_output(fifteen_puzzle)