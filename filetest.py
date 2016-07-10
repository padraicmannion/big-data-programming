#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versions =
#################################################################################################################

# The unittest library is used to perform the test cases and the class Commit from filechecker is imported.

import unittest
from filechecker import Commit


# unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
# the setUp function uses the standard practice of naming the variable self to call itself.
# def setUp(self).
class TestFile(unittest.TestCase):
    def setUp(self):
        self.filechecker = Filechecker()


    # assertDictContainsSubset(expected, actual, msg=None)
    # Tests whether the key/value pairs in dictionary actual are a superset of those in expected. If not,
    # an error message listing the missing keys and mismatched values is generated.

    # assertItemsEqual(actual, expected, msg=None)
    # Test that sequence expected contains the same elements as actual, regardless of their order. When
    # they do not, an error message listing the differences between the sequences will be generated.
    # Duplicate elements are not ignored when comparing actual and expected. It verifies if each element
    # has the same count in both sequences. It is the equivalent of assertEqual(sorted(expected),
    #sorted(actual)) but it works with sequences of unhashable objects as well.
    #references
    #http://nullege.com/codes/search/unittest.TestCase.assertDictContainsSubset
    #http://nullege.com/codes/search?cq=unittest.TestCase.assertCountEqual
    #http://nullege.com/codes/search?cq=unittest.TestCase.addTypeEqualityFunc

    #self.assertDictContainsSubset(
    #{'author': 'viacheslav.vdovenko', 'date': '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', 'revision': '-r1551924:1551925'},
    #)

# Runs all the test cases.
if __name__ == '__main__':
    unittest.main()
