from utils import ADFGVX, get_matrix_ADFGVX


def adfgvx(filename, key, matrix):
    with open(filename, 'r') as file:
            content = file.read()

    block_len = len(content) // len(key)
    sorted_key = "".join(list(sorted(key)))
    key_matrix = [[] for _ in range(block_len)]
    sorted_key_matrix = [[] for _ in range(block_len)]

    for ind, char in enumerate(content):
        sorted_key_matrix[ind % block_len].append(char)

    for char in key:
        ind = sorted_key.find(char)
        for row in range(block_len):
            key_matrix[row].append(sorted_key_matrix[row][ind])
    
    res = ""
    indexes = []
    non_alpha = ""
    
    for line in key_matrix:
        for char in line:
            if char.isalpha():
                index = ADFGVX.find(char) if char in ADFGVX else 0
                
                if len(indexes) < 2:
                    indexes.append(index)
                else:
                    res += matrix[indexes[0]][indexes[1]]
                    if len(non_alpha) > 0:
                        res += non_alpha
                    indexes = []
                    non_alpha = ""
                    indexes.append(index)
            else:
                non_alpha += char

    return res


if __name__ == "__main__":
    matrix = get_matrix_ADFGVX("AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M")
    print(adfgvx("data/message3.txt", "CRYPTO", matrix))