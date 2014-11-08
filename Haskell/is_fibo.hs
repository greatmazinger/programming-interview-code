{- N is a Fibonacci number iff
 -     (5*N^2 + 4) or (5*N^2 – 4)
 - is a square number.
 -}

-- binsearch
--     Finds mid such that mid^2 == num
--     and low <= mid <= high
binsearch :: Integer -> Integer -> Integer -> Bool
binsearch low high num = 
    let mid = ((high + low) `div` 2)
        midsquare = mid * mid
    in
        if low > high
            then False
            else (if num == midsquare
                      then True
                      else (if num < midsquare
                                then (binsearch low (mid - 1) num)
                                else (binsearch (mid + 1) high num)))

-- binsearch2
--     A version of binsearch that uses guards instead of nested loops.
binsearch2 :: Integer -> Integer -> Integer -> Bool
binsearch2 low high num
    | low > high = False 
    | num == midsquare = True
    | num < midsquare = binsearch low (mid -1) num
    | otherwise = binsearch (mid + 1) high num
    where
        mid = ((high + low) `div` 2)
        midsquare = mid * mid

-- Use the binsearch2 version instead of binsearch
is_square :: Integer -> Bool
is_square num = binsearch2 1 num num

is_fibo :: Integer -> Bool
is_fibo num = let part1 = 5 * (num^2)
                  alt1 = part1 + 4
                  alt2 = part1 -4
              in if is_square alt1
                     then True
                     else is_square alt2

doUntil times = do
    input <- getLine
    let left = times - 1
    let num = read input :: Integer
    if is_fibo num
        then putStrLn "Fibo"
        else putStrLn "NotFibo"
    if left > 0
        then doUntil left
        else return ()

main :: IO ()
main = do
    input <- getLine
    let times = read input :: Integer
    doUntil times
