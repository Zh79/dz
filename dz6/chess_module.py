import itertools

def main():
    def queens ():
        for p in itertools.permutations (range (8) ):
            yield [x for x in enumerate (p) ]

    for q in queens ():
        err = False
        for a, b in ( (a, b) for a in q for b in q if a [0] < b [0] ):
            if abs (a [0] - b [0] ) == abs (a [1] - b [1] ):
                err = True
                break
        if not err: print (q)

