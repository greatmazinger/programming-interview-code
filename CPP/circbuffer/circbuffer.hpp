#ifndef CIRCULAR_BUFFER
#define CIRCULAR_BUFFER

#include <cassert>

class CBRecord {
public:
    CBRecord(int new_offset, unsigned int new_utime)
             : offset(new_offset)
             , utime(new_utime)
    {
        offset = new_offset;
        utime = new_utime;
    }

    CBRecord() 
             : offset(0)
             , utime(0)
    {
    }

    // Default copy constructor is ok.
private:
    int offset;
    unsigned int utime;
};

class CircularBuffer {
public:
    CircularBuffer( int capacity )
                    : cbcapacity(capacity)
                    , cbsize(0)
    {
        assert(capacity > 0);
        buf = new CBRecord[capacity];
    }
   
   // TODO: What about the copy constructor?

    inline int capacity() { return cbcapacity; }
    inline int size() { return cbsize; }
    inline bool empty() { return
private:
    CBRecord * buf;
    CBRecord * front;
    CBRecord * back;
    int cbcapacity;
    int cbsize;
};

#endif // CIRCULAR_BUFFER
