from pysvt import test


d = {"i": [["anagram", "nagaram"], ["rat", "car"], ["ab", "a"]], "o": [True, False, False]}


@test(data=d, method="isAnagram")
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)