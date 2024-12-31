with open('Day1.txt') as file:
    contents = file.readlines()

dict1 = {}
arr1 = []
arr2 = []

for line in contents:
    line = line.split()
    val = int(line[1])
    if val in dict1:
        dict1[val] +=1
    else:
        dict1[val] = 1
    arr1.append(int(line[0]))
    arr2.append(val)
sum=0
#print(arr1,arr2,dict1)
for i in range(len(arr1)):
    if arr1[i] in dict1:
        sum += arr1[i] * dict1[arr1[i]]
print(sum)