n=int(input())
count=25
while(count>n):
    n = n+1
    if(n<count):
        print("Inside The Loop, My variable is", n)
    elif(n>count):
        print("Error")
    else:
        print("Inside The Loop, My variable is 25\n""End Program")