ACTIONS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(number):
    result = [code for i, code in enumerate(ACTIONS) if number & 2 ** i]
    return result[::-1] if number & 16 else result