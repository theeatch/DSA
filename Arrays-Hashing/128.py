from pysvt import test

data = {
    "i": [[[100,4,200,1,3,2]], [[0,3,7,2,5,8,4,6,0,1]]],
    "o": [4, 9]
    }  

@test(data=data, method="longestConsecutive")

class Solution: 
    def longestConsecutive(self, nums: list[int]) -> int:
        # create a set (set removes duplication and sorts the elements)
        nums = set(nums)
        max_len = 0
        for num in nums:
            # if the number - 1 is not in the set then it is the start of the sequence
            if num - 1 not in nums:

                current_num = num
                current_len = 1
                # if the next consecutive number is in the set then increment the length of the sequence
                while current_num + 1 in nums:
                    current_num += 1
                    current_len += 1
                max_len = max(max_len, current_len)
        return max_len