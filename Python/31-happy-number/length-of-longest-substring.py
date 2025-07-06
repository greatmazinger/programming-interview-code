def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    longest = 1
    current = 1
    left = 0
    right = 1
    letters = set(s[0])
    while right < len(s):
        if s[right] in letters:
            # So there's a dupe. We need to move the left past the dupe.
            while s[left] != s[right]:
                letters.remove(s[left])
                left += 1
                print("{} - {}".format(s[left], s[right]))
            left += 1
            # Found the dupes:
            # Assert s[left] == s[right]
            # But: left < right
            current = (right - left) + 1
        else:
            current += 1
            letters.add(s[right])
            if current > longest:
                longest = current
        right += 1
    return longest
