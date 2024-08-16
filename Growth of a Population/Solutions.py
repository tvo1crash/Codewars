def nb_year(p0, percent, aug, p):
    y=0
    print(percent/100)
    while p0<p: 
        p0 = int(p0 + p0 * percent / 100 + aug)
        y += 1
    return y