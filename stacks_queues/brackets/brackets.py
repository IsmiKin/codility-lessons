# A string S consisting of N characters is considered to be properly nested if
# any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# tring S consists only of the following characters: "(", "{", "[", "]", "}"
# and/or ")".

from stack import Stack

OPEN_SYMBOL = ['(', '[', '{']
CLOSE_SYMBOL_RELATION = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def is_properly_nested(string):
    stack = Stack()

    for character in string:
        if character in OPEN_SYMBOL:
            stack.push(character)
        else:
            try:
                if CLOSE_SYMBOL_RELATION[character] == stack.pop():
                    continue
                else:
                    return False
            except IndexError:
                return False

    return True
