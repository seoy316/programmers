def solution(arr1, arr2):
    rows_A, cols_A = len(arr1), len(arr1[0])
    rows_B, cols_B = len(arr2), len(arr2[0])
    
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result