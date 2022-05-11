i=1
while i<=500:
    a=i%10
    b=i//10
    c=b%10
    d=b//10
    e=d%2==0
    if a%2==0 or b%2==0 or c%2==0 or d%2==0 and e%2==0:
        print(i)    
    i=i+1
