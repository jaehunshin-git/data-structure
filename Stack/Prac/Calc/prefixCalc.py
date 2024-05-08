class PrefixCalculatorArray:
    def calculate(self, expression):
        stack = []
        operators = set(['+', '-', '*', '/'])

        for char in reversed(expression):  # 입력 문자열을 거꾸로 읽음
            if char.isdigit():
                stack.append(int(char))
            elif char in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()

                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 / operand2)

        return stack.pop()


# Example usage
# expression = "-*-567*42"
expression = str(input())
calculator = PrefixCalculatorArray()
result = calculator.calculate(expression)
print("Result:", result)
