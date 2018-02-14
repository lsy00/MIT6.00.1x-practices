def selectionsort(L):
    def getsorted(L):
        global sortedlist
        if len(L) == 1:
            sortedlist.append(L[0])
            print sortedlist
        else:
            smallest = L[0]
            for i in L:
                if i < smallest:
                    smallest = i
            sortedlist.append(smallest)
            L.remove(smallest)
            return getsorted(L)

    global sortedlist    
    sortedlist = []
    if L == []:
        return []
    getsorted(L)
    return sortedlist
    
    

selectionsort([9,1,6,8,7,7])

def selectionsort2(L):
    
suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt,len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt],L[i] = L[i],L[suffixSt]
        suffixSt+=1
        #don't copy the list
        #find the right pointer and insert the element
