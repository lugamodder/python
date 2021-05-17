def bubble_sort(a):
    for j in range (0,len(a)):
         for i in range(0,len(a)-1):
             if a[i] < a[i+1]:
                 a[i],a[i+1] = a[i+1],a[i]
    return a
    
if __name__ == '__main__': 
    a = [1,4,2,5,3,8,22,54,11,69,7,33,62,71,0,83,99,12,34]
    print(bubble_sort(a))