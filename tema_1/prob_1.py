def prob_1(u):
    m = 0
    while 1 + u != 1:
        m += 1
        u = 10 ** (-m)
    return m-1,u*10

result = prob_1(1)

print(result)