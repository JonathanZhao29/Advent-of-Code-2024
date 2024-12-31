# file = open('Day5.txt')
# content = file.readline()
# inputDict = {}
# while content != "\n":
#     #print(content)
#     middle = content.find("|")
#     if int(content[:middle]) in inputDict:
#         inputDict[int(content[:middle])].append(int(content[middle+1:]))
#     else:
#         inputDict[int(content[:middle])] = [int(content[middle+1:])]
#     content= file.readline()
# #print(inputDict)
# content = file.readline()
# sum = 0
# p2Sum = 0

# def part2(arr, inputDict):
#     newArr = []
#     for key in arr:
#         if key in inputDict.keys():
#             indexes = set((newArr.index(val) if val in newArr else -1 for val in inputDict[key]))
#             if -1 in indexes:
#                 indexes.remove(-1)
#             if indexes:
#                 #print("Index", indexes)
#                 newArr.insert(min(indexes), key)
#             else:
#                 newArr.append(key)
#         else:
#             newArr.append(key)
#         #print(insertIndex)
#         #if insertIndex:
#             #newArr.insert(insertIndex, key)
#     #print(newArr)
#     #print(newArr[int((len(newArr)-1)/2)])
#     return newArr[int((len(newArr)-1)/2)]



# while content:
#     update = [*map(int, content.split(","))]
#     #print(update)
#     prev = set()
#     for val in update:
            
#         if val in inputDict.keys() and any(page in prev for page in inputDict[val]):
#             break
#         else:
#             prev.add(val)
#     if len(prev) == len(update):
#         sum+= update[int((len(update)-1)/2)]
#     else:
#         p2Sum +=part2(update, inputDict)
#     content = file.readline()
# print("Part 1",sum)
# print("Part 2", p2Sum)

from functools import cmp_to_key

rules,pages = open("Day5.txt").read().split('\n\n')

cmp = cmp_to_key(lambda x,y: -(x + '|' + y in rules)) #Create a comparison key function that puts X before Y if its X|Y is in the rules

sum = 0
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=cmp)
    if p!=s:
        sum +=int(s[len(s)//2])
print(sum)