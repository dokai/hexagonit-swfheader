import unittest
import doctest
import os.path

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocFileSuite(
            'README.txt',
            globs={'TEST_SWF' : os.path.join(os.path.dirname(__file__), 'test.swf')}))
    return suite
