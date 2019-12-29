import utfm

funs = utfm.load_module("somecode.py")

# ADDITION TESTS

c_addition = utfm.Category("ADDITION")

c_addition.add_test(utfm.Test(funs.add, [1, 1], 2))
c_addition.add_test(utfm.Test(funs.add, [3, 4], 7))

c_addition.check()

utfm.Test(funs.add, [3, 4], 5).check()

# CONCATENATION TESTS

c_concatenation = utfm.Category("CONCATENATION")

c_concatenation.add_test(utfm.Test(funs.concat, [[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]))
c_concatenation.add_test(utfm.Test(funs.concat, [[0], [], [42]], [0, 42]))

c_concatenation.check()

# LENGTH TESTS

c_length = utfm.Category("LENGTH")

c_length.add_test(utfm.Test(funs.length, [[1, 2, 3]], 3))

c_length.check()
