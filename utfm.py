from optparse import OptionParser

import importlib


class Suite:

    def __init__(self, categories = []):
        self.categories = categories

    def add_category(self, category):
        self.categories.append(category)

    def run(self, opt = None):
        nb_tests = 0
        passed = 0

        print("")
        for c in self.categories:
            nb_tests += len(c.tests)
            passed += c.check(opt)

        perc = 0
        if nb_tests != 0:
            perc = passed / nb_tests * 100

        if perc > 50:
            color = "\033[0;32m" #green
        else:
            color = "\033[0;31m" #red

        print(">>>" + color + " PASSED: " + str(perc) + "%" + "\033[0m <<<\n")


class Category:

    def __init__(self, title, tests = []):
        self.title = title
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def check(self, opt = None):
        passed = 0

        print("~~~ " + self.title + " ~~~")

        for t in self.tests:
            passed += t.check(opt)

        print("")

        return passed


class Test:

    def __init__(self, function, inp = [], out = None):
        self.function = function
        self.inp = inp
        self.out = out

    def check(self, opt = None):
        fmt_inp = ", ".join(str(x) for x in self.inp)

        try:
            res = self.function(*self.inp)

            if res == self.out:
                print("\033[0;32m[OK]\033[0m ", end='')
                if opt.verbose:
                    print(f"{self.function.__name__}({fmt_inp}) = {res}", end='')

                print("")
                return 1

            else:
                print("\033[0;31m[KO]\033[0m ", end='')
                if opt.verbose:
                    print(f"{self.function.__name__}({fmt_inp}) = {res} | Expected: {self.out}", end='')
                else:
                    print(f"Received: {res} | Expected: {self.out}", end='')

                print("")
                return 0


        except Exception as e:
            print(e, "\033[0;31m[K0]\033[0m")
            return 0


def load_module(path):
    if path[-3:] == ".py":
        path = path[:-3]

    return importlib.import_module(path)


def parse_options():

    usage = "Usage: ./%prog [options]"

    parser = OptionParser(usage=usage)

    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                      default=False,
                      help="display complete outputs to stdout")

    parser.add_option("-q", "--quiet", action="store_false", dest="verbose",
                      help="do not print complete outputs to stdout")

    (options, args) = parser.parse_args()

    #return (options, args)
    return options
