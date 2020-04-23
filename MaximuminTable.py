n_init = int(input())
 
 
arr = [1]*n_init
 
 
def maketable(arr,n,max_elem):
 
    if n == n_init:
        return max_elem
    temp_arr=[]
    temp_arr.append(1)
 
    for i in range(1,len(arr)):
        temp_arr.append(temp_arr[-1] + arr[i])
        if temp_arr[-1] > max_elem:
            max_elem = temp_arr[-1]
    return maketable(temp_arr,n+1,max_elem)
 
 
ret = maketable(arr,1,1)
print(ret)