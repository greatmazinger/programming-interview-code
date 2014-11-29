/* Longest increasing common subsequnce problem 
 * - this version uses the n*log n algorithm.
 */
object LICS {

    def main(args: Array[String]) {
        var seq: Vector[Int] = get_input().toVector
        var lics = get_LICS( seq )
        println(lics)
        println(lics.length)
    }

    def get_LICS(seq: Vector[Int]): List[Int] = {
        var M: Array[Int] = Range(0, (seq.length + 1)).toArray
        //   M[j] = stores the index k of the smallest value X[k] s.t.
        //     there is an increasing subsequence of length j ending at X[k] on the range k ≤ i
        //     -- (note we have j ≤ k ≤ i here, because
        //        j represents the length of the increasing subsequence
        //        k represents the index of its termination
        var P: Array[Int] = Array.fill(seq.length)(-1)
        //   P[k] = stores the index of the predecessor of X[k] in the longest increasing subsequence ending at X[k]
        var L: Int = 0    // length of longest common subsequence found so far
        // Let X = seq:
        //  at any point in the algorithm, the sequence
        //         X[M[1]], X[M[2]], ..., X[M[L]]
        //  is nondecreasing.
        //  Source: http://en.wikipedia.org/wiki/Longest_increasing_subsequence
        for (x <- Range(0, seq.length)) {
            var longest = seq(x) :: List.empty
            var lo: Int = 1
            var hi: Int = L
            while (lo <= hi) {
                val mid = (lo + hi) / 2
                if (seq( M(mid) ) < seq(x)) {
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }
            // On first through this loop, goes straight here.
            val newL = lo
            // The predecessor of X[i] is the last index of the subsequence of length (newL - 1)
            P(x) = M(newL - 1)
            M(newL) = x
            if (newL > L) {
                L = newL
            }
        }
        // Recreate the longest increasing subsequence
        var lics = new Array[Int](L)
        var k = M(L)
        for (x <- ((L - 1) to 0 by -1)) {
            lics(x) = seq(k)
            k = P(k)
        }
        return lics.toList
    }

    def get_input() : List[Int] = {
        var seq: List[Int] = List.empty
        for (ln <- io.Source.stdin.getLines) {
            seq = ln.toInt :: seq
        }
        seq = seq.reverse
        return seq
    }

}
