operations = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '/'}

def answer(question):
    question = question.replace('What is ', '').replace('?', '')
    for op in operations:
        question = question.replace(op, operations[op])
    parts = question.split()
    try:
        # yes, eval sucks and should be avoided
        # but this makes it so much easier without using re which is Complicated™ for a short exercise
        result = eval(' '.join(parts[:3]))
        for i in range(3, len(parts), 2):
            result = eval(str(result) + ' ' + parts[i] + ' ' + parts[i + 1])
        return result
    except:
        raise ValueError("invalid expression")