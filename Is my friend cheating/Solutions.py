def remov_nb(n):
    result = []
    sum = n * (1 + n) / 2
    for i in range(1, n+1):
        j = (sum-i)/(i+1)
        if j == int(j) and j <= n+1 and i != j:
            result.append((int(i), int(j)))
    return result