'''Multiple Threading - different classes run at same time...
    Program has one main thread and t1, t2, t3 are its tasks'''

print("Current time using multiple threads is: (hrs : mins : sec)")

import threading 
import datetime

def hours(current):
        h=current.hour
        if h<10:
            print("0 ", h, end=" : ")
        else:
            print(h, end=" : ")

def minutes(current):
        m=current.minute
        if m<10:
            print("0", m, end=" : ")
        else:
            print(m, end=" : ")


def seconds(current):
        s=current.second
        if s<10:
            print("0", s)
        else:
            print(s)



if __name__=='__main__':
    current = datetime.datetime.now()
    t1=threading.Thread(target=hours, args=[current])
    t2=threading.Thread(target=minutes, args=[current])
    t3=threading.Thread(target=seconds, args=[current])

    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()



    




