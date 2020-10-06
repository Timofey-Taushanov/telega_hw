from random import randint

def ex_8(s):
    return s == ''.join(reversed(s))

def ex_9(sec):
    d = sec // (24*3600)
    sec %= (24*3600)
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    sec %= 60
    print(d, h, m, sec, sep=':')

def ex_11():
    l = []
    for i in range(10):
        a = randint(0, 100)
        l.append(a)
    print(l, l[0], l[-1], sep='\n')

def ex_13(n):
    n = n
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    print(n+nn+nnn)

def ex_14():
    l = []
    for i in range(20):
        a = randint(0, 1000)
        l.append(a)
        if i == 19:
            l.insert(randint(0, 19), 237)
    
    print(l)

    for i in l:
        if i == 237:
            break
        elif i % 2 == 0:
            print(i)

def ex_15():
    a = [1, 3, 'bruh', 69]
    b = [1, 4, 'Bruh', 3]

    print(a, b, sep='\n')

    for i in a:
        if i not in b:
            print(i)

def ex_17(number):
    numerals = []
    
    for n in str(number):
        numerals.append(n)
    
    return sum(numerals)

def ex_18_and_19(n):
    if n == 18:
        word = 'Bruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuh'
        print(word, word.count('u'), sep='\n')
    elif n == 19:
        a = 6
        b = 9
        print(a, b, sep=' ')
        a, b = b, a
        print(a, b, sep=' ')
    else:
        print('Bruh')

def ex_21(l):
    return l == set(l)

