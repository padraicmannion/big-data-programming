#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versions =
#################################################################################################################

# The unittest library is used to perform the test cases and the class ChangeProcessor from change_processor is imported.
# future division is used to bring in true devision instead of floor/integer division.
from __future__ import division
import unittest
from change_processor import ChangeProcessor
 var = 0

# test the changes functionality
# unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
# the setUp function uses the standard practice of naming the variable self to call itself.
# def setUp(self). The 3 files are taken into the ChangeProcessor class and the code in the
# base class runs taking data from the file.  The file test_changes 1.txt is assigned to the
# variable change_processor which contains 1 commit.  The file test_changes2.txt is assigned
# to change_processor2 and has 9 commits.  changes_python.log contains the full file and
# is held in variable named change_processor3.

class TestChanges(unittest.TestCase):

    def setUp(self):
        self.change_processor = ChangeProcessor('test_changes_1.txt')
        self.change_processor2 = ChangeProcessor('test_changes_2.txt')
        self.change_processor3 = ChangeProcessor('changes_python.log')

    # this tests the length of data file is read correctly i.e. number of lines.
    # in the 1st file the length should be 10, in the 2nd 99 and in the full file 5255.
    def test_changes_length_of_data(self):
        result = len(self.change_processor.data)
        self.assertEqual(10, result)
        result = len(self.change_processor2.data)
        self.assertEqual(99, result)
        result = len(self.change_processor3.data)
        self.assertEqual(5255, result)

    # this tests how much a specific author commited in the 1st case 1, in 2nd 3 and 3rd case is 191.
    # After this I test 2 other authors 1st vnai0001 who commited 26 and rober.hanaway who commited 132.
    def test_changes_get_number_of_commit_by_author(self):
        result = self.change_processor.get_number_of_commit_by_author('viacheslav.vdovenko')
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_commit_by_author('viacheslav.vdovenko')
        self.assertEqual(3, result)
        result = self.change_processor3.get_number_of_commit_by_author('viacheslav.vdovenko')
        self.assertEqual(191, result)
        result = self.change_processor3.get_number_of_commit_by_author('vnai0001')
        self.assertEqual(26, result)
        result = self.change_processor3.get_number_of_commit_by_author('robert.hanaway')
        self.assertEqual(152, result)
       
        
	# this tests the number of authors - the answer should be 1 in the 1 commit file.  In the
    # 2nd case there are 3 authors and in the full file there are 10.
    def test_changes_number_of_authors(self):
        result = self.change_processor.get_number_of_authors()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_authors()
        self.assertEqual(3, result)
        result = self.change_processor3.get_number_of_authors()
        self.assertEqual(10, result)

    # this tests the number of commits - the answer should be 1 in the 1st test file, 9 in the 2nd
    # test case that tests the 2nd test file and 422 for the 3rd case that tests the full file.
    def test_changes_number_of_commits(self):
        result = self.change_processor.get_number_of_commits()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_commits()
        self.assertEqual(9, result)
        result = self.change_processor3.get_number_of_commits()
        self.assertEqual(422, result)

    # this tests the first author - the answer should be 'viacheslav.vdovenko' is correct he is at index 0.  The 2nd
    # test case tests the 2nd test file who is the 7th author in the file index position 6 'vnai001'.  The 3rd test is
    # in the full file and tests if robert.hanaway is in the 2nd last index which he is.  The next tests are for the 16th and 17th
    # author/15 and 16 index respectively.  The last tests index position 421 but because index starts at 0 not 1 that means 421
    # is the last author not 422.  viacheslav.vdovenko is the author in the last position so it's correct.
    def test_changes_get_author(self):
        result = self.change_processor.get_author(0)
        self.assertEqual('viacheslav.vdovenko', result)
        result = self.change_processor2.get_author(6)
        self.assertEqual('vnai0001', result)
        result = self.change_processor3.get_author(420)
        self.assertEqual('robert.hanaway', result)
        result = self.change_processor3.get_author(15)
        self.assertEqual('vnai0001', result)
        result = self.change_processor3.get_author(16)
        self.assertEqual('viacheslav.vdovenko', result)
        result = self.change_processor3.get_author(421)
        self.assertEqual('viacheslav.vdovenko', result)
        
    # this tests the first revision - the answer should be r1551925.  The 2nd test case tests index position 3 or the 3rd revision
    # which is r1551569 so its correct.  The next 2 tests check the revision numbers on the full file for index 15 and 20 which are correct.
    def test_changes_get_revision(self):
        result = self.change_processor.get_revision(0)
        self.assertEqual('r1551925', result)
        result = self.change_processor2.get_revision(2)
        self.assertEqual('r1551569', result)
        result = self.change_processor3.get_revision(15)
        self.assertEqual('r1551248', result)
        result = self.change_processor3.get_revision(20)
        self.assertEqual('r1550591', result)
      

    # this tests the date - the answer should be 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015).
    # the 2nd tests the 2nd test file at index 5 should be same date as 1st case but 06:10:10 +0000.
    # the 3rd tests the full file at index 10 should be 2015-11-26 14:17:48 +0000 (Thu, 26 Nov 2015).
    def test_changes_get_date(self):
        result = self.change_processor.get_date(0)
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', result)
        result = self.change_processor2.get_date(5)
        self.assertEqual('2015-11-27 06:10:10 +0000 (Fri, 27 Nov 2015)', result)
        result = self.change_processor3.get_date(10)
        self.assertEqual('2015-11-26 14:17:48 +0000 (Thu, 26 Nov 2015)', result)
        

    # this tests the comment - the answer should be 'Renamed folder to the correct name'.
    # the 2nd tests the 2nd test file at index 6 comment which is correct.  The last 2 test the
    # full file to ensure the comments are correct which they are.
    def test_changes_get_comment(self):
        result = self.change_processor.get_comment(0)
        self.assertEqual(['Renamed folder to the correct name'], result)
        result = self.change_processor2.get_comment(6)
        self.assertEqual(['SFR-108 : 1.buddy sync removed from settings. 2. italics text corrected.'], result)
        result = self.change_processor3.get_comment(420)
        self.assertEqual(['Added configuration for web auth, plan management and logout'], result)
        result = self.change_processor3.get_comment(421)
        self.assertEqual(['Rename folder'], result)

    # this tests the number of comment lines - the answer should be 1 line.
    # the next 2 test the number of comment lines for the 2nd test file and the full file and are correct.
    def test_changes_get_number_of_comment_lines(self):
        result = self.change_processor.get_number_of_comment_lines(0)
        self.assertEqual('1 line', result)
        result = self.change_processor2.get_number_of_comment_lines(2)
        self.assertEqual('1 line', result)
        result = self.change_processor3.get_number_of_comment_lines(10)
        self.assertEqual('4 lines', result)

    # this tests the file changes of first revision.  The 2nd test checks the 2nd test file at index position 2 or the 3rd commit.  The final 2 tests
    # are run on the full file at index position 16 and 18 which are correct.
    def test_changes_get_file_changes(self):
        result = self.change_processor.get_file_changes(0)
        self.assertEqual(['Changed paths:', 'A /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawable-xxxhdpi (from /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawablw-xxxhdpi:1551688)', \
'D /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawablw-xxxhdpi', \
'A /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawable-xxxhdpi (from /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawablw-xxxhdpi:1551922)', \
'D /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawablw-xxxhdpi'], result)
        result = self.change_processor2.get_file_changes(2)
        self.assertEqual(['Changed paths:', 'M /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/settings.gradle'], result)
        result = self.change_processor3.get_file_changes(16)
        self.assertEqual(['Changed paths:', 'M /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/libs/ui/src/com/newbay/syncdrive/android/ui/gcm/GcmNotificationCreator.java'], result)
        result = self.change_processor3.get_file_changes(18)
        self.assertEqual(['Changed paths:', 'M /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/build.gradle'], result)
       

    # Function used for testing user_input = 4 on interesting.py.  result gets the number of commits for the author, result2 gets the number of commits
    # in that file and result 3 gets the % of author commits over total commits in the file to 3 decimil places.  All 3 files are tested by the same author
    # In the 1st case there is only 1 commit so it makes up 1.0 or 100% in the 2nd case 33% or .333 and in the 3rd .453 or 45.3%
    # result4 is used for user_input = 5 where it shows the % the other users submitted by 1 or 100% - result3.
    def test_get_percentage_of_total_commits(self):
        result = self.change_processor.get_number_of_commit_by_author('viacheslav.vdovenko')       
        result2 = self.change_processor.get_number_of_commits()
        result3 = round(result / result2, 3)
        self.assertEqual(1.0, result3)
        result4 = 1 - result3
        self.assertEqual(0.0, result4)
        
        result = self.change_processor2.get_number_of_commit_by_author('viacheslav.vdovenko')       
        result2 = self.change_processor2.get_number_of_commits()
        result3 = round(result / result2, 3)
        self.assertEqual(.333, result3)
        result4 = 1 - result3
        self.assertEqual(.667, result4)
        
        result = self.change_processor3.get_number_of_commit_by_author('viacheslav.vdovenko')       
        result2 = self.change_processor3.get_number_of_commits()
        result3 = round(result / result2, 3)
        self.assertEqual(.453, result3)
        result4 = round(1 - result3, 3)
        self.assertEqual(.547, result4)
           
    def test_average(self):
        # Test the average which is total the commits in the file / number of authors in the file
        # This will say what average commit / author is.  In 1st case there is only 1 so it stays 10
        # 2nd case 9/3 = 3 average.  The 3rd case is the full file 422/10 = 42.2.
        result = self.change_processor.get_number_of_commits()
        result2 = self.change_processor.get_number_of_authors()
        result3 = result / result2
        self.assertEqual(1, result3)
        
        result = self.change_processor2.get_number_of_commits()
        result2 = self.change_processor2.get_number_of_authors()
        result3 = result / result2
        self.assertEqual(3, result3)
        
        result = self.change_processor3.get_number_of_commits()  
        result2 = self.change_processor3.get_number_of_authors()
        result3 = result / result2
        self.assertEqual(42.2, result3)
      
           
# Runs all the test cases.
if __name__ == '__main__':
    unittest.main()
