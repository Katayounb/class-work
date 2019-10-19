mylist = [1,2,3,4,5,6,7,8,9]
newlist = mylist[4:8]
print(newlist)

for n in newlist:
    n *= 2
    print(n)
myevenlist = []
myoddlist = []
list1=mylist[0:5]
print(list1)
list2=mylist[5:9]
print(list2)
print(list1, '',list2)

for n in mylist:
    if n % 2 == 0:
        myevenlist.append(n)
    else:
        myoddlist.append(n)

print(myoddlist, myevenlist)
