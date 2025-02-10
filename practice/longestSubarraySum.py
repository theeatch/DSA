def longestSubarrayWithSumK(a: [int], k: int) -> int:
    maxCount=0
    i=j=0
    windowSum=a[0]
    while(j<len(a)):
        while(windowSum>k):
            windowSum-=a[i]
            i+=1
        if(windowSum==k):
            maxCount=max(maxCount, j-i+1)
        j+=1
        if(j<len(a)):
            windowSum+=a[j]
        

    # Write your code here
    return maxCount


# only positives allowed in array.
'''
Problem statement
You are given an array 'a' of size 'n' and an integer 'k'.



Find the length of the longest subarray of 'a' whose sum is equal to 'k'.



Example :
Input: "n" = 7 "k" = 3
"a" = [1, 2, 3, 1, 1, 1, 1]

Output: 3

Explanation: Subarrays whose sum = "3" are:

[1, 2], [3], [1, 1, 1] and [1, 1, 1]

Here, the length of the longest subarray is 3, which is our final answer.
'''