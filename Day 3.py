# content = open('Day3.txt').readlines()

# print(content)

# correct = "mul("
# sum = 0
# on = True
# for line in content:
#     i = 0
#     while i < len(line):
        
#         if line[i:i+7] == "don't()":
#             on = False
#             i +=7
#         if line[i:i+4] == "do()":
#             on = True
#             i+=4
#         print(line[i:i+4])
#         if line[i:i+4] != correct or not on:
#             i+=1
#         else: #Matches front
#             print("Front Matched")
#             #Get first number
#             leftNum = ""
#             i = i+4
#             print(line[i])
#             while line[i].isnumeric():
#                 leftNum +=line[i]
#                 i+=1
#             #Check for coma
#             if line[i] != "," or not leftNum:
#                 print("failed")
#                 continue
#             #get second number
#             rightNum = ""
#             i+=1
#             while line[i].isnumeric():
#                 rightNum+=line[i]
#                 i+=1
#             if line[i] != ")" or not rightNum:
#                 continue
            
#             sum += int(leftNum) * int(rightNum)
            
#             #check for closing parenthesis
#             i+=1
# print(sum)     

import re
content = open('Day3.txt').readlines()
sum = 0
on = True
for line in content:
    for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', line):
        match x[0]:
            case "do()":
                on = True
            case "don\'t()":
                on = False
            case _:
                if on:
                    print(int(x[1]) * int(x[2]))
                    
                    sum += int(x[1]) * int(x[2])
                    print(sum)
print(sum)