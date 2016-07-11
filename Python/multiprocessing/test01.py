from multiprocessing import Process

def f( mydict ):
    print "In f(): hello %s" % str(mydict["name"])
    mydict["name"] = "This shouldn't propagate."
    print "      : changed to:  %s" % str(mydict["name"])

if __name__ == "__main__":
    d = { "name" : "Bob Belcher",
          "show" : "Bob's Burgers" }
    p = Process( target = f, args = (d,) )
    p.start()
    p.join()
    print "In toplevel: hello %s" % str(d["name"])
