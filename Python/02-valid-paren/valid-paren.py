from typing import List

def is_open(ch: str) -> bool:
    return ch in ["(", "{", "["]

def check_if_valid(ch: str, stack: List[str]) -> bool:
    if is_open(ch):
        stack.append(ch)
        return True
        # If the new character is an open, then adding to the stack is always valid.
    # So this is a closing paren. We have to check to see if it matches the top of the stack
    result = False
    if len(stack) > 0:
        if ch == ")":
            result = (stack[-1] == "(")
        elif ch == "}":
            result = (stack[-1] == "{")
        elif ch == "]":
            result = (stack[-1] == "[")

        if result:
            stack.pop()
    return result

def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if not check_if_valid(ch, stack):
            return False
    return len(stack) == 0

def test1():
    print("Running TEST 1:")
    teststr = "()"
    assert isValid(teststr)
    print("  -> TEST 1 passed.")

def test2():
    print("Running TEST 2:")
    teststr = "(){"
    assert not isValid(teststr)
    print("  -> TEST 2 passed.")

def test3():
    print("Running TEST 3:")
    teststr = "]{}"
    assert not isValid(teststr)
    print("  -> TEST 3 passed.")

def test4():
    print("Running TEST 4:")
    teststr = "(){}[]((({}{}[])))"
    assert isValid(teststr)
    print("  -> TEST 4 passed.")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
