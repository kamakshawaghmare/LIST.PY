# x=int(input("enter the number:"))
# for y in range(1,11):
#     print(x*y)

# # x=int(input("enter the number:"))
# y=1
# while y<=10:
#     print(x*y)
#     y=y+1

# a=float(input("enter the number:"))
# b=float(input("enter the number:"))
# while a<=b:
#     i=1
#     while i<=10:
#         print(a,"*",i,"=",a*i)
#         i=i+1
#     print()
#     a=a+1

for i in range(1,11,1):
    for j in range(i,101,10):
        print(j,end=" ")
    print()