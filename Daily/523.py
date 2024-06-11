from pysvt import test
from functools import reduce
from itertools import count
d = {
    "i": [[[23,2,4,6,7], 6], [[23,2,6,4,7], 6], [[23,2,6,4,7], 13],[[23,2,4,6,6],7],[[0],1],[[23,6,9],6],[[1,0],2],[[5,0,0,0],3]],
    "o": [True, True, False, True, False, False, False, True]
}

@test(data=d, method="continuousSubSum")

class Solution(object):
    def continuousSubSum(self, nums: list[int], k: int) ->  bool:
        map = {0: -1}  
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False  