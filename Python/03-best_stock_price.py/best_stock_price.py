from typing import List

def getMaxForRange(prices: List[int]) -> int:
    result = [ 0 ]
    print(f"DBG: len(prices) = {len(prices)}")
    for i in range(len(prices) - 1, -1, -1):
        print(f"DBG:    i = {i}, prices[i] = {prices[i]}")
        if prices[i] > result[0]:
            result.insert(0, prices[i])
        else:
            result.insert(0, result[0])
    print(f"DBG: result = {str(result)}")
    return result

def maxProfit(prices: List[int]) -> int:
    maxlist = getMaxForRange(prices)
    curr = 0
    for i in range(len(prices) - 1):
        if maxlist[i + 1] - prices[i] > curr:
            curr = maxlist[i + 1] - prices[i]
    return curr

def test4():
    prices = [1, 6, 3]
    exp = 5
    result = maxProfit(prices)
    print(f"TEST4: exp = {exp} -- actual = {result}")

if __name__ == "__main__":
    print("Running TESTS:")
    test4()
