# # alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
# # 'u', 'v', 'w', 'x', 'y', 'z']


# # reversedlist = []

# # for i in range( len(alphabetList) - 1, -1, -1):
# #     reversedlist.append(alphabetList[i])


# # string = input()
# # strList = []

# # for i in range(len(string)):
# #     strList.append(string[i])

# # i = 0
# # while i < strList.__len__() - 1:
# #     t = strList[i]
# #     strList[i] = strList[i + 1]
# #     strList[i + 1] = t
# #     i = i + 2


# # # print(strList)

# # newLst = []

# # for j in range(len(strList)):
# #     for k in range(len(alphabetList)):
# #         if strList[j] == alphabetList[k]:
# #             # print(strList[j], reversedlist[k])
# #             newLst.append(reversedlist[k])
# #             break

# # print(*newLst, sep='')

# L = 1000000000123
# R = 1000000123456
# if R - L == 1:
#     print(R)
# else:
#     globarr = []
#     for i in range(L, R+1):
#         bitarr = []
#         for j in range(L, R+1):
#             if i == j:
#                 bitor = i
#                 bitarr.append(bitor)
#             else:
#                 bitor = i | j
#                 bitarr.append(bitor)
#         globarr.append(max(bitarr))
#         # print(bitarr)
#         # break
    
#     print(max(globarr))


import math

n= int(math.pow(10,9))
Z = 1000000007
g=[1,2,2,3]
[[g.append(i)for j in range(g[i-1])]for i in range(3,n)]
print(g)