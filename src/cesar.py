from utils import alpha_to_index, index_to_alpha


def cesar(char: str, incr: int) -> str:
    if char.isalpha():
        return index_to_alpha((alpha_to_index(char) + incr) % 26)
    
    return char


def cesar_file(filename: str, incr: int) -> str:
    with open(filename, 'r') as file:
        return "".join(cesar(char, incr) for char in file.read())


def acrostic_cesar_file(filename: str, incr: int) -> str:
    with open(filename, 'r') as file:
        return "".join(cesar(line[0], incr) for line in file.readlines())


if __name__ == "__main__":
    print(cesar_file("data/message1.txt", 14))
    print(acrostic_cesar_file("data/message1.txt", 14))
    # La réponse est 'CINQ'
