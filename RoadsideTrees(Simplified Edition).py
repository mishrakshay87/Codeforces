
n = int(input())

arr=[]
for j in range(n):
    elem = int(input())
    arr.append(elem)


    
t = arr[0] + 1
    
for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            t += arr[i] - arr[i-1] + 2
        else:
            t += arr[i-1] - arr[i] + 2
    
print(t)    