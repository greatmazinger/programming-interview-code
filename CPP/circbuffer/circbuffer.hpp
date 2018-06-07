#ifndef CIRCULAR_BUFFER
#define CIRCULAR_BUFFER

#include <cassert>

class CBRecord {
public:
    CBRecord(int new_offset, unsigned int new_utime)
             : offset{new_offset}
             , utime{new_utime}
    {
        offset = new_offset;
        utime = new_utime;
    }

    CBRecord() 
             : offset{0}
             , utime{0}
    {
    }

    // Default destructor is ok.
    ~CBRecord() = default;

    // Default copy constructor is ok.
    CBRecord(const CBRecord&) = default;
    // Default copy assignment op is ok.
    CBRecord& operator=(const CBRecord&) = default;

private:
    int offset;
    unsigned int utime;
};

class CircularBuffer {
public:
    CircularBuffer( int capacity )
                    : cbcapacity{capacity}
                    , cbsize{0}
    {
        assert(capacity > 0);
        buf = new CBRecord[capacity];
    }
   
    // Default destructor is ok.
    ~CircularBuffer() = default;

    // Default copy constructor is ok.
    CircularBuffer(const CircularBuffer&) = default;
    // Default copy assignment op is ok.
    CircularBuffer& operator=(const CircularBuffer&) = default;

    inline int capacity() { return cbcapacity; }
    inline int size() { return cbsize; }
    inline bool empty() { return this->cbsize == 0; };

    // TODO: What does push_back return?
    //  Possibilities:
    //   - a reference to the element pushed?
    //   - boolean for success?
    //   - nothing?
private:
    CBRecord *buf;
    CBRecord *front;
    CBRecord *back;
    int cbcapacity;
    int cbsize;
};

#endif // CIRCULAR_BUFFER
