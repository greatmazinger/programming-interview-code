import logging
import os

logger = None

def setup_logger( targetdir = ".",
                  filename = "lis.log",
                  logger_name = 'lis',
                  debugflag = 0 ):
    # Set up main logger
    global logger
    logger = logging.getLogger( logger_name )
    formatter = logging.Formatter( '[%(funcName)s] : %(message)s' )
    filehandler = logging.FileHandler( os.path.join( targetdir, filename ) , 'w' )
    if debugflag:
        logger.setLevel( logging.DEBUG )
        filehandler.setLevel( logging.DEBUG )
    else:
        filehandler.setLevel( logging.ERROR )
        logger.setLevel( logging.ERROR )
    filehandler.setFormatter( formatter )
    logger.addHandler( filehandler )

def recreate_longest_inc_sequence( M, lsf, P, X ):
    lis = [ 0 ] * lsf
    k = M[lsf]
    for x in xrange(lsf - 1, -1, -1):
        lis[x] = X[k]
        k = P[k]
    return lis

def longest_inc_subsequence( numbers ):
    """
    >>> longest_inc_subsequence( [ 5, 2, 7, 4, 3, 8 ] ) # doctest: +NORMALIZE_WHITESPACE
    [2, 3, 8]
    >>> longest_inc_subsequence( [] )
    []
    """
    global logger
    X = numbers # rename the input list
    length = len(X)
    if length == 0:
        return []
    M = range(0, length + 1)
    # M[j] = stores the index k of the smallest value X[k] s.t.
    #     there is an increasing subsequence of length j ending at X[k] on the range j <= k <= i
    #     -- (note we have j <= k <= i here, because
    #        j represents the length of the increasing subsequence
    #        k represents the index of its termination
    #     and there can't be a subsequence longer than the last index
    # Note also that M[0] is unused.
    P = [ -1 ] * length
    lsf = 0 # length of longest increasing subsequence so far
    # At any point
    #    X[M[1], X[M[2]], ..., X[M[L]]
    # is nondecreasing.
    for i in xrange(length):
        logger.debug( "==[ %d ]==================================================" % i )
        longest = [ X[i] ]
        lo = 1
        hi = lsf
        logger.debug( "before:: lo: %d   hi(lsf): %d" % (lo, hi) )
        while lo <= hi:
            mid = (lo + hi) / 2
            if X[M[mid]] < X[i]:
                lo = mid + 1
            else:
                hi = mid - 1
            logger.debug( "      :: lo[ %d ]  mid[ %d ]  hi[ %d ]" % (lo, mid, hi) )
        new_lsf = lo # first time through loop goes here
        logger.debug( "after :: lo(new_lsf): %d   hi(lsf): %d" % (lo, hi) )
        # The predecessor of X[i] is the last index of the subsequence of length (new_lsf - 1)
        logger.debug( "setting P[%d] to M[%d] = %d" % (i, new_lsf - 1, M[new_lsf - 1]) )
        P[i] = M[new_lsf - 1]
        logger.debug( "setting M[%d] to %d" % (new_lsf, i) )
        M[new_lsf] = i
        if new_lsf > lsf:
            logger.debug( "new lsf found: %d" % new_lsf )
            lsf = new_lsf
    result = recreate_longest_inc_sequence( M, lsf, P, X )
    return result

if __name__ == "__main__":
    import doctest

    setup_logger( debugflag = True )
    doctest.testmod()
