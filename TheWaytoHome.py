max_step = int(list(input().split(" "))[1])
 
arr = list(map(int,list(input())))
start = 0
curr = 0
count = 0
step = max_step
 
def findjumps(count,curr):
 
    if curr == len(arr)-1:
        return count
    step = max_step
    if curr + max_step <= len(arr):
        while curr + step < len(arr) and arr[curr + step] != 1 and step >0:
            step -= 1
        if curr+step >= len(arr):
            count += 1
            return count
        if arr[curr + step] != 1 or step <=0:
            return -1
        count += 1
        curr += step
    else:
        curr = len(arr)-1
        count += 1
        return count
    return findjumps(count,curr)
 
 
print(findjumps(0,0))