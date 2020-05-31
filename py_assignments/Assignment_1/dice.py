import random
i=1
while i>0:
    print("Output after rolling the dice:")
    print(random.randint(1,6))
    print("\n")
    a=input("Do you want to roll it again? y or n\n")
    if a=='n':
        break
    
