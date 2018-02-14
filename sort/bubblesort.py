def bubblesort(L):
    complete = False
    while complete == False:
        complete = True
        for i in range(1,len(L)):
            if L[i-1] > L[i]:
                temp = L[i-1]
                L[i-1] = L[i]
                L[i] = temp
                complete = False
    if complete == True:
        return L
        
