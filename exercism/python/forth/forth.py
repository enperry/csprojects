class StackUnderflowError(Exception):
    def __init__(self, message = ""):
        super().__init__(message)

def evaluate(input_data, definitions = None, stack = None):
    def parse(data):
        res_list = []
        for d in data:
            res_list.append(definitions.get(d, [d]))
        return [item for sublist in res_list for item in sublist]

    if(stack is None):
        stack = []
    if(definitions is None):
        definitions = {}
    for line in input_data:
        if(line[ : 2] == ": " and line[-2 : ] == " ;"):
            words = line[2 : -2].split(" ")
            if(words[0].isnumeric()):
                raise ValueError("Numbers can not be redefined.")
            definitions[words[0].lower()] = parse(words[1 : ])
            continue
        args = line.split(" ")
        for arg in args:
            arg = arg.lower()
            if(arg in definitions):
                stack = evaluate([" ".join(definitions[arg])], definitions, stack)
            elif(arg.isnumeric()):
                stack.append(int(arg))
            elif(arg == "+"):
                if(len(stack) < 2):
                    raise StackUnderflowError("Stack must contain two values to perform addition.")
                stack.append(stack.pop() + stack.pop())
            elif(arg == "-"):
                if(len(stack) < 2):
                    raise StackUnderflowError("Stack must contain two values to perform subtraction.")
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif(arg == "*"):
                if(len(stack) < 2):
                    raise StackUnderflowError("Stack must contain two values to perform multiplication.")
                stack.append(stack.pop() * stack.pop())
            elif(arg == "/"):
                if(len(stack) < 2):
                    raise StackUnderflowError("Stack must contain two values to perform subtraction.")
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            elif(arg == "drop"):
                if(stack):
                    stack.pop()
                else:
                    raise StackUnderflowError("Empty stack.")
            elif(arg == "dup"):
                if(stack):
                    stack.append(stack[-1])
                else:
                    raise StackUnderflowError("Empty stack.")
            elif(arg == "over"):
                if(len(stack) >= 2):
                    stack.append(stack[-2])
                else:
                    raise StackUnderflowError("Stack does not contain the 2 elements needed for over.")
            elif(arg == "swap"):
                if(len(stack) >= 2):
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                else:
                    raise StackUnderflowError("Stack does not contain the 2 elements needed for swap.")
            else:
                raise ValueError(f"Argument \"{arg}\" not recognized")
    return stack
