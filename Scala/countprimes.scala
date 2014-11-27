/* count_primes */

import scala.io.StdIn.readInt
import scala.math.sqrt

object Sieve {
    def main(args: Array[String]) {
        val number = readInt()
        val flags = Array.fill(number + 1)( true )
        flags(0) = false
        flags(1) = false
        for (x <- Range(2, sqrt(number).toInt + 1)) {
            if (flags(x)) {
                var y = x * x
                while ((y <= number) && (y > x)) {
                    flags(y) = false
                    y = y + x
                }
            }
        }
        val total = flags.foldLeft(0)( (x: Int, f: Boolean) => if (f) (x + 1) else x )
        println( total )
    }
}

/*
 * Performance numbers:
 * 
 * 1000000
 * 78498
 * 
 * real    0m2.203s
 * user    0m1.358s
 * sys     0m0.304s
 * 
 * 100000000
 * 5761455
 * 
 * real    0m6.833s
 * user    0m6.559s
 * sys     0m0.407s
 */
