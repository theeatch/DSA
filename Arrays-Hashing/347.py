from pysvt import test


d ={
    "i":[[[1,1,1,2,2,3],2],[[1],1]],
    "o":[[1,2],[1]]
}

@test(data=d, method="topkfrequent")

class Solution(object):
    def topkfrequent(self, nums: list[int], k: int) -> list[int]:
        d=dict.fromkeys(nums,0)
        for i in nums:
            # enter num and its occurence in dictionary
            d[i]+=1
            # sort the dictionary by value and return the keys
        return sorted(d, key=d.get, reverse = True)[:k]
