/* Longest increasing common subsequnce problem */
object LICS2 {

    def main(args: Array[String]) {
        var seq: Vector[Int] = get_input().toVector
        var lics = get_LICS( seq )
        println(lics)
        println(lics.length)
    }

    def get_LICS(seq: Vector[Int]): List[Int] = {
        // This might be unnecessarily complex, but I'll go with it for now.
        // newseq is a vector s.t.
        //     newseq(i) => LICS that ends at seq(i)
        //                  -- must use seq(i)
        var lics = seq(0) :: List.empty
        var newseq: Vector[ List[Int] ] = (seq(0) :: List.empty) +: Vector.fill(seq.length - 1)( List.empty )
        // Note: +: is the Vector prepend operator. It's the same for list, but we're prepending
        //       to a Vector here.
        for (x <- Range(1, seq.length)) {
            // Look for longest subsequence:
            //      newseq(t) ::: seq(x) 
            //      s.t. newseq(t)(-1) <= seq(x)
            // Note: ::: is the concatenation of sequences
            var longest = seq(x) :: List.empty
            for (t <- Range(0, x)) {
                if ((seq(t) <= seq(x)) && (newseq(t).length + 1 > longest.length)) {
                    longest = newseq(t) ::: (seq(x) :: List.empty)
                }
            }
            newseq = newseq updated (x, longest)
            if (longest.length > lics.length) {
                lics = longest
            }
        }
        return lics
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
