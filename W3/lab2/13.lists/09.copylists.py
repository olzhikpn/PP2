#1.Copy a List

#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

#2.Use the copy() method

#You can use the built-in List method copy() to copy a list.

#Example 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#3.Use the list() method

#Another way to make a copy is to use the built-in method list().

#Example 1
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#4.Use the slice Operator

#You can also make a copy of a list by using the : (slice) operator.

#Example 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)