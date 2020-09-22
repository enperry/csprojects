def slices(series, length):
    if length not in range(1, len(series) + 1): 
        raise ValueError(f'Length {length} not in range for this series')
    return [series[i - length:i] for i in range(length, len(series) + 1)]
