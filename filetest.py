#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versioning =
#################################################################################################################

# The unittest library is used to perform the test cases and the class Commiting from filechecker is imported.

import unittest
from filechecker import Commiting


class TestFile(unittest.TestCase):
    def setUp(self):
        self.filechecker = Filechecker()
        # unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
        # the setUp function uses the standard practice of naming the variable self to call itself.
        # def setUp(self).

    def test_file_commits_details(self):
        # Function that calls itself and is used to test the details variable
        self.assertEqual( ,self.filechecker.get)

    def test_file_author_count(self):
        # Function for testing the number of authors in the list which is 10.
        self.assertEqual(10, self.filechecker.get())


    def test_file_number_of_commits(self):
        # The value for len(commits) is 422.  Function for testing the number of commits in the file.
        self.assertEqual(422, self.filechecker.get())

# function for revison, author, date, comment, line_count and changes needed



# Runs all the test cases.
if __name__ == '__main__':
    unittest.main()