#dictionary
#unordered collection of item
#create using {} 
#dictionary has key, value
#key must be unique and immutable(int,float,string,tuple)
dict1 = {}
dict1 = {1: 'mandar', 2:'kulkarni', 'name':'latik', 3:[1, 2, 3]}
print(dict1, type(dict1))

for key in dict1:
    print(dict1[key])

dict1 = {1: 'mandar', 2:'kulkarni', 'name':'latik', 3:[1, 2, 3], 3:'str1'} # if key is repeated dict takes lates one
print(dict1) #{1: 'mandar', 2: 'kulkarni', 'name': 'latik', 3: 'str1'}

dict1 = dict([(1,'apple'), (2,'mango')])
print(dict1)

dict1 = {1: 'mandar', 2:'kulkarni', 'name':'latik', 3:[1, 2, 3], 3:'str1'}
print(dict1['name'])
print(dict1.get('name'))

dict1['add'] = 'karvenagar, pune -52'

print(dict1)

dict1['name'] = 'ashish' #key exist value updated from latik to ashish

print(dict1)

#{1: 'mandar', 2: 'kulkarni', 'name': 'ashish', 3: 'str1', 'add': 'karvenagar, pune -52'}

dict1.pop('name') #{1: 'mandar', 2: 'kulkarni', 3: 'str1', 'add': 'karvenagar, pune -52'}
print(dict1)

dict1.popitem()
print(dict1)

dict1.popitem()
print(dict1)

print(dict1.popitem()) #(2, 'kulkarni') #random remove

dict1 = {1: 'mandar', 2:'kulkarni', 'name':'latik', 3:[1, 2, 3], 3:'str1'}
print(dict1.popitem())

del dict1[1]
print(dict1)

del dict1
# print(dict1) not defined error

dict1 = {1: 'mandar', 2:'kulkarni', 'name':'latik', 3:[1, 2, 3], 3:'str1'}
items = dict1.items()
print(items)

for key,value in dict1.items():
    print(key)
    print(value)

for value in dict1.values():
    print(value)

print(dict1.values())
print(dict1.items())
print(dict1.keys())

person = {'name': 'Phill', 'age': 22, 'salary': 35000}
print(person)
salary = person.setdefault('salary')
city = person.setdefault('city')
code = person.setdefault('code', 411052)
print('salary, city, code', salary, city, code, person)


#nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)
print(people[1]['name'])
print(people[2]['sex'])

people[3] = {}
print(people)

people[3] = {'name':'ashish', 'age':27, 'sex':'male'}
people[4] = {'name':'mangesh', 'age':37, 'sex':'male'}
people[5] = {'name':'shish', 'age':47, 'sex':'male'}
people[6] = {'name':'aish', 'age':27, 'sex':'male'}
people[7] = {'name':'ashsh', 'age':57, 'sex':'male'}
print(people)
print(people.keys())
print(people.values())
print(people.items())


#to get keys
for i in people.keys():
    print(i)
print('------------keys-----------')
for i in people.values():
    print(i)

for i,j in people.items():
    print('key {0} : value{1}'.format(i,j))
    print(i,':',j)

for i in people:
    if people[i]['sex'] == 'male':
        print(people[i])

ls = []
for i in  people:
    if people[i]['sex'] == 'male':
        ls.append(people[i])

print(ls)
ls = []
print("--------------------------------------------")

for i in people:
    if people[i]["sex"] == "male":
        ls.append(people[i])
ls.sort(key = lambda x:x["age"])
print(ls)

print("----------------------------------------------")
ls = []

ls = [ people[i] for i in people if people[i]["sex"] == "male"]
ls.sort(key= lambda x:x["age"])
print(ls)

'''
rules = {
    'move':{'description':'move the file','fname':'move_file','completion_value':20,'priority':1,'enabled':1},
    'delete':{'description':'delete the file','fname':'delete_file','completion_value':50,'priority':2,'enabled':0},
    'write':{'description':'write to the file','fname':'write_to_file','completion_value':10,'priority':4,'enabled':1},
    'exit':{'description':'exit rule evaluation - do not execute any rules after this one.','fname':None,'completion_value':0,'priority':3,'enabled':1}
}

def evaluate_it(x):
    """
    this function evaluates a dictionary of rules  and returns a list
    of enabled rules to execute in order of priority
    param: x: a dictionary of rules to execute
    """
    dict1 = x.copy()
    sorting = sorted(dict1.items(), key = lambda x: (x[1]["priority"]))
    lsit = [ val for val in dict(sorting).values() for i,j in val.items() if i == 'enabled' and j == 1]
    print(lsit)

evaluate_it(rules)



'''
