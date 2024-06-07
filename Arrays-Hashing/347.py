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
            # zip the dictionary into tuple, lambda functions describes sort according to value , in descending order
        res = sorted(zip(d.keys(),d.values()), key=lambda x: x[1], reverse=True)
        # return the first k elements (x[0] is the key of dictionary)
        return list(map(lambda x: x[0], res[:k]))