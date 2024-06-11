from pysvt import test

d ={
    "i": [[[1,1,4,2,1,3]],[[5,1,2,3,4]],[[1,2,3,4,5]]],
    "o": [2,5,0]
}

@test(data=d, method="heightCheck")

class Solution(object):
    def heightCheck(self, heights: list[int]) -> int:
        res=0
        newnums = heights.copy()
        heights.sort()
        for i in range(len(heights)):
            if heights[i] != newnums[i]:
                res+=1
        return res
            

            