from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    rtotal = Counter(ransomNote)
    mtotal = Counter(magazine)
    for ch in rtotal.keys():
        if ch not in mtotal or rtotal[ch] > mtotal[ch]:
            return False
    return True

def test1():
    print("Running TEST 1:")
    ransom_note = "aaa"
    magazine = "abaaac"
    expected = True

    assert expected == canConstruct(ransom_note, magazine)
    print(" - TEST 1 Done")

if __name__ == "__main__":
    test1()
