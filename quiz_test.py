ques1="what is the capital of india ?"
ans1="new delhi"
ques2="what is the sum of 34+56 ?"
ans2="90"
ques3="which language used to create this program ?"
ans3="python"
ques4="how many states in india?"
ans4="28"
ques5="what is the capital of uttar pradesh"
ans5="lucknow"
score=0
print("what is the capital of india ?")
a=input("enter the answer: ")
if a==ans1:
    print("correct answer")
    score+=1
else:
    print("wrong answer")
print("what is the sum of 34+56 ?")
b=input("enter the answer: ")
if b==ans2:
    print("correct answer")
    score+=1
else:
    print("wrong answer")
print("which language used to create this program ?")
c=input("enter the answer: ")
if c==ans3:
    print("correct answer")
    score+=1
else:
    print("wrong answer")
print("how many states in india?")
d=input("enter the answer: ")
if d==ans4:
    print("correct answer")
    score+=1
else:
    print("wrong answer")
print("what is the capital of uttar pradesh")
e=input("enter the answer: ")
if e==ans5:
    print("correct answer")
    score+=1
else:
    print("wrong answer")
if score==5:
    print("excellent")
elif score==4:
    print("good")
elif score==3:
    print("average")
elif score==2:
    print("do better")
else:
    print("poor")
print("your score is: ",score)