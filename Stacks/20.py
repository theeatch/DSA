from pysvt import test

data = {
    "i": [["()"],["()[]{}"],["(]"]],
    "o": [True,True,False],
}

@test(data=data, method="isValid")

class Solution:
    def isValid(self, s:str) ->bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return stack == []