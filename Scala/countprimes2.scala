/* count_primes */

object Sieve {
    def sieve( xs: Stream[Int] ):Stream[Int] =
        xs match {
            case first #:: rest => first #:: sieve( rest.filter( x => x % first != 0 ) )
            case _ => Stream.empty
        }
 
    def main(args: Array[String]) {
        val number = readInt()
        val primes = sieve( List.range(2, number).toStream ).toList
        println( primes.length )
    }
}

/*
 * Performance numbers:
 *
 * 100000000 => ????
 */
