import random
i=1
a=random.randint(0,9)
print("You have total 5 chances to guess the number(between 0 and 9)")
while i<=5:
    b=int(input("Guess the number\t"))
    if a==b:
        print("Correct guess!")
        break
    else:
        if a<b:
            print("entered number is more than actual number")
        else:
            print("entered number is less than actual number")
        i=i+1