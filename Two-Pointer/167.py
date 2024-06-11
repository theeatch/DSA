from pysvt import test

d = {
    "i": [[[2, 7, 11, 15], 9], [[2, 3, 4], 6], [[-1, 0], -1]],
    "o": [[1, 2], [1, 3], [1, 2]]
}


@test(data=d, method="twoSumSort")

class Solution(object):
    def twoSumSort(self, nums: list[int], target) -> list[int]:
        # create a dictionary to store the index of the numbers
        d = {}
        # iterate though the numbers with index
        for i, n in enumerate(nums):
            # if the difference between the target and the number is in the dictionary
            if target - n in d:
                # answer return
                return [d[target - n]+1, i+1]
            # else add the number in the dictionary
            d[n] = i
        return []