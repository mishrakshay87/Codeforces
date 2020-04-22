n = input()
 
arr = list(map(int,list(input().split())))
 
hs_mp={}
 
i = 0
n = len(arr)
left_count = 0
last_left = 0
right_count = 0
while i < n:
    #get left fills
    j = i - 1
    while j >= 0 and arr[j] <= arr[i]:
        if j >= 1:
            if arr[j-1] > arr[j]:
                left_count += 1
                j = j - 1
                break

        j = j - 1
        left_count += 1
 
    hs_mp[i] = left_count
 
 
 
    j = i + 1
    while j < len(arr) and arr[j] <= arr[i]:
        if j < n-1:
            if arr[j+1] > arr[j]:
                right_count += 1
                j = j + 1
                break
        right_count += 1
        j = j + 1
 
 
    hs_mp[i] = left_count + right_count + 1
    right_count = 0
    left_count = 0
    i += 1
 
 
print(max(hs_mp.values()))