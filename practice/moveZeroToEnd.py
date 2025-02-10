arr=[1,0,2,3,2,0,0,4,5,1]

n = len(arr)
i=0
for j in range(n):
    if arr[j]==0:
        i=j
        break

for j in range(i+1,n):
    if(arr[j]!= 0):
        arr[i]=arr[j]
        arr[j]=0
        i+=1

print(arr)