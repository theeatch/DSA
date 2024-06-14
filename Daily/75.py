from pysvt import test

d ={
    "i": [[[2,0,2,1,1,0]],[[2,0,1]]],
    "o": [[0,0,1,1,2,2],[0,1,2]]
}

@test(data=d, method="sortColors")

class Solution(object):
    def sortColors(self, nums: list[int]) -> list[int]:
        i = 0
        j = len(nums) - 1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            else:
                k += 1
        return nums