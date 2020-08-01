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


# import math

# n= int(math.pow(10,9))
# Z = 1000000007
# g=[1,2,2,3]
# [[g.append(i)for j in range(g[i-1])]for i in range(3,n)]
# print(g)

# lst = [1,2,4,20,3,10,5]
# subsum = 33
# def subarrayGivenSum(lst, S):
#     currsum = lst[0]
#     start = 0
#     i = 1
#     while i <= len(lst):
#         while currsum > subsum and start < i - 1:
#             currsum = currsum - lst[start]
#             start += 1
#         if currsum == subsum:
#             return [start, i-1]
#         if i < len(lst):
#             currsum += lst[i]
#         i += 1
#     return -1
# z = subarrayGivenSum(lst, subsum)
# print(z)
#----------------------------------------------------------------

# All subarrays with sum k, get count

# lst = [3,4,7,2,-3,1,4,2]
# subsum = 7

# def getallsubsum(lst, S):
#     currsum = 0
#     prefixSum = []
#     count = 0
#     for i in range(len(lst)):
#         currsum += lst[i]
#         if i == 0 :
#             prefixSum.append(lst[i])
#         else:
#             newSum = prefixSum[-1] + lst[i]
#             prefixSum.append(newSum)
#         if currsum == S:
#             count += 1
#         else:
#             pre = currsum - S
#             if pre in prefixSum:
#                 print(pre)
#                 count += 1
#     return count
    
# z = getallsubsum(lst, subsum)
# print(z)


# also get all subarrays with given by doing minor modification in above function
# lst = [3,4,7,2,-3,1,4,2]
# subsum = 7

# def getallsubsum(lst, S):
#     currsum = 0
#     prefixSum = []
#     indexArr = []
#     for i in range(len(lst)):
#         currsum += lst[i]
#         if i == 0 :
#             prefixSum.append(lst[i])
#         else:
#             newSum = prefixSum[-1] + lst[i]
#             prefixSum.append(newSum)
#         if currsum == S:
#             indexArr.append(lst[0:i+1])
#         else:
#             pre = currsum - S
#             if pre in prefixSum:
#                 index = prefixSum.index(pre)
#                 indexArr.append(lst[index+1:i+1])
#     return indexArr

z = getallsubsum(lst, subsum)
print(z)
lst = [1,2,4,20,3,10,5]
subsum = 33
def subarrayGivenSum(lst, S):
    currsum = lst[0]
    start = 0
    i = 1
    while i <= len(lst):
        while currsum > subsum and start < i - 1:
            currsum = currsum - lst[start]
            start += 1
        if currsum == subsum:
            return [start, i-1]
        if i < len(lst):
            currsum += lst[i]
        i += 1
    return -1
z = subarrayGivenSum(lst, subsum)
print(z)