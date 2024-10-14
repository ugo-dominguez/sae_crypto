def index_to_alpha(index: int) -> str:
    return chr((ord("A") + (index % 26)))


def alpha_to_index(alpha: str) -> int:
    return ord(alpha.upper()) - ord("A")
