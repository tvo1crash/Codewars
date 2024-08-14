OPPOSITES = {"NORTH": "SOUTH",
             "SOUTH": "NORTH",
             "EAST" : "WEST",
             "WEST" : "EAST"}

def dirReduc(arr):    
    arr_old = arr[:]
    arr_new = []
    while True:
        idx = 0
        while idx < len(arr_old):
            if idx == len(arr_old)-1:
                arr_new.append(arr_old[idx])
            elif arr_old[idx] == OPPOSITES[arr_old[idx+1]]:
                idx += 1
            else:
                arr_new.append(arr_old[idx])
            idx += 1
        if arr_old == arr_new:
            break
        else:
            arr_old = arr_new[:]
            arr_new = []
    return arr_new
                