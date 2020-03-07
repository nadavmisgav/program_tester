from program import Program
from collections import defaultdict
from collections import namedtuple
import csv

Test = namedtuple("Test", ["name", "args", "excpect"])


class Tester:
    def __init__(self, tests):
        self.tests = tests
        self.results = defaultdict(list)

    def test(self, student, path):
        try:
            with Program(path) as prog:
                prog.compile()
                for _, args, excpect in self.tests:
                    res = self._run_test(prog, args, excpect)
                    print("." if res else "X", end="")
                    self.results[student].append("PASS" if res else "FAIL")
                print()
        except (RuntimeError, RuntimeWarning) as e:
            print(str(e))
            self.results[student].append(str(e))

    @staticmethod
    def _run_test(prog, args, excpect):
        prog.log_file.write("#"*40+"\n")
        res = excpect == prog.run(args)
        prog.log_file.write("expected:\n{}\n".format(excpect))
        prog.log_file.write("result: {}\n".format("PASS" if res else "FAIL"))
        return res

    def report_results(self):
        with open("result.csv", "w") as fd:
            handle = csv.writer(fd, dialect='excel')
            handle.writerow(["student", "grade"] +
                            [test.name for test in self.tests])
            for key, val in self.results.items():
                passed = sum(1.0 for res in val if res == "PASS")
                grade = 100*passed/len(self.tests)
                handle.writerow([key, grade] + val)
