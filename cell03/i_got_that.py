b = input("What you gotta Say? : ")
c = ["STOP"]
while b in c:
    if b != c:
        continue
    print("I got that, Anything else?")
    if b == c:
        break
