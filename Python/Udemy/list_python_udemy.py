#python list udemy

even = [0,2,4,6,8,10,20,18,16,14,12,10]
odd = [3,5,7,9,1]

union = even + odd
print(union)
union.sort()
print("after sorting: ",union)

fab = even
print(sorted(even),fab, sep="\n")
#will print NONE print(union.sort())

print(id(fab), id(even))
fab.sort(reverse=True)
print(" fab.sort(reverse=True) descending order of the list EVEN", even)

eve = [2,4,6,8]
eve1 = [2,4,6,8]
another_eve = eve

another_eve.sort(reverse=True)

print("printing even list", eve)

print("Is another_eve is eve? ", another_eve is eve, id(eve), id(another_eve)) #compare memory location and not content
print("Is content of another_eve == content of eve? ", another_eve == eve) #compare content

another_eve1 = list(eve1)

print("Is another_eve1 is eve1? ", another_eve1 is eve1, id(eve1), id(another_eve1))#compare memory location and not content

another_eve1.sort(reverse=True)
print("Is content of another_eve1 == content of eve1? ", another_eve1 == eve1) #compare content

members = [even, odd]
members.insert(1,"mandar")
print(members)

count = 0
for i in members:
    if isinstance(i,list):
        print("found list at index :", members.index(i))
        count += 1

print("total no of sub lists in 'members' list: ", count)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage","spam"])
menu.append(["egg", "bacon", "sausage"])
menu.append(["spam", "bacon", "sausage","spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon","spam"])
menu.append(["spam", "egg", "sausage", "spam"])


print("menu", menu)

print("printing the sub-list which do not have spam")
for i in menu:
    if "spam" not in i:
        for j in i:
            print(j)
        print("-"*10)

#print([j for j in i if "spam" not in i for i in menu ])

#create a list, then create iterator using iter() function

ls1 = [1, 2,3 ,4 ,5,22, 1,3,56,3,5,7,2,135,0]

my_iter = iter(ls1)

for i in range(0, len(ls1)):
    print(next(my_iter))

#range
print(range(10))

print(range(0,10))

print(list(range(0,11)))

even = list(range(0,100,2))
odd = list(range(1,100,2))

print(even,odd, sep="\n")

for i in even:
    if i % 5 == 0:
        print("index of {0} is {1} ".format(i, even.index(i)))
else:
    print("Iternation completed")

#if range1 == range2 : checks the value/sequence in the range

print(range(0,5,2), range(0,6,2))
print(list(range(0,5,2)),list( range(0,6,2)))
print(range(0,5,2) == range(0,6,2))

o = range(0,100,4)
print(o)
print(o[::5])
p = o[::2]
print(p)

for i in p:
    print(i)
