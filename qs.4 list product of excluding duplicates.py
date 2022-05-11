# List product excluding duplicates.
    # List = [6,1,3,5,6,3,1]
    # Output: 60

# a=[6,1,3,5,6,3,1]
# i=0
# product=1
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         product=product*(a[i])
#     i=i+1
# print(product)


# a=[[0],[5,7],[9,11],[13,15,17]]
# p=len(a[0])
# r=len(a[1])
# i=len(a[2])
# t=len(a[3])
# mx=max(p,r,i,t,)
# mi=min(p,r,i,t,)
# print(mx)
# print(mi)

a=[[0],[5,7],[9,11,12,65],[13,15,17]]
print(len(a))
p=len(a[0])
r=len(a[1])
i=len(a[2])
t=len(a[3])
# print(a[2])
print(max(a))
print(min(a))