#dict in python :- udemy

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making clider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
print("value of key:Apple:", fruit["apple"])
fruit["pare"]  = "greenish fruit"

print(fruit)
del fruit["lime"]
print(fruit)
#fruit.clear()
#print(fruit)

while True:
    user_choice = input("Please Enter fruit name or exist: ")
    if user_choice == "exist":
        break
    else:
        dic_val = fruit.get(user_choice, "we do not have {0}".format(user_choice))
        print(dic_val)

#sorting dict1

keys = fruit.keys()
ls = list(keys)
print(ls)
ls.sort()
print("ls after sorting", ls)
for i in ls:
    print(i + ":"+ fruit[i])
#ls.sort()

for i in sorted(fruit.keys()):
    print(i + ":" + fruit[i])


for k,v in fruit.items():
    print(k,v)

tuple1 = fruit.items()

print(tuple1)

for item in tuple1:
    key, val = item
    print("key is ", key)
    print("val is", val)

tu = ([('mandar', 'kulkarni1')]) #even required
name = tu
print("name, surname", name )

dict1 = dict(tu)

print(dict1)

print(tuple(tuple1))

user_input = input("ENTER SOME TEXT HERE : ")
str1= ""
fset = frozenset(user_input)
vowels_set = set("aAeEiIoOuU")
print(vowels_set)
ls = []
for i in user_input:
    #if i not in {'a','A','e','E','i','I','o','O','u','U'}:
    if i not in vowels_set:
        #str_without_vowels = str_without_vowels + i
        str1 = str1 + i
        ls.append(i)
print("list without vowels", ls)
print("str ", str1)

print(fset - vowels_set)
