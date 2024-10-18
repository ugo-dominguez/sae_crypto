ADFGVX = "ADFGVX"


def index_to_alpha(index: int) -> str:
    return chr((ord("A") + (index % 26)))


def alpha_to_index(alpha: str) -> int:
    return ord(alpha.upper()) - ord("A")


def get_matrix_ADFGVX(symbols) -> list[list[str]]:
    ncols = len(ADFGVX)
    return [symbols[i:i + ncols] for i in range(0, len(symbols), ncols)]
