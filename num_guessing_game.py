import random
com=random.randint(1,100)
a=int(input("enter the no.: "))
count=0
while True:
    if a==com:
        print("you guess the correct no.",a)
        break
    elif a>com:
        print("guess lower")
        a=int(input("enter the no.: "))
        count+=1
    elif a<com:
        print("guess higher")
        a=int(input("enter the no.: "))
        count+=1
print("you guess the no. in attempt: ",count)
print("thanks for playing....")
    
