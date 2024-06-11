from pysvt import test

d ={
    "i":[["A man, a plan, a canal: Panama"],["race a car"],[""]],
    "o":[True, False, True]
}

@test(data=d, method="validPalin")

class Solution(object):
    def validPalin(self, s: list[str]) -> bool:
        str = ''.join(e for e in s if e.isalnum()).lower()
        return str == str[::-1]