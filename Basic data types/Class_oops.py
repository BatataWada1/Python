class Circle:
    pi = 3.14159 #class variable
    def __init__(self,redius):
        self.redius = redius #instance variable
    def area(self,ent):
        print(self.pi) #accessing class variable using instance of class
        self.ent = ent #instance variable
        print(self.ent) 
        return self.redius * self.redius * Circle.pi #self.pi

obj = Circle(10)
obj1 = Circle(20) 
print(obj.area(30))
print(obj.redius)
print(obj.pi)
print(Circle.pi)
print("#################")
print(obj1.area(30))
print(obj1.redius)
print(obj1.pi)
print(Circle.pi)
print("#################")


class demo:
    print("class demo")
    class_variable = 10
    print("class variable", class_variable)

    def __init__(self, iv = 20):
        print("this is constructor")
        self.instance_variable = iv 
        print("Instance variable", self.instance_variable)
        
    @staticmethod
    def addition(a,b):
        print("this is static method addition")
        c = a + b
        print("addition is: ", c)
        print("accessing class variable", demo.class_variable)
        demo.class_variable = 90
        print("class variable change", demo.class_variable)
        #print("accessing instance variable", self.instance_variable)

objDemo = demo()
objDemo.addition(10,20)
demo.addition(20,30)
print(demo.class_variable)
print(objDemo.instance_variable)
print("#######################")

class Hospital:
    print("this is class hospital")
    class_var = 10
    print("class variable", class_var)

    def __init__(self, iv = 20):
        print("this is intance method")
        self.instance_var = iv
        print("instance variable", self.instance_var)

    @staticmethod
    def stat(a = 30, b = 40):
        print("This is static method")
        c = a + b
        print("addition in stat", c)
        print("accessing the class var ", Hospital.class_var)
        #print("accessing the instance var ", self.instance_var)

    @classmethod
    def classMethod(cls, x = 30, y = 40):
        print("this is class method")
        print(cls.class_var)
        cls.stat()
        obj = cls()
        print(obj)
        #print(cls.instance_var) 
        print("addition in class method ",(x + y))
        print("Accessing class var :", Hospital.class_var)
        #print("accessing instance var:", self.instance_var)



objHos = Hospital()
Hospital.stat()
print(Hospital.classMethod())
print("##########################")
objHos.classMethod()
Hospital.classMethod()



from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
#print(__init__)
import cmp
list1 = [1,2,3,5]
list2 = [2,3,4]
print(cmp(list1,list2))
