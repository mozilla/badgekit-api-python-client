import sys


def args ():
    args = {
        'verbosity': 1,
    }

    for arg in sys.argv[1:]:
        if arg == '--quiet':
            args['verbosity'] = 0
        if arg == '--verbose':
            args['verbosity'] = 2

    return args

args = args()