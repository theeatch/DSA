class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen=''
        for char in s:
            if char not in seen:
                seen+=char
                longest = max(longest, len(seen))
            else:
                seen = seen[seen.index(char) +1:] + char
        return longest