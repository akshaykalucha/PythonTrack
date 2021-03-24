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

import sys
def x(s,val):
    #print s
    global p
    if len(val)==6:
        y(val)
    else:
        i=s
        while i<len(a):
            val.append(a[i])
            x(i+1,val)
            val.remove(a[i])
            i+=1
def y(xx):
    for i in xx:
        print i,
    print ' '
if __name__=='__main__':
    a=map(int,sys.stdin.readline().strip().split())
    while a[0]!=0:
        a=a[1:]
        val=[]
        s=0
        x(s,val)
        a=map(int,sys.stdin.readline().strip().split())

@run_async
@whitelist_plus
def sudolist(bot: Bot, update: Update):
    true_sudo = list(set(SUDO_USERS) - set(DEV_USERS))
    reply = "<b>Sudo list❤:</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, user.first_name)}\n"
        except TelegramError:
            pass


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

# #len of z will be total subarrays in given array with sum k   
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



import sys
def getQ(size):
    bucket=[[] for i in range(size)]
    return bucket
def noDigit(b):
    return len(str(max(b)))
def getHash(val,i):
    i+=1
    return (val%10**i)/(10**(i-1))
def radix(b,i):
    bucket=getQ(10)
    for elem in b:
        p=getHash(elem,i)
        bucket[p].append(elem)
    dic=[]
    for everylist in bucket:
        dic.extend(everylist)
    return dic
def SortIt(b):
    noofd=noDigit(b)
    for i in range(noofd):
        b=radix(b,i)
    return b
if __name__=='__main__':
    print 'Enter The Numbers'
    a=sys.stdin.readline().split()
    b=[int(i) for i in a]
    b=SortIt(b)
    for i in b:
        print i


def main():
    N=(int)(input())
    abc=0;
    for akjhdkafka in range(N):
        abc+=1
        s="Case #"+str(abc)+": "
        C=(int)(input())
        I=(int)(input())
        A=raw_input().split(' ')
        P=[]
        for x in range(len(A)):
            P.append((int)(A[x]))
        a=-1
        b=-1
        for x in range(len(P)):
            if C-P[x] in P:
                a=x;
                b=P.index(C-P[x],x);
                break;
        if(a>b):
            s+=str(b+1)+' '+str(a+1)
        else:
            s+=str(a+1)+' '+str(b+1)
        print s
if __name__=='__main__':
    main()


import sys
def ans(n,b,i,val):
    if n==i or n==0:
        return val+i
    if b==val+i:
        return ans(n,b,i+1,val)
    else:
        return ans(n,b,i+1,val+i)
def main():
    t=int(sys.stdin.readline())
    for i in range(t):
        n,b=sys.stdin.readline().split()
        print ans(int(n),int(b),0,0)
if __name__=='__main__':
    main()



class Totient:
    def __init__(self, n):
        self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1:
                for j in range(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]
if __name__ == '__main__':
    from itertools import imap
    totient = Totient(10**18)
    print totient
    #print sum(imap(totient, range(10**18)))


  
import sys
if __name__=='__main__':
    xx=[0]*(10**9+2)
    for i in range(1000):
        for j in range(1000):
            p=i*i+j*j
            if p<=10**9:
                xx[p]=1
    print xx

"""
Searching a sorted array by repeatedly dividing the search interval in half
"""

def BinarySearch(list1, x):
	low = mid = 0
	high = len(list1) - 1

	while(low <= high):
		mid = (low + high) // 2

		if(x < list1[mid]):
			high = mid - 1
		elif(x > list1[mid]):
			low = mid + 1
		else:
			return mid
	return -1

print("Enter sorted list with space between them : ")
nums = [int(x) for x in input().split()]
x = int(input("Enter the element to search : "))
index = BinarySearch(nums, x)
if index != -1:
	print("{0} element was found at position {1}".format(x, index + 1))
else:
	print("Element not found")