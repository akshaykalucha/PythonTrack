alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']


reversedlist = []

for i in range( len(alphabetList) - 1, -1, -1):
    reversedlist.append(alphabetList[i])


string = input()
strList = []

for i in range(len(string)):
    strList.append(string[i])

i = 0
while i < strList.__len__() - 1:
    t = strList[i]
    strList[i] = strList[i + 1]
    strList[i + 1] = t
    i = i + 2


# print(strList)

newLst = []

for j in range(len(strList)):
    for k in range(len(alphabetList)):
        if strList[j] == alphabetList[k]:
            # print(strList[j], reversedlist[k])
            newLst.append(reversedlist[k])
            break

print(*newLst, sep='')