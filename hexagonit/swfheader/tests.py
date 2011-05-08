import doctest
import os.path
import pprint
import unittest


def int_valued_dict(d):
    """Returns a new dictionary with long values converted to int.

    We do this to normalize the output in the doctest.
    """
    d2 = {}
    for k, v in d.iteritems():
        if isinstance(v, long):
            d2[k] = int(v)
        else:
            d2[k] = v
    return d2


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocFileSuite(
        '../../README.rst',
        globs={
            'TEST_SWF': os.path.join(os.path.dirname(__file__), 'test.swf'),
            'pprint': lambda d: pprint.pprint(int_valued_dict(d))}))
    return suite
