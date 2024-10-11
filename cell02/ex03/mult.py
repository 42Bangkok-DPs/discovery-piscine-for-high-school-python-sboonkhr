
#!/usr/bin/env python3
x=int(input())
y=int(input())
z=x*y
if z > 0:
  print (x ,"x", y ,"=", z,
         "The result is positive")
elif z < 0:
  print (x ,"x", y ,"=" ,z,
         "The result is negative")
else:
  print (x ,"x" ,y ,"=", z,
         "The result is both positive and negative")
