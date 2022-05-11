# i=1
# while i<=100:
#     if i%3==0 and i%5==0:
#         print("navgurukul")
#     elif i%3==0:
#         print("nav")
#     else:
#         print("gurukul")
#     print(i)
#     i=i+1
#from tkinter import Y


i=1
while i<=100:
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul") 
    elif i%7==0 and i%3==0:
        print("navgurukul") 
    else:
        print(i) 
    i+=1         