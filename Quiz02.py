"""aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

list1 = ["PYthon", [4, 8, 12, 16]]
print(list1[0][1])    
print(list1[1][3])

l = ["list"] * 10
print(len(l))

l = [None] * 10
print(l)
print(len(l))

list2 = ["a", "e", "i", "o", "t"]
list2.sort(reverse=True)
print(list2)

sample = [10, 20, 30, 40, 50]
print(sample[-2])
print(sample[-4:-1])"""

num = [10, 20, 30, 40]
del num[0:6]
print(num)

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

newList = listOne + listTwo
#newList = extend(listOne, listTwo)
#newList = listOne.extend(listTwo)
#newList.extend(listOne, listTwo)

print(newList)

"""list1 = ['xyz', 'zara', 'python']
print (max(list1))

my_list = [1, 2, 3]
my_list[1:2] = [99, 100] 

print(my_list)

print(list((1, 2, [3, 4]))[2][1])

a = [1, 2, 3] 
b = a 
b[0] = 10 

print(a)
print(b)"""

old_list = [1, 2, 5]
new_list = [6, 8]

old_list.append(new_list)
print(old_list)
print(len(old_list))

tup1 = ("apple", "grapes", "lemon")
tup2 = (1, 2, 3)
print(tup1 + tup2)

name = "Madagascar"
print(name[2:6])