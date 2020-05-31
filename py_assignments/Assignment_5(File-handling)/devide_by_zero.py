
def Process(devidend, divider):
    try:
        ans=devidend/divider
        print("Answer is ", ans)
    except:
        print("devide by zero error.")


num1=int(input("Enter the dividend: "))
num2=int(input("Enter the divider: "))

Process(num1, num2)
