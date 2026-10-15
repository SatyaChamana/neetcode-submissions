class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
                # print(stack)
            elif s == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
                # print(stack)
            elif s == "*":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
                # print(stack)
            elif s == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int((b)/a))
                # print(stack)
            else:
                stack.append(int(s))

        return stack.pop()

            