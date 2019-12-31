import importlib


class Category:

    def __init__(self, title, tests = []):

        self.title = title
        self.tests = []

    def add_test(self, test):

        self.tests.append(test)

    def check(self):

        print("\n~~~ " + self.title + " ~~~")

        for t in self.tests:
            t.check()


class Test:

    def __init__(self, function, inp = [], out = None):

        self.function = function
        self.inp = inp
        self.out = out

    @classmethod
    def load_from_file(cls, func, path):

        f = open(path)
        lines = f.readlines()
        f.close()

        inp = []
        for i in range(int(lines[0])):
            if len(lines[i + 1]) > 1:
                inp.append(lines[i + 1][0])
            else:
                inp.append(lines[i + 1])

        out = lines[len(lines) - 1]

        return cls(func, inp, out)


    def check(self):

        fmt_inp = ", ".join(str(x) for x in self.inp)

        try:
            res = self.function(*self.inp)

            if res == self.out:
                print("\033[0;32m[OK]\033[0m", end='')
                print(f" {self.function.__name__}({fmt_inp}) = {res}", end=' ')

            else:
                print("\033[0;31m[KO]\033[0m", end='')
                print(f" {self.function.__name__}({fmt_inp}) = {res} | Expected: {self.out}", end=' ')
                #print(f" Expected: {self.out} | Received: {res}")

            print("")

        except Exception as e:
            print(e, "\033[0;31m[K0]\033[0m")


def load_module(path):

    if path[-3:] == ".py":
        path = path[:-3]

    return importlib.import_module(path)
