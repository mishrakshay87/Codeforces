wrd = input()
 
arr ="abcdefghijklmnopqrstuvwxyz"
letter_list = []
 
j = 0
count = []
for i in arr:
    letter_list.append(i)
    count.append(i+"->"+str(j))
    j += 1
 
 
right = 0
left = 0
curr = 0
rotations = 0
for w in wrd:
    index_w = letter_list.index(w)
    rotations += min(26-abs(index_w - curr),abs(index_w - curr))
 
    curr = index_w
 
 
print(rotations)