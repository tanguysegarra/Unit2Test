# Unit2Test >> "You need to test!"


## What is it?

A Python3 unit-testing framework I wrote for fun and learning purposes.


## Three levels

With this tool, you can either create simple individual tests and run them one
by one, by hand.

You could also decide to create a category of tests for a given feature, give it
a title, and run all of the tests contained in this category.

Finally, you could build a test suite containing categories, themselves
containing many tests, to get the best of this tool. This would allow you a
better displaying and a success rate given as a summary for your tests.


## API

* `load_module(PATH)`: to import functions from python file given as PATH.

* `parse_options()`: to parse potential options given through the command line.
There is the verbose option `-v | --verbose`, the quiet option `-q |
--quiet`(set as default), and the help option `-h | --help`.

* `Test(FUNCTION, INPUT, OUTPUT)`: to declare a new test.
The FUNCTION value is the tested function's name, preceded by the return
value of the `load_module` call.
The INPUT value must be a list containing all parameters given to the
function.
THE OUTPUT value is the expected return value of the tested function with
these parameters.

* `TEST.check()`: to evaluate the instanced test TEST.

* `Category(TITLE)`: to declare a new category of tests. The TITLE value will be
used for display.

* `Category(TITLE, TESTS)`: same as above, but an already built list of tests
TESTS can be as a constructor parameter.

* `CATEGORY.add_test(TEST)`: to add the test TEST to the category CATEGORY.

* `CATEGORY.check()`: to evaluates all the tests in the instanced category
CATEGORY.

* `Suite(CATEGORIES)`: to create a suite of categories, all of them contained
in the list CATEGORIES.

* `SUITE.run()`: to run all the tests contained in each categories and get a
success percentage displayed.


## Example

All the code below is available in the file [example.py](example.py)

First, include the module

```python3
from utfm import *
```

Then, import the code to test with

```python
funs = load_module("somecode.py")
```

You can create and execute directly a random test with

```python
Test(funs.add, [3, 4], 5).check()
```

You can create a category of tests with

```python
c_addition = Category("ADDITION")

c_addition.add_test(utfm.Test(funs.add, [3, 4], 7))
c_addition.add_test(utfm.Test(funs.add, [1, 1], 2))
```

and launch the tests on this category with

```python
c_addition.check()
```

When executed with

```
$python example.py
```

all this code should give you the following output

```
add(3, 4) = 7 | Expected: 5 [KO]
add(3, 4) = 7 [OK]
add(1, 1) = 2 [OK]
```

# Author

* [Tanguy Segarra](https://github.com/tanguysegarra/) - *Initial work*

# TODO

* add feature to load test from file
