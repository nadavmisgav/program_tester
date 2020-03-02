import os
from tester import Tester

import sys
sys.path.append('tests')
from example_tests import tests  # noqa


SRC_DIR = "src_files"


def main():
    tester = Tester(tests)
    for student in os.listdir(SRC_DIR):
        print("Testing student {}: ".format(student), end='')
        tester.test(student, os.path.join(SRC_DIR, student))

    print("Creating report")
    tester.report_results()


if __name__ == "__main__":
    main()
