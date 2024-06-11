from pysvt import test

d={
    "i": [[[2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]],[[28,6,22,8,44,17],[22,28,8,6]]],
    "o": [[2,2,2,1,4,3,3,9,6,7,19],[22,28,8,6,17,44]]
}

@test(data=d, method="relativeSortArray")

class Solution(object):
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []
        for i in arr2:
            res += [i]*arr1.count(i)
        for i in sorted([i for i in arr1 if i not in arr2]):
            res.append(i)
        return res