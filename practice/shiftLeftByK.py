n=7

arr=[1,2,3,4,5,6,7]

k = 12
newarr=[]
if(k>n):
    k=k%n

for i in range(k):
    newarr.append(arr[i])


for i in range(n-k):
    arr[i]=arr[i+k]

for i in range(k):
    arr[n-k+i] = newarr[i]


print(arr)
    

