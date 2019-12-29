from optparse import OptionParser

import importlib


class Category:

    def __init__(self, title, tests = []):

        self.title = title
        self.tests = []

    def add_test(self, test):

        self.tests.append(test)

    def check(self):

        print("~~~ " + self.title + " ~~~")

        for t in self.tests:
            t.check()

        print("")


class Test:

    def __init__(self, function, inp = [], out = None):

        self.function = function
        self.inp = inp
        self.out = out

    def check(self):

        fmt_inp = ", ".join(str(x) for x in self.inp)

        try:
            res = self.function(*self.inp)


            if res == self.out:
                print(f"{self.function.__name__}({fmt_inp}) = {res}", end=' ')
                print("\033[0;32m[OK]\033[0m")

            else:
                print(f"{self.function.__name__}({fmt_inp}) = {res} | Expected: {self.out}", end=' ')
                print("\033[0;31m[KO]\033[0m")

        except Exception as e:
            print(e, "\033[0;31m[K0]\033[0m")


def load_module(path):

    if path[-3:] == ".py":
        path = path[:-3]

    return importlib.import_module(path)
