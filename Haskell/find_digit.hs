{-
 - Given a number N, find the number of positions in N such that the digit at
 - that position divides N.
 -
 - Input is taken from standard input. The first number is the number of inputs
 - after.
 -}
find_digits num digits =
    if num == 0
        then 0 
        else
            if digits == 0 then 0
            else
                let digit = digits `mod` 10
                    rest = digits `div` 10
                    quotient = (if digit /= 0
                                    then num `div` digit
                                    else num)
                    remainder = (if digit /= 0
                                    then num `mod` digit
                                    else num)
                    flag = (if remainder == 0 then 1 else 0)
                in
                    if quotient == 0
                        then flag
                        else flag + find_digits num rest


doUntil times = do
    input <- getLine
    let left = times - 1
    let num = read input :: Integer
    let digits = find_digits num num
    print digits
    if left > 0
        then doUntil left
        else return ()

main :: IO ()
main = do
    input <- getLine
    let times = read input :: Integer
    doUntil times
