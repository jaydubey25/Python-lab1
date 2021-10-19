>>> list=[]
>>> list=[1,2,3]
>>> list1=[1,"hello",4.2]
>>> list1
[1, 'hello', 4.2]
>>> list1=[1,"hello",[1,4.2]]
>>> list1
[1, 'hello', [1, 4.2]]
>>> print(list1[-1:1])
[]
>>> list1.append(4)
>>> list1
[1, 'hello', [1, 4.2], 4]
>>> list1.append([1,4])
>>> list1.append(4)
>>> list1
[1, 'hello', [1, 4.2], 4, [1, 4], 4]
>>> list1[2]='r'
>>> list1
[1, 'hello', 'r', 4, [1, 4], 4]
>>> list1.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
>>> list1.extend([1,2,3])
>>> list1
[1, 'hello', 'r', 4, [1, 4], 4, 1, 2, 3]
>>> list1 + (1,2,3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list1 + (1,2,3)
TypeError: can only concatenate list (not "tuple") to list
>>> list1 + [1,2,3]
[1, 'hello', 'r', 4, [1, 4], 4, 1, 2, 3, 1, 2, 3]
>>> print(["sukhdev"]*3)
['sukhdev', 'sukhdev', 'sukhdev']
>>> list1.insert(3,"sukhdev sharma")
>>> list1
[1, 'hello', 'r', 'sukhdev sharma', 4, [1, 4], 4, 1, 2, 3]
>>> list
[1, 2, 3]
>>> list=[1,3,4]
>>> list[1:1]=[9,93,44]
>>> list
[1, 9, 93, 44, 3, 4]
>>> list[1:3]=[9,93,44]
>>> list
[1, 9, 93, 44, 44, 3, 4]
>>> list.remove(44)
>>> list
[1, 9, 93, 44, 3, 4]
>>> list.pop()
4
>>> list
[1, 9, 93, 44, 3]
>>> list.clear()
>>> list
[]
>>> list=[11,3,4,2,5,6,4,5]
>>> list.count(4)
2
>>> 
