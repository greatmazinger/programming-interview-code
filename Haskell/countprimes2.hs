-- count_primes

sieve (p:xs) =  p : sieve [ x | x <- xs, x `mod` p > 0 ]
sieve ([])   =  []
        
main :: IO ()
main = do
    input <- getLine
    let number = read input :: Integer
    let primes = [ x | x <- sieve( [2..number] ) ]
    print $ length primes

-- Performance numbers:
--
-- 100000000
-- NOTE: The performance is rather bad, so I'm obviously doing something really wrong here.
