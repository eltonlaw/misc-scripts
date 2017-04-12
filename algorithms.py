""" Implementation of algorithms from 'Algorithms Unlocked' """


def linear_search(A, y):
    """ Runtime: n """
    output = None
    for i, x in enumerate(A):
        if x == y:
            output = i
            break
    return output


# Print Minimum Compute Time
if __name__ == "__main__":
    from timeit import Timer
    import sys
    import inspect
    all_fn = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for algo, fn in all_fn:
        stmt = "shuffle(A); " + algo + "(A, 1)"
        import_fn = "from __main__ import " + algo + ";"
        import_shuffle = "from random import shuffle;"
        setup_array = "A = list(range(10));"
        setup = import_fn + import_shuffle + setup_array
        time = min(Timer(stmt=stmt, setup=setup).repeat(10, 1000))

        print("\n '{}': Min. Time = {:0.5f}".format(algo, time))
        print("-"*79)
