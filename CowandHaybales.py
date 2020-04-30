n = int(input())
 
 
for j in range(n):
    l1 = list(map(int,list(input().split())))
    
    d =  l1[1]
    
    w = list(map(int,list(input().split())))
 
    t = 0
    
    for i in range(1,len(w)):
    
        if t + i > d:
            break
        while w[i] != 0 and t < d:
            w[i] = w[i] - 1
            w[0] += 1
            t += i
            if t + i > d:
                break
    
    print(w[0])