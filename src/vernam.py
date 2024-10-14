from utils import alpha_to_index, index_to_alpha


def vernam(filename, key):
    with open(filename, 'r') as file:
        content = file.read()
    
    res = ""
    key_index = 0
    for char in content:
        if char.isalpha():
            res += index_to_alpha((alpha_to_index(char) - alpha_to_index(key[key_index])) % 26)
            key_index = (key_index + 1) % len(key)
        else:
            res += char
    
    return res


#ici la clé 'CINQ' provient du message 1.
print(vernam("data/message2.txt", "CINQ"))
