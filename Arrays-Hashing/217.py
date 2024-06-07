from pysvt import test

d = {
    "i": [[[1, 2, 3, 1]], [[1, 2, 3, 4]], [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]],
    "o": [True, False, True],
}


@test(data=d, method="containsDuplicate")
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = dict.fromkeys(nums, 0)

        for i in nums:
            # if the number is already in the dictionary then increment and if any key has val 2 return true return True
            d[i] += 1
            if d[i] >= 2:
                return True
        return False