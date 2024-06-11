from pysvt import test

d= {
    "i": [[["cat","bat","rat"],"the cattle was rattled by the battery"],[["a","b","c"],"aadsfasf absbs bbab cadsfafs"], [["a","aa","aaa","aaaa"],"a aa a aaaa aaa aaaa aa aaaaaa bbb baba ababa"],[["catt","cat","bat","rat"],"the cattle was rattled by the battery"]],
    "o": ["the cat was rat by the bat","a a b c","a a a a a a a a bbb baba a","the cat was rat by the bat"]
}

@test(data=d, method="replaceWord")

class Solution(object):
    def replaceWord(self, dictionary: list[str], sentence: str) -> str:
        sentence = sentence.split()
        dictionary.sort(key=len)
        for index, i in enumerate(sentence):
            for word in dictionary:
                if i.startswith(word):
                    sentence[index] = word
                    break
        return " ".join(sentence)
        