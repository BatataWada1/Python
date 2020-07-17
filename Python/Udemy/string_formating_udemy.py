#udeymy string formating

for i in range(1,13):
    print("{0} : square is {1} Cube is {2}".format(i, i ** 2, i ** 3))

print("###########################")

for i in range(1,13):
    print("{0:2} : square is {1:3} Cube is {2:4}".format(i, i ** 2, i ** 3))

print("###########################")

for i in range(1,13):
    print("{0:2} : square is {1:<3} Cube is {2:<4}".format(i, i ** 2, i ** 3))

print("###########################")


# f string

age = 20
name = "mandar"

#Error print("my name is " + name + "my age is : " + age)

print("my name is " + name + f" my age is: {age}")


# python string interpolation :- depricated from python 3 and recommended not to use
fl = 23.23
print("my age is %d : float is %f" % (age,fl))

meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print (meal1, meal2, meal3, meal4)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

par = "parrot"
print(par[:6] + par[6:])
