import Prelude
import System.Environment

main :: IO ()
main = 
    let sieve(p:xs) = p : sieve [ x | x <- xs, x `mod` p > 0 ]
        in print $ show $ take 1000 (sieve [2..])
        
