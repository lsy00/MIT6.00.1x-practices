def hannuota(n,a,b,c):
    if n == 1:
        print('%s-->%s'%(a,c))
    else:
        hannuota(n-1,a,c,b) #把n-1移到b柱
        hannuota(1,a,b,c)  #把n移去c柱
        hannuota(n-1,b,a,c) #把n和n-1叠起来到c
n = int(input('how many discs are on this tower'))
hannuota(n,'A','B','C')
