import bnb
import reachablechecker
import utility

def print_all_values_of_less_than(fifteen_puzzle):
    print("i"+"    "+"Kurang(i)")
    for i in range(1,17):
        print(str(i)+"\t"+str(reachablechecker.less_than(i,fifteen_puzzle)))

def game_output(fifteen_puzzle):
    print("\n> Matrix posisi awal 15-Puzzle:\n")
    utility.print_matrix(fifteen_puzzle) # 1st output in project specification
    print("")
    print("> Nilai dari fungsi Kurang(i) untuk setiap ubin tidak kosong pada posisi awal:\n")
    print_all_values_of_less_than(fifteen_puzzle) # 2nd output in project specification
    print("")
    print("> Jumlah nilai Kurang(i) untuk setiap ubin tidak kosong pada posisi awal =", reachablechecker.sum_of_less_than(fifteen_puzzle))
    print("")
    print("> Jumlah seluruh nilai Kurang(i) ditambah dengan X = ",end = "")
    print(reachablechecker.sum_of_less_than_plus_x(fifteen_puzzle)) # 3rd output in project specification
    if (not reachablechecker.is_reachable(fifteen_puzzle)): # 4th output in project specification
        print("\n> Hasil: Puzzle tidak dapat diselesaikan.\n")
        exit()
    else:
        print("\n> Hasil: Puzzle dapat diselesaikan.\n")
        print("> Tahap penyelesaian:\n")
        bnb.procedure_bnb(fifteen_puzzle)