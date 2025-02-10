arr=[1,1,0,0,1,1,1,0,0,1,1]

i=maxCount=count=0

for j in range(len(arr)):
    if(arr[j]!=1):
        count=j-i
        maxCount=max(count,maxCount)
        i=j+1

print(maxCount)