num=int(input("enter the number:"))
orig=num
sum=0
while num>0:
   sum=sum+num%10
   num=num//10
print(sum)
if orig%sum==0:
    print("harshad number")
else:
    print("not an harshad number")

