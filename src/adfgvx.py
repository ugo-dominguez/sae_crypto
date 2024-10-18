from utils import ADFGVX, get_matrix_adfgvx


def get_key_matrix(key: str, message: str) -> list[list[str]]:
    block_len = len(message) // len(key)
    sorted_key = "".join(list(sorted(key)))
    key_matrix = [[] for _ in range(block_len)]
    sorted_key_matrix = [[] for _ in range(block_len)]

    for ind, char in enumerate(message):
        sorted_key_matrix[ind % block_len].append(char)

    for char in key:
        ind = sorted_key.find(char)
        for row in range(block_len):
            key_matrix[row].append(sorted_key_matrix[row][ind])
            
    return key_matrix


def adfgvx(filename, key, matrix):
    with open(filename, 'r') as file:
        content = file.read()

    key_matrix = get_key_matrix(key, content)
    indexes = []
    res = ""
    non_alpha = ""
    
    for line in key_matrix:
        for char in line:
            if char.isalpha():
                index = ADFGVX.find(char)
                
                if len(indexes) < 2:
                    indexes.append(index)
                else:
                    res += matrix[indexes[0]][indexes[1]] + non_alpha
                    
                    indexes = [index]
                    non_alpha = ""
            else:
                non_alpha += char

    return res


if __name__ == "__main__":
    matrix = get_matrix_adfgvx("AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M")
    print(adfgvx("data/message3.txt", "CRYPTO", matrix))