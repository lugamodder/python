def bubble_sort(a):
    for j in range (0,len(a)):
         for i in range(0,len(a)-1):
             if a[i] < a[i+1]:
                 a[i],a[i+1] = a[i+1],a[i]
    return a

def shake_sort(a):
    l = 0
    r = len(a)-1

    while l <= r:
        for i in range(l,r,+1):
             if a[i] < a[i+1]:
                 a[i],a[i+1] = a[i+1],a[i]

        r -= 1

        for i in range(r,l,-1):
             if a[i-1] < a[i]:
                 a[i],a[i-1] = a[i-1],a[i]

        l += 1

    return(a)




if __name__ == '__main__':
    import timeit
    a = [1,4,2,5,3,8,22,54,11,69,7,33,62,71,0,83,99,12,34]
    print(shake_sort(a))
    a = [1,4,2,5,3,8,22,54,11,69,7,33,62,71,0,83,99,12,34]
    print(bubble_sort(a))