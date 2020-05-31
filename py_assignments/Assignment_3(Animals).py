#Abstraction- different individual clases

#Encapsulation- hides the implementation details from user 
print("classes: dog, lion, goat, tiger, cat, elephant, camel, zebra, cow, deer")

print("1) DOG :")
class dog():
    def __init__(self):
        self.__color="black"                        #atributes or instance variables 
        self.__sound="bark"                         #private variables
        self.__maxAge=12
   
    def get_color(self):
        return self.__color
    def set_color(self, color):
         self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is domestic animal")
c1=dog()
print("Furcolor of dog is ", c1.get_color())
c1.set_color("white")
print("Furcolor of dog After using set function is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())


print("\n2) LION:")
class lion():
    def __init__(self):
        self.__color="orange"                         #atributes or instance variables 
        self.__sound="roar"
        self.__maxAge=30
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c2=lion()
print("Furcolor of lion is ", c2.get_color())
c2.set_color("brown")
print("Furcolor of dog After using set function is ", c2.get_color())
c2.sound()
print("Its max age is ", c2.get_maxAge())


print("\n3) GOAT:")    
class goat():
    def __init__(self):
        self.__color="black and white"                         #atributes or instance variables 
        self.__sound="bleat"
        self.__maxAge=15
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c3=goat()
print("Furcolor of goat is ", c3.get_color())
c3.set_color("black")
print("Furcolor of dog After using set function is ", c3.get_color())
c3.sound()
print("Its max age is ", c3.get_maxAge())


print("\n4) TIGER:")    
class tiger:
    def __init__(self):
        self.__color="orange"                         #atributes or instance variables 
        self.__sound="roar"
        self.__maxAge=30
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c4=tiger()
print("Furcolor of tiger is ", c4.get_color())
c4.set_color("yellow")
print("Furcolor of tiger After using set function is ", c4.get_color())
c4.sound()
print("Its max age is ", c4.get_maxAge())


print("\n5) CAT:")    
class cat:
    def __init__(self):
        self.__color="brown"                         #atributes or instance variables 
        self.__sound="meow"
        self.__maxAge=15
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is domestic animal")
c5=cat()
print("Furcolor of cat is ", c5.get_color())
c5.set_color("white")
print("Furcolor of cat After using set function is ", c1.get_color())
c5.sound()
print("Its max age is ", c5.get_maxAge())


print("\n6) ELEPHANT:")   
class elephant:
    def __init__(self):
        self.__color="gray"                         #atributes or instance variables 
        self.__sound="trumpet"
        self.__maxAge=50
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c1=elephant()
print("Furcolor of elephant is ", c1.get_color())
c1.set_color("brown")
print("Furcolor of elephant After using set function is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())


print("\n7) CAMEL:")    
class camel:
    def __init__(self):
        self.__color="brown"                         #atributes or instance variables 
        self.__sound="grunt"
        self.__maxAge=25
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is domestic animal")
c1=camel()
print("Furcolor of camel is ", c1.get_color())
c1.set_color("chocolety")
print("Furcolor of camel After using set function is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())


print("\n8) ZEBRA:")   
class zebra:
    def __init__(self):
        self.__color="black and white"                         #atributes or instance variables 
        self.__sound="whinny"
        self.__maxAge=2
        
    def get_color(self):
        return self.__color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c1=zebra()
print("Furcolor of zebra is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())


print("\n9) COW:")    
class cow:
    def __init__(self):
        self.__color="white"                         #atributes or instance variables 
        self.__sound="moo"
        self.__maxAge=13
        
    def get_color(self):
        return self.__color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is domestic animal")
c1=cow()
print("Furcolor of cow is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())


print("\n10) DEER:")    
class deer:
    def __init__(self):
        self.__color="chocolety"                         #atributes or instance variables 
        self.__sound="bell"
        self.__maxAge=12
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color
    def sound(self):
        print("Its sound is ", self.__sound)
    def get_maxAge(self):
        return self.__maxAge
    def living(self):
        print("It is wild animal")
c1=deer()
print("Furcolor of deer is ", c1.get_color())
c1.set_color("golden")
print("Furcolor of deer After using set function is ", c1.get_color())
c1.sound()
print("Its max age is ", c1.get_maxAge())



