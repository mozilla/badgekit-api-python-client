import badgekitapiclient
import glob
import os.path
import remote
import unittest

try:
    import json
except ImportError:
    import simplejson as json


client = badgekitapiclient.Client(remote.Remote())


def run (*tests, **kwargs):
    tests = unittest.TestSuite(tests)
    return unittest.TextTestRunner(**kwargs).run(tests)


class TestCase (unittest.TestCase):

    def __init__ (self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.client = client

    @classmethod
    def get_suite (cls):
        return unittest.TestLoader().loadTestsFromTestCase(cls)

    @classmethod
    def run_tests (cls, **kwargs):
        suite = cls.get_suite()
        return run(suite, **kwargs)
