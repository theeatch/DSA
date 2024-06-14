from pysvt import test

d={
    "i" : [[[1,2,2]],[[3,2,1,2,1,7]],[[2,2,2,2,0]]],
    "o" : [1,6,6]
}

@test(data=d, method="minMove")

class Solution:
    def minMove(self, nums: list[int]) -> int:
        nums.sort()
        i=1
        highest=nums[0]
        moves=0
        while i < len(nums):
            if nums[i] <= highest:
                moves+= highest - nums[i] + 1
                nums[i] += highest - nums[i] +1
                print(nums)
            highest = nums[i]
            i+=1
        return moves