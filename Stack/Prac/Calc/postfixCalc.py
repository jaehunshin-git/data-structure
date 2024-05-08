class PostfixCalculatorArray:
    def __init__(self):
        self.stack = []

    def calculate(self, expression):
        for token in expression:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()

                if token == '+':
                    self.stack.append(operand1 + operand2)
                elif token == '-':
                    self.stack.append(operand1 - operand2)
                elif token == '*':
                    self.stack.append(operand1 * operand2)
                elif token == '/':
                    self.stack.append(operand1 / operand2)

        return self.stack.pop()


# Example usage
expression = "91-2/121+*-1-"
# expression = str(input())
calculator = PostfixCalculatorArray()
result = calculator.calculate(expression)
print("Result:", result)
