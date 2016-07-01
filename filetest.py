#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versioning =
#################################################################################################################

# The unittest library is used to perform the test cases.

import unittest
#from filechecker import


class TestFile(unittest.TestCase):
    def setUp(self):
        self.filechecker = Filechecker()
        # unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
        # the setUp function uses the standard practice of naming the variable self to call itself.
        # def setUp(self).

    def test_file_author_commits(self):
        # Function to test the authors commits starts by looking for an author that isn't in the list in this case it
        # will return 0 because the author will have 0 commits.  After I tested for specific authors from
        # which I knew what the results of no of commits are e.g. dred0001 commited 2, murari.krishnan commited 1,
        # robert.hanaway commited 152 and viacheslav.vdovenko commited 191.
        self.filechecker.move(15)
        self.assertEqual(15, self.filechecker.getMileage())
        self.filechecker.move(12)
        self.assertEqual(27, self.filechecker.getMileage())
        self.filechecker.move(13)
        self.assertEqual(40, self.filechecker.getMileage())
        self.filechecker.move(3.5)
        self.assertEqual(43.5, self.filechecker.getMileage())

    def test_file_author_count(self):
        # Function for testing the number of authors in the list which is 10.
        self.filechecker.setMake('Ferrari')
        self.assertEqual('Ferrari', self.filechecker.getMake())


    def test_file_number_of_commits(self):
        # The value for len(commits) is 422.  Function for testing the number of commits in the file.
        self.filechecker.setEngineSize(1.8)
        self.assertEqual(1.8, self.filechecker.getEngineSize())



# Runs all the test cases.
if __name__ == '__main__':
    unittest.main()