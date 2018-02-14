def genPrimes():
    num = 1
    primenum = []
    while True:
        isPrime = True
        if num >=3:
            num += 2
        else:
            num += 1
        for prime in primenum:
            if num!=2 and num%prime == 0:
                isPrime = False
        if isPrime == True:
            yield num
            primenum.append(num)

a = genPrimes()
