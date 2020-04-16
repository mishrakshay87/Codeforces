first = list(input().split())
n_house = int(first[0])
 
task = list(map(int,list(input().split())))
 
 
house = []
for i in range(1,n_house+1):
    house.append(i)
 
 
curr_index = 0
time = 0
for i in task:
    house_ind = i - 1
    if house_ind >= curr_index:
        time += house_ind - curr_index
    else:
        time += len(house) - curr_index + house_ind 
    curr_index = house_ind
print(time)