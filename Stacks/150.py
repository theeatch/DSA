from pysvt import test

test = {
    "i" : [[["2","1","+","3","*"]],[["4","13","5","/","+"]],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]],
    "o" : [[9],[6],[22]],
}

@test(data=test, method="evalRPN")
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for char in tokens:
            if char in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if char == '+':
                    stack.append(b + a)
                elif char == '-':
                    stack.append(b - a)
                elif char == '*':
                    stack.append(b * a)
                elif char == '/':
                    stack.append(int(b / a)) 
            else:
                stack.append(int(char)) 
        return stack[-1]