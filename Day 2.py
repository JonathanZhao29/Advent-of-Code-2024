# with open('Day2.txt') as file:
#     contents = file.readlines()

# res = 0
# for line in contents:
#     print(line)
#     report = line.split()
#     curr = int(report[0])
#     direction = -1 if curr-int(report[1])>0 else 1
#     for i in range(1,len(report)):
        
#         diff = abs(int(report[i]) - curr)
#         if diff > 0 and diff < 4:
#             print("Within bounds")
#             newdirection = -1 if curr-int(report[i])>0 else 1
#             if direction != newdirection:
#                 break
#             print("Within direction")
#             curr = int(report[i])
            
#         else:
#             break
#         if i == len(report)-1:
#             res +=1

content = [[*map(int, line.split())] for line in open('Day2.txt')]
#print(content)

def good(d):
    inc = [d[i+1] - d[i] for i in range(len(d)-1)] 
    if set(inc) <= {1,2,3} or set(inc) <= {-1,-2,-3}: #Check whether it is a subset of increasing or decreasing
        return True
    return False


print(sum(any([good(c[:d] + c[d+1:]) for d in range(len(c))]) for c in content))