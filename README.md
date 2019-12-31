# Unit2TestUrPython: "You need to test your python"

## What is it?

A Python3 unit-testing framework I wrote for fun and learning purposes.

## How to use?

Start your test code with

```python3
import utfm
```

## API

* `load_module(PATH)`: to import functions from python file given as PATH.

* `Category(TITLE)`: to declare a new category of tests. The TITLE value will be
used for display.

* `Category(TITLE, TESTS)`: same as above, but an already built list of tests
TESTS can be as a constructor parameter.

* `CATEGORY.add_test(TEST)`: to add the test TEST to the category CATEGORY.

* `Test(FUNCTION, INPUT, OUTPUT)`: to declare a new test.
    The FUNCTION value is the tested function's name, preceded by the return
    value of the `load_module` call.
    The INPUT value must be a list containing all parameters given to the
    function.
    THE OUTPUT value is the expected return value of the tested function with
    these parameters.

* `Test.load_from_file(PATH)`: read the file given as PATH. Its first lign
* should be the function name, its second lign should be the input parameters,
* and the third lign should be the expected output.

* `TEST.check()`: to evaluate the instanced test TEST.

* `CATEGORY.check()`: to evaluate all the tests in the instanced category
CATEGORY.

## Example

All the code below is available in the file [example.py](example.py)

```python3
import utfm

funs = utfm.load_module("somecode.py")

c_addition = utfm.Category("ADDITION")

c_addition.add_test(utfm.Test(funs.add, [3, 4], 7))
c_addition.add_test(utfm.Test(funs.add, [1, 1], 2))

c_addition.check()

utfm.Test(funs.add, [3, 4], 5).check()
```

When executed with

```
$python example.py
```

you should get the following output

```
add(3, 4) = 7 [OK]
add(1, 1) = 2 [OK]
add(3, 4) = 7 | Expected: 5 [KO]
```

# Author

* [Tanguy Segarra](https://github.com/tanguysegarra/) - *Initial work*

# TODO

* add feature to load test from file
* add feature to get success percentage over all tests
        for example a stats_display() function
* add verbose/quiet/file options
