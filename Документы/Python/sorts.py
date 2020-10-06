git add *

def bubble(l):
    if type(l) != list:
        return l
    if len(l) <= 1:
        return l
    for i in l:
        if type(i) == int:
            continue
        elif type(i) == float:
            continue
        else:
            return l
    
    is_replaced = True
    while is_replaced:
        is_replaced = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                is_replaced = True
    return l

def qsort(l):
    if type(l) != list:
        return l
    if len(l) <= 1:
        return l
    for i in l:
        if type(i) == int:
            continue
        elif type(i) == float:
            continue
        else:
            return l
    
    p = len(l)-1
    i = -1
    j = 0
    pivot = l[p]
    while True:
        a = l[j]
        if a >= pivot:
            j += 1
        else:
            i += 1
            l[i], l[j] = l[j], l[i]
            j += 1
        if j == len(l)-1:
            del l[p]
            l.insert(i+1, pivot)
            break
    
    high = []
    less = []

    for q in l:
        if q >= pivot:
            high.append(q)
        elif q < pivot:
            less.append(q)

    qsort(less)
    qsort(high)

    l.clear()

    for q in less:
        l.append(q)
    for q in high:
        l.append(q)
      
    return l

def merge(l):
    if type(l) != list:
        return l
    if len(l) <= 1:
        return l
    for i in l:
        if type(i) == int:
            continue
        elif type(i) == float:
            continue
        else:
            return l

    
    n = len(l)
    l_One = []
    l_Two = []
    
    for i in range(0, n//2):
        l_One.append(l[i])
    for i in range(n//2, n):
        l_Two.append(l[i])
    
    l.clear()

    merge(l_One)
    merge(l_Two)

    while l_One and l_Two:

        if l_One[0] >= l_Two[0]:
            l.append(l_Two[0])
            del l_Two[0]
        else:
            l.append(l_One[0])
            del l_One[0]

    while l_One:
        l.append(l_One[0])
        del l_One[0]

    while l_Two:
        l.append(l_Two[0])
        del l_Two[0]
    
    return l

bruh = [7, 2, 1, 3, 6, 5, 4, 8]
qsort(bruh)
print(bruh)