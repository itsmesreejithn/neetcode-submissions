class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for token in tokens:
            if token not in "+-*/":
                self.stack.append(int(token))
            else:
                b = self.stack.pop()
                a = self.stack.pop()

                if token == "+":
                    self.stack.append(a+b)
                if token == "-":
                    self.stack.append(a-b)
                if token == "*":
                    self.stack.append(a*b)
                if token == "/":
                    self.stack.append(int(a/b))
            
        return self.stack[0]