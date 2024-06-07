from pysvt import test

d = {
    "i": [
        [["eat", "tea", "tan", "ate", "nat", "bat"]],
        [[""]],
        [["a"]]
    ],
    "o": [
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        [[""]],
        [["a"]]
    ]
}


@test(data=d,method="group_anagram")

class Solution(object):
    def group_anagram(self, strs: list[str]) -> list[list[str]]:
        # create empty dict
        anagrams_dict = {}
        # loop through list of strings
        for word in strs:
            # sort the word (letters of word in sorted e.g. -  tea=aet)
            sorted_word = ''.join(sorted(word))
            # if this sorted word is in the dictionary then append the word as value to dict key of sorted word.
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                # else create a new key with sorted word and value as list with word
                anagrams_dict[sorted_word] = [word]
        # return the dict values as list (values contains list of anagrams of that sorted word)
        return list(anagrams_dict.values())