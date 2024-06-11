from pysvt import test

d = {
    "i": [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]],
    "o": [[[-1,-1,2],[-1,0,1]],[[]],[[0,0,0]]]
}

@test(data=d, method="threeSum")

class Solution(object):
    def threeSum(self, nums: list[int]) -> list[int]:
        # initialize the output list and traverse the list with 3 pointers, i at the start, j at i+1 and k at the end and find sum = 0 add to set.
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output
