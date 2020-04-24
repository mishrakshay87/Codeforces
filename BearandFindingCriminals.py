pos = list(map(int,list(input().split())))[1]
 
pos = pos - 1
arr = list(map(int,list(input().split())))
 
j = pos - 1
k = pos + 1
count = 0
if arr[pos] == 1:
    count = 1
 
 
while j >= 0 and k < len(arr):
    if arr[j] == arr[k] == 1:
        count += 2
    j = j - 1
    k = k + 1
 
while j >= 0:
    if arr[j] == 1:
        count += 1
    j = j - 1
 
while k < len(arr):
    if arr[k] == 1:
        count += 1
    k = k + 1
 
print(count)