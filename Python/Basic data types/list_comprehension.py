#python list comprehension

ls = []

for i in 'Human':
    ls.append(i)

print(ls)

ls = [ i for i in 'Human']

print(ls)

ls = list(map(lambda x: x, 'human'))
print(ls)


ls = list(map(lambda x: x * 2, 'human'))
print(ls)

ls = list(filter(lambda x: x % 2 == 0, range(0,20)))
print(ls) #0, 2, 4 ...


ls = list(map(lambda x: x % 2 == 0, range(0,20)))
print(ls) #True, False, True .....


ls = [ i for i in range(0,20) if i % 2 == 0 ]
print(ls)

ls = [i for i in range(100) if i % 2 == 0 if i % 5 == 0]
print(ls)

ls = [ "even" if i % 2 == 0 else "odd" for i in range(10)]
print(ls)

ls = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in matrix[0]:
    for j in matrix[1]:
        ls.append([i] + [j])

print(ls)

pq = []
for i in range(len(matrix[0])):
    print('i is ', i)
    ls = []
    for row in matrix:
        print('row is', row)
        ls.append(row[i])
        print('row[i] is', row[i])
    pq.append(ls)

print(pq)

ls = []
ls = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(ls)



