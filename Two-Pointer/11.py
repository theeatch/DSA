from pysvt import test

d={
    "i": [[[1,8,6,2,5,4,8,3,7]],[[1,1]],[[2,3,4,5,18,17,6]]],
    "o": [49,1,17],
}

@test(data=d, method="maxArea")

class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        max_area=0
        k = len(height)-1
        j=0
        for i in range(len(height)):
            max_area = max(max_area, abs(min(height[j], height[k])*(k-j)))
            if height[j] > height[k]:
                k -= 1
            else:
                j += 1
        return max_area