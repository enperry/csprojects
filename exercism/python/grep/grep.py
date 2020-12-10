def grep(pattern, flags, files):
    acc = []
    for file in files:
        for i, line in enumerate(open(file).readlines(), 1):
            result = line
            if("-i" in flags):
                pattern = pattern.lower()
                line = line.lower()
            m = pattern == line.rstrip() if "-x" in flags else pattern in line
            if(("-v" in flags) ^ m):
                if("-n" in flags):
                    result = f"{i}:" + result
                if(len(files) > 1):
                    result = f"{file}:" + result
                if("-l" in flags):
                    result = file + "\n"
                if(result not in acc):
                    acc.append(result)

    return "".join(acc)