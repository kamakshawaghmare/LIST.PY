# num=int(input("enter the number:"))
# sum=0
# i=1
# while num>i:
#     if num%i==0:
#         sum=sum+i
#         num=num//10
#     print(sum,"perfect number")
# if num==sum:
#     print("perfect number")
# i=i+1

num=int(input("enter:"))
i=1
sum=0
while num>=i:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("perfect number")
else:
    print("not perfect")