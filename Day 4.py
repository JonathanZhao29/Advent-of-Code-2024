input = [list(line.strip()) for line in open('Day4.txt')]
print(input)
# def check(x,y, i, j, content):
#     match x,y:
#         case 0,-1: #Straight Up
#             if content[i-1][j] == "M" and content[i-2][j] == "A" and content[i-3][j] == "S":
#                 #print(i,j)
#                 return True
#         case -1,-1: #Left Up
#             if content[i-1][j-1] == "M" and content[i-2][j-2] == "A" and content[i-3][j-3] == "S":
#                 #print(i,j)
#                 return True
#         case 0, 1: #Straight Down
#             if content[i+1][j] == "M" and content[i+2][j] == "A" and content[i+3][j] == "S":
#                 #print(i,j)
#                 return True
#         case 1,1: #Right Down
#             if content[i+1][j+1] == "M" and content[i+2][j+2] == "A" and content[i+3][j+3] == "S":
#                 #print(i,j)
#                 return True
#         case 1,-1: #Left Down
#             if content[i+1][j-1] == "M" and content[i+2][j-2] == "A" and content[i+3][j-3] == "S":
#                 #print(i,j)
#                 return True
            
#         case -1,1: #Right Up
#             if content[i-1][j+1] == "M" and content[i-2][j+2] == "A" and content[i-3][j+3] == "S":
#                 #print(i,j)
#                 return True
#         case 1,0: #Right
#             if content[i][j+1] == "M" and content[i][j+2] == "A" and content[i][j+3] == "S":
#                 #print(i,j)
#                 return True
#         case -1,0: #Left
#             if content[i][j-1] == "M" and content[i][j-2] == "A" and content[i][j-3] == "S":
#                 #print(i,j)
#                 return True
#     return False
            


# sum = 0
# for i in range(len(input)):
#     for j in range(len(input[0])):
#         if input[i][j] == "X":
#             #print(input[i][j], i+1,j+1)
#             #Search all directions for xmas
#             #Up
#             if i >2:
#                 #Straight up
#                 if check(0,-1, i,j, input):
#                     sum+=1
#                 #Left Up
#                 if j >2:
#                     sum +=1 if check(-1,-1, i,j, input) else 0
#                 #Right Up
#                 if j < len(input[0])-3:
#                     sum +=1 if check(-1,1, i,j, input) else 0
#             #Down
#             if i < len(input)-3:
#                 #Straight Down
#                 if check(0,1, i,j, input):
#                     sum+=1
                
#                 #Left Down
#                 if j > 2:
#                     sum +=1 if check(1,-1, i,j, input) else 0
#                 #Right Down
#                 if j < len(input[0])-3:
#                     sum +=1 if check(1,1, i,j, input) else 0
            
#             #Left
#             if j>2:
#                 sum +=1 if check(-1,0, i,j, input) else 0
#             #Right
#             if j < len(input[0])-3:
#                 sum +=1 if check(1, 0, i,j, input) else 0
# print(sum)

def leftCross(i,j,input):
    if input[i-1][j-1] == "M" and input[i+1][j+1] == "S":
        return True
    elif input[i-1][j-1] == "S" and input[i+1][j+1] =="M":
        return True
    return False

def rightCross(i,j,input):
    if input[i-1][j+1] == "M" and input[i+1][j-1] == "S":
        return True
    elif input[i-1][j+1] == "S" and input[i+1][j-1] =="M":
        return True
    return False

def checkCrosses(i,j,input):
    return leftCross(i,j,input) and rightCross(i,j,input)

sum = 0
for i in range(len(input)):
     for j in range(len(input[0])):
        if input[i][j] == "A":
            if i <1 or i >len(input)-2 or j <1 or j > len(input[0])-2:
                continue
            else:
                #Check for cross
                sum+=1 if checkCrosses(i,j,input) else 0
print(sum)