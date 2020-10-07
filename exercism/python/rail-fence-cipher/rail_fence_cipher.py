def encode(message, rails):
    ciphertext = ""
    step = 2 * (rails - 1)
    # first row
    ciphertext = ciphertext + message[::step]
    # middle row
    for i in range(1, rails - 1):
        first = message[i::step]
        second = message[2 * rails - i - 2::step]
        for a, b in zip(first, second):
            ciphertext = ciphertext + a + b
        if(len(first) > len(second)):
            ciphertext = ciphertext + first[-1]
    # final row
    ciphertext = ciphertext + message[rails - 1::step]
    return ciphertext

def decode(encoded_message, rails):
    # declare variables
    grid = [[""] * len(encoded_message) for i in range(rails)]
    step = 2 * (rails - 1)
    i = 0
    # algo
    for y in range(rails):
        indices = sorted(set(range(y, len(encoded_message), step)) | set(range(2 * rails - y - 2, len(encoded_message), step)))
        for x in indices:
            grid[y][x] = encoded_message[i]
            i = i + 1
    # compile, return
    plaintext = ""
    for i in range(len(encoded_message)):
        letter = "".join(grid[j][i] for j in range(rails))
        plaintext = plaintext + letter
    return plaintext