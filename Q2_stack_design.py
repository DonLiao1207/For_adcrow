class StackPeekMinimum:
    def __init__(self):
        self.stack = []
        self.min_in_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_in_stack:
            self.min_in_stack.append(min(x, self.min_in_stack[-1]))
        else:
            self.min_in_stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_in_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peek_minimum(self) -> int:
        return self.min_in_stack[-1]


if __name__ == "__main__":
    pystack = StackPeekMinimum()
    pystack.push(-1)
    pystack.push(-6)
    pystack.push(5)
    pystack.push(-10)
    stack_minimum = pystack.peek_minimum()
    print(f'stack content: {pystack.stack}')
    print(f'stack minimum: {stack_minimum}')
    stack_top_1 = pystack.top()
    print(f'stack top before pop: {stack_top_1}')
    pystack.pop()
    stack_top_2 = pystack.top()
    print(f'stack top after pop: {stack_top_2}')
    stack_minimum = pystack.peek_minimum()
    print(f'stack minimum: {stack_minimum}')
    '''
    output:
    stack content: [-1, -6, 5, -10]
    stack minimum: -10
    stack top before pop: -10
    stack top after pop: 5
    stack minimum: -6
    '''
