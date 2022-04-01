def convert_file_to_int_matrix(fifteen_puzzle_in_file):
    int_matrix = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        idx_col = 0
        j = 0

        while j < len(fifteen_puzzle_in_file[i]) - 1:
            if(fifteen_puzzle_in_file[i][j] != " " and fifteen_puzzle_in_file[i][j+1] != " "): # 2 digits
                int_matrix[i][idx_col] = int(fifteen_puzzle_in_file[i][j]) * 10 + int(fifteen_puzzle_in_file[i][j+1])
                idx_col += 1;
                j += 3;
            elif(fifteen_puzzle_in_file[i][j] != " " and fifteen_puzzle_in_file[i][j+1] == " "): # 1 digit
                int_matrix[i][idx_col] = int(fifteen_puzzle_in_file[i][j])
                idx_col += 1;
                j += 2;
                
        if(int_matrix[i][3] == 0):
            int_matrix[i][3] = int(fifteen_puzzle_in_file[i][len(fifteen_puzzle_in_file[i])-1])

    return int_matrix