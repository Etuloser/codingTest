"""
Q3
Implement a stack that accepts the following commands and performs the operations
described:
push v: Push integer v onto the top of the stack
pop: Pop the top element from the stack
inc i v: Add v to each of the bottom i elements of the stack
After each operation, print the value at the top of the stack. If the stack is empty, print the
string 'EMPTY'.
"""


class MyStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, v: int):
        self.stack.append(v)
        print(self.stack[-1])

    def pop(self):
        self.stack.pop()
        if self.stack:
            print(self.stack[-1])
        else:
            print("EMPTY")

    def inc(self, i: int, v: int):
        if self.stack:
            for j in range(min(i, len(self.stack))):
                self.stack[j] += v
            print(self.stack[-1])
        else:
            print("EMPTY")


def process_commands(commands) -> list:
    stack = MyStack()

    for cmd in commands:
        if cmd[0] == "push":
            stack.push(int(cmd[1]))
        elif cmd[0] == "pop":
            stack.pop()
        elif cmd[0] == "inc":
            stack.inc(int(cmd[1]), int(cmd[2]))

    return stack.stack
