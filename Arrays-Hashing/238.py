from pysvt import test
from functools import reduce 

d = {
    "i": [[[1,2,3,4]], [[-1,1,0,-3,3]]],
    "o": [[24,12,8,6], [0,0,9,0,0]]
    }


@test(data=d, method="productExceptSelf")
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # count the number of zeros in the list
        count = nums.count(0)
        # if there are more than 1 zeros then return list of zeros (because answer for all product will be 0)
        if count > 1:
            return [0 for i in range(len(nums))]
        # else find product with reduce (loop over elements and multiply but if element == 0  then keep previous product), 1 is inital val of acc
        product = reduce(lambda acc,x: acc if x==0 else acc * x, nums, 1)
        return list(
            # loop over elements and if element is 0 then return product (cannot divide by 0) 
            # else if count is 0 then return product//element (no 0 elements) 
            # else return 0 (elements other than 0 will have product 0)
            map(lambda x: product if x == 0 else (product // x if count <= 0 else 0), nums)
        )