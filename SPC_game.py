import random
while True:
    computer=random.choice([1,2,3])
    youstr=input("enter your choise: ")
    youdict={"stone":1,"paper":2,"ciser":3}
    revdict={1:"stone",2:"paper",3:"ciser"}
    you=youdict[youstr]

    print("computer choise:",revdict[computer])
    # print("your choise:",revdict[you])

    if (computer==you):
        print("it is draw")
    else:
        if (computer==1 and you==2):
            print("you win")
        elif (computer==1 and you==3):
            print("you lose")
        elif (computer==2 and you==3):
            print("you win")
        elif (computer==2 and you==1):
            print("you lose")
        elif (computer==3 and you==1):
            print("you win")
        elif (computer==3 and you==2):
            print("you lose")
        else:
            print("something is worng")
    print("do you want to play again")
    a=input("enter your choice: ")
    if a=="no":
        print("thankyou...")
        break
   
    