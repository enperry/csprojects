def saddle_points(matrix):
    if(len(set(map(len, matrix))) > 1):
        raise ValueError("irregular matrix")
    # declare vars, algorithm
    pointsList = []
    # go through rows and cols, check for condition of saddle point
    for i, row in enumerate(matrix, 1):
        for j, number in enumerate(row, 1):
            if(number == max(row) and number == min(row[j - 1] for row in matrix)):
                pointsList.append({"row": i , "column": j})
    return pointsList