from pysvt import test

d = {
    "i": [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]],
    "o": [[0, 1], [1, 2], [0, 1]]
}


@test(data=d, method="twoSum")

class Solution(object):
    def twoSum(self, nums: list[int], target) -> list[int]:
        # create a dictionary to store the index of the numbers
        d = dict.fromkeys(nums, 0)
        # iterate though the numbers with index
        for i, n in enumerate(nums):
            # if the difference between the target and the number is in the dictionary
            if target - n in d:
                # answer return
                return [d[target - n], i]
            # else add the number in the dictionary
            d[n] = i
        return []