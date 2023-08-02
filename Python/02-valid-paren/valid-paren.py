class Solution:
    def is_open(self, ch: str) -> bool:
        return ch in ["(", "{", "["]

    def check_if_valid(self, ch: str, stack: List[str]) -> bool:
        if self.is_open(ch):
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

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if not self.check_if_valid(ch, stack):
                return False
        return len(stack) == 0
