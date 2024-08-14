def digital_root(n):
    lst = [int(i) for i in str(n)]
    while len(lst)>1:
        n = sum(lst)
        lst = [int(i) for i in str(n)]
    return lst[0]