from utfm import *

funs = load_module("somecode.py")

# ADDITION TESTS

c_addition = Category("ADDITION")

c_addition.add_test(Test(funs.add, [1, 1], 2))
c_addition.add_test(Test(funs.add, [3, 4], 7))

# CONCATENATION TESTS

c_concatenation = Category("CONCATENATION")

c_concatenation.add_test(Test(funs.concat, [[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]))
c_concatenation.add_test(Test(funs.concat, [[0], [], [42]], [0, 42]))

# LENGTH TESTS

c_length = Category("LENGTH")

c_length.add_test(Test(funs.length, [[1, 2, 3]], 3))

# TEST SUITE RUNNER

suite = Suite([c_addition, c_concatenation, c_length])
suite.run()
