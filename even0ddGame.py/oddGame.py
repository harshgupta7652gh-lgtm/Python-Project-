import random
while True:
    a=random.randint(0,9)
    while True:
        user=input("enter your choice: ")
        if user=='even':
            print("c0mputer choice: 0dd")
            break
        elif user=='0dd': 
            print("c0mputer ch0ice: even")
            break
        else: 
            print("invalid ch0ice")
    while True:
        b=int(input("enter the no.: "))
        if b<0 and b>9:
            print("choice between 0-9")
        else:
            break
    print("c0mputer enter: ",a)
    sum=a+b
    if sum%2==0:
        if user=='even':
            print("you win")
        else:
            print("you l0se")
    else:
        if user=='0dd':
            print("y0u win")
        else:
            print("y0u l0se")
    p=input("D0 y0u play again: ")
    if p=='n0':
        print("Thanksy0u....")
        break
    
