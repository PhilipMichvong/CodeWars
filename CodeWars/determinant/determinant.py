def determinant(matrix):
    import numpy as np
    import math
    if len(matrix) == 1:
        element = [item[0] for item in matrix]
        return element[0]
    n_array = np.array(matrix)
    print(n_array)
    det = np.linalg.det(n_array)
    return int(round(det,0))