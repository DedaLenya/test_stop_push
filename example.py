print(1233)

def fibo(num_in_fibo, i=0, fibon=[]):
    if i == num_in_fibo + 1:
        return max(fibon)

    if i > 1:
        fibon.append(fibon[i - 1] + fibon[i - 2])
    elif i == 1:
        fibon.append(i)
    else:
        fibon.append(i)
    i += 1

    return fibo(num_in_fibo, i, fibon)

print(fibo(10))