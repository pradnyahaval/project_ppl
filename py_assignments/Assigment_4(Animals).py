print("classes: dog, lion, goat, tiger, cat, elephant, camel, zebra, cow, deer")

class tiger():
    def __init__(self, e="black", c="orange"):
        self._legs='4'
        self._eyecolor=e
        self._skincolor=c
        
    def get_legs(t):
        return t._legs
    def get_eyecolor(t):
        return t._eyecolor
    def get_skincolor(t):
        return t._skincolor
    def sound(t):
        print("sound: roar")

class lion(tiger):                  #Inheritance
    def get_legs(l):
        return l._legs
    def get_eyecolor(l):
        return l._eyecolor
    def set_skincolor(l, sc):
        l._skincolor=sc
    def get_skincolor(l):
        return l._skincolor
    def sound(l):
        print("sound: roar")

class cat(tiger):
        def get_legs(c):
            return c._legs
        def set_eyecolor(c, e):
            c._eyecolor=e
        def get_eyecolor(c):
            return c._eyecolor
        def set_skincolor(c, sc):
            c._skincolor=sc
        def get_skincolor(c):
            return c._skincolor
        def sound(c):
            print("sound: meow")
            
class cow(tiger):
    #def get_legs(w):
    #    return w._legs
    def get_eyecolor(w):
        return w._eyecolor
    def set_skincolor(w, sc):
        w._skincolor=sc
    def get_skincolor(w):
        return w._skincolor
    def sound(w):
        print("sound: moo")
        
class elephant(tiger):
    def get_legs(e):
        return e._legs
    def get_eyecolor(e):
        return e._eyecolor
    def set_skincolor(e, sc):
        e._skincolor=sc
    def get_skincolor(e):
        return e._skincolor
    def sound(e):
        print("sound: trumpet")
        
class rabbit(tiger):
    def get_legs(r):
        return r._legs
    def set_eyecolor(r, e):
        r._eyecolor=e
    def get_eyecolor(r):
        return r._eyecolor
    def set_skincolor(r, sc):
        r._skincolor=sc
    def get_skincolor(r):
        return r._skincolor
    def sound(r):
        print("sound: muttering")
        
class squirrel(tiger):
    def get_legs(s):
        return s._legs
    def get_eyecolor(s):
        return s._eyecolor
    def get_skincolor(s):
        return s._skincolor
    def sound(s):
        print("sound: chirping")
        
class fox(tiger):
    def get_legs(f):
        return f._legs
    def set_eyecolor(f, e):
        f._eyecolor=e
    def get_eyecolor(f):
        return f._eyecolor
    def set_skincolor(f, sc):
        f._skincolor=sc
    def get_skincolor(f):
        return f._skincolor
    def sound(e):
        print("sound: simper")
        
class monkey(tiger):
    def get_legs(m):
        return m._legs
    def get_eyecolor(m):
        return m._eyecolor
    def set_skincolor(m, sc):
        m._skincolor=sc
    def get_skincolor(m):
        return m._skincolor
    def sound(e):
        print("sound: chatter")
        
class kangaroo(tiger):
    def set_legs(k, n):
        k._legs=n
    def get_legs(k):
        return k._legs
    def get_eyecolor(k):
        return k._eyecolor
    def set_skincolor(k, sc):
        k._skincolor=sc
    def get_skincolor(k):
        return k._skincolor
    def sound(k):
        print("sound: chortle")
            


if __name__=='__main__':
    t=tiger()
    print("\nTiger:")
    print("No. of legs: "+t.get_legs())
    print("Eye color: "+t.get_eyecolor())
    print("Skin color: "+t.get_skincolor()) 
    t.sound()
    
    l=lion()
    l.set_skincolor("brown")
    print("\nLion:")
    print("No. of legs: "+l.get_legs())
    print("Eye color: "+l.get_eyecolor())
    print("Skin color: "+l.get_skincolor())
    l.sound()
    
    c=cat()
    c.set_eyecolor("golden")
    c.set_skincolor("black")
    print("\nCat:")
    print("No. of legs: "+c.get_legs())
    print("Eye color: "+c.get_eyecolor())
    print("Skin color: "+c.get_skincolor())  
    c.sound()
    
    w=cow()
    w.set_skincolor("white")
    print("\nCow:")
    print("No. of legs: "+t.get_legs())
    print("Eye color: "+w.get_eyecolor())
    print("Skin color: "+w.get_skincolor())
    w.sound()
    
    e=elephant()
    e.set_skincolor("gray")
    print("\nElephant:")
    print("No. of legs: "+e.get_legs())
    print("Eye color: "+e.get_eyecolor())
    print("Skin color: "+e.get_skincolor())
    e.sound()
    
    r=rabbit()
    r.set_skincolor("white")
    r.set_eyecolor("red")
    print("\nRabbit:")
    print("No. of legs: "+r.get_legs())
    print("Eye color: "+r.get_eyecolor())
    print("Skin color: "+r.get_skincolor())
    r.sound()
    
    s=squirrel()
    print("\nSquirrel:")
    print("No. of legs: "+s.get_legs())
    print("Eye color: "+s.get_eyecolor())
    print("Skin color: "+l.get_skincolor())
    s.sound()
    
    f=fox()
    f.set_eyecolor("yellow")
    f.set_skincolor("rusty red")
    print("\nFox:")
    print("No. of legs: "+f.get_legs())
    print("Eye color: "+f.get_eyecolor())
    print("Skin color: "+f.get_skincolor())
    f.sound()
    
    m=monkey()
    m.set_skincolor("gray")
    print("\nMonkey:")
    print("No. of legs: "+m.get_legs())
    print("Eye color: "+m.get_eyecolor())
    print("Skin color: "+l.get_skincolor())
    m.sound()
    
    k=kangaroo()
    k.set_legs('3')
    k.set_skincolor("brown")
    print("\nKangaroo:")
    print("No. of legs: "+k.get_legs())
    print("Eye color: "+k.get_eyecolor())
    print("Skin color: "+k.get_skincolor())
    k.sound()
 
    

        
        
