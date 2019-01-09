# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    OPEN_SYMBOL = ['(', '[', '{']
    CLOSE_SYMBOL_RELATION = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items)-1]

        def size(self):
            return len(self.items)

    stack = Stack()

    for character in S:
        if character in OPEN_SYMBOL:
            stack.push(character)
        else:
            try:
                if CLOSE_SYMBOL_RELATION[character] == stack.pop():
                    continue
                else:
                    return 0
            except IndexError:
                return 0

    return 1
