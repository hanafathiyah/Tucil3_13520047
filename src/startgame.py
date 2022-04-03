import imp
import convertfile
import readfile
import output
import os

def main():
    os.system("cls")
    print("Selamat datang di permainan 15-Puzzle\n")
    fifteen_puzzle_file_name = input("Masukkan nama file permainan 15-Puzzle: ")
    fifteen_puzzle_in_file = readfile.read_file(fifteen_puzzle_file_name)

    if(fifteen_puzzle_in_file == []):
        exit()

    fifteen_puzzle = convertfile.convert_file_to_int_matrix(fifteen_puzzle_in_file)
    output.game_output(fifteen_puzzle)