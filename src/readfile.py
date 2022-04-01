import sys
def read_file(fifteen_puzzle_file_name):
    
    file_contents = []

    try:
        with open(fifteen_puzzle_file_name, 'r') as file:
            for row in file:
                row_contents = list(row.strip())
                if len(row_contents) > 0:
                    file_contents.append(row_contents)
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        print ("Unexpected error: ", sys.exc_info()[0])

    return file_contents

