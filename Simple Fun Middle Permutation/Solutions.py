import math
def middle_permutation(string):
    string = sorted(string)
    n = len(string)
    
    k = math.factorial(n) // 2 - 1
    
    result = []
    for i in range(n):
        idx = k // math.factorial(n - 1 - i)
        result.append(string[idx])
        string.pop(idx)
        k %= math.factorial(n - 1 - i)
    
    return ''.join(result)