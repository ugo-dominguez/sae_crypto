def index_to_alpha(index: int) -> str:
    return chr((ord("A") + (index % 26)))


def alpha_to_index(alpha: str) -> int:
    return ord(alpha.upper()) - ord("A")


def rearrange(matrix: list[list[str]], header: str) -> list[list[str]]:
    current_header = list(sorted(header))
    
    res = []
    header_indexes = [list(header).index(c) for c in current_header]
    
    for line_index in range(len(matrix)):
        res.append([matrix[line_index][i] for i in header_indexes])
    
    return res
