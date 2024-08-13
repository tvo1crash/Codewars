def smaller(arr):
    sorted_arr = sorted(arr)
    dic = {}
    result = []
    for i in range(len(sorted_arr)):
        if sorted_arr[i] not in dic:
            dic[sorted_arr[i]] = i
    for i in arr:
        result.append(dic[i])
    return result
