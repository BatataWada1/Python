#program flow control in python udemy

d1, d2, d3 = 1, 2, 3

print(d2)
if d2 == 3 and d1 > 1 or d3:
    print("i am in ")
else:
    print("i am out")

#will print i am in because OR is higher precedance than AND

if (d2 == 3 and d1 > 1) or not d3:
    print("i am in")
else:
    print("i am out")


str1 = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for i in str1:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(i)

#for i in range(0,101):
#    if (i %  7 == 0) :
#        print(i)

        
print(4 //2)

div = 14

if div / 7:
    print(div)

## one to thirty table

#for i in range(1,31):
#    for j in range(1,31):
#        print("{0:2} times {1:2} is {2:2}".format(j, i, i * j))
#    print('--' * 20)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(0,21):
    if i > 0:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            print(i)


number = 5
multiplier = 8
answer = 0
 
# add your loop after this comment
for i in range(0,multiplier):
     answer += number
print(answer)

for i in range(1,11):
    print(i, end="\t")
    if i % 12 == 0:
        print("found")
        break
else:
    print("iteration completed")

import sys
while True:
    user_option = int(input("Please Enter one of the option from below \n1.Learn Python\n2.Learn Java\n3.Go swimming\n4.Have dinner\n5.Go to bed\n6.Exit\n[OPTION]: "))
    print("you selected [OPTION]: {0}".format(user_option))
    if user_option == 1:
      print("Hello to the world of Python")  
    if user_option == 6:
        print("Thank you for visiting")
        #sys.exit()
        break
