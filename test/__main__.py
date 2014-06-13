from glob import glob
import os.path
import tests
import utils


def main (**kwargs):
    pattern = os.path.join(os.path.dirname(__file__), '*_test.py');
    all_tests = []

    for path in glob(pattern):
        name = os.path.splitext(os.path.basename(path))[0]
        test = __import__(name)
        all_tests.append(test.suite())

    tests.run(*all_tests, **kwargs)


if __name__ == '__main__':
    main(**utils.args)
