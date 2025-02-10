class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        dict={}
        res = 0
        for right in range(len(s)):
            dict[s[right]] = 1 + dict.get(s[right], 0)
            
            while (right - left + 1) - max(dict.values()) > k:
                dict[s[left]] -=1
                left +=1
            res = max(res, right-left+1)
        return res
            