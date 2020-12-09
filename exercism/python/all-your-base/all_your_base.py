def rebase(input_base, digits, output_base):
    if(input_base < 2 or output_base < 2):
        raise ValueError("Invalid base")

    if(any([True for x in digits if x >= input_base or x < 0])):
        raise ValueError("Invalid digits")

    quo = sum([x * input_base ** exp for exp, x in enumerate(digits[::-1])])
    result = list() if quo else [0]
    while quo:
        quo, rem = divmod(quo, output_base)
        result.append(rem)

    return result[::-1]