#tuple udemy

#packing and unpacking tuple

t1 = "mandar kulkarni", "hingane home colony, plot no." , 18 #packing
print(t1)

name, address, no = t1 #unpacking

print("your name {0}, your address {1}, your no {2}".format(name,address,no))

t2 = "mandar", 2020, (1, "netezza"), (2, "bigfix")

name, year, first_pro, second_pro = t2
print(name)
print(year)
print(first_pro)
print(second_pro)

print("name : {0} \nYear:{1} \nFirst Project: {2} \nSecond Project: {3}".format(name,year,first_pro,second_pro))

imelda = "More Mayhem", "Imelda May", 2011, (
     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)

name, album_name, year, tracks = imelda
print("Name of the singer is:{0} \nAlbum Name:{1} \nRelease Year:{2}".format(name,album_name,year))
for i in tracks:
    no, name = i
    print("Track No:{0} Track Name:{1}".format(no,name))
