def max_and_min(arr1, arr2):
    stack = []
    ans = []
    n = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] - arr2[j] < 0:
                n = (arr1[i] - arr2[j]) * (-1)
            else:
                n = (arr1[i] - arr2[j])
            stack.append(n)
    ans.append(max(stack))
    ans.append(min(stack))
    return ans