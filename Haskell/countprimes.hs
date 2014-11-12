-- count_primes
--    This is probably non-idiomatic Haskell (aka n00b Haskell)
--    but still just learning the language. If there are things
--    here that Shouldn't Be Done, please let me know. I may or
--    may not change it. :)
import qualified Data.Vector as V

sieve :: Integer -> Integer -> Integer -> V.Vector Bool -> V.Vector Bool
sieve current endsqrt number flags = 
    if current > endsqrt then
        flags
    else
        if flags V.! (fromIntegral current) then
            let
                flags3 = sieve (current + 1) endsqrt number flags2
            in
                flags3
        else
            let
                flags3 = sieve (current + 1) endsqrt number flags
            in
                flags3
    where
        flags2 = flags V.// [ (fromIntegral i, False) |
                              step <- [0..(((number-start) `div` current) + 1)],
                              let i = start + (current * step),
                              i <= number ]
        start = current * current

-- Version of sieve that uses guards
sieve2 :: Integer -> Integer -> Integer -> V.Vector Bool -> V.Vector Bool
sieve2 current endsqrt number flags
    | current > endsqrt = flags
    | flags V.! (fromIntegral current) =
            sieve (current + 1) endsqrt number flags2
    | otherwise =
            sieve (current + 1) endsqrt number flags
    where
        flags2 = flags V.// [ (fromIntegral i, False) |
                              step <- [0..(((number-start) `div` current) + 1)],
                              let i = start + (current * step),
                              i <= number ]
        -- This is probably where I can improve things. The `div` calculation
        -- is affecting the performance. Not sure how to use the list comprehension
        -- such that I don't need to calculate.
        start = current * current

main :: IO ()
main = do
    input <- getLine
    let number = read input :: Integer
    let endsqrt = ceiling $ sqrt (fromIntegral number)
    let flags = (V.fromList [ True | x <- [0..number] ]) V.// [ (0, False), (1, False) ]
    let prime_flags = sieve 2 endsqrt number flags
    let count = V.length $ V.filter (\a -> a) prime_flags
    print count

-- Performance numbers:
--
-- 100000000
-- 5761455
--
-- real    54m5.325s
-- user    53m56.066s
-- sys     0m3.425s
--
-- NOTE: The performance is rather bad, so I'm obviously doing something really wrong here.
