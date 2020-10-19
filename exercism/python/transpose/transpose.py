from itertools import zip_longest
    
def transpose(lines: str):
    return "\n".join("".join(chars).rstrip("-") for chars in zip_longest(*lines.split("\n"), fillvalue = "-")).replace("-", " ")
