import unittest

from change_processor import ChangeProcessor

# test the changes functionality
class TestChanges(unittest.TestCase):

    def setUp(self):
        self.change_processor = ChangeProcessor('test_changes_1.txt')
        self.change_processor2 = ChangeProcessor('test_changes_2.txt')
        self.change_processor3 = ChangeProcessor('changes_python.log')

    # this tests the length of data file is read correctly.
    def test_changes_length_of_data(self):
        result = len(self.change_processor.data)
        self.assertEqual(10, result)
        result = len(self.change_processor2.data)
        self.assertEqual(99, result)
        result = len(self.change_processor3.data)
        self.assertEqual(5255, result)

    # this tests the number of authors - the answer should be 1.
    def test_changes_get_number_of_commit_by_author(self):
        result = self.change_processor.get_number_of_commit_by_author('viacheslav.vdovenko')
        self.assertEqual(1, result)

	# this tests the number of authors - the answer should be 1.
    def test_changes_number_of_authors(self):
        result = self.change_processor.get_number_of_authors()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_authors()
        self.assertEqual(3, result)
        result = self.change_processor3.get_number_of_authors()
        self.assertEqual(10, result)

    # this tests the number of commits - the answer should be 1.
    def test_changes_number_of_commits(self):
        result = self.change_processor.get_number_of_commits()
        self.assertEqual(1, result)
        result = self.change_processor2.get_number_of_commits()
        self.assertEqual(9, result)
        result = self.change_processor3.get_number_of_commits()
        self.assertEqual(422, result)

    # this tests the first author - the answer should be 'viacheslav.vdovenko'.
    def test_changes_get_author(self):
        result = self.change_processor.get_author(0)
        self.assertEqual('viacheslav.vdovenko', result)
        result = self.change_processor2.get_author(6)
        self.assertEqual('vnai0001', result)
        result = self.change_processor3.get_author(420)
        self.assertEqual('robert.hanaway', result)

    # this tests the first revision - the answer should be r1551925.
    def test_changes_get_revision(self):
        result = self.change_processor.get_revision(0)
        self.assertEqual('r1551925', result)

    # this tests the date - the answer should be 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015).
    def test_changes_get_date(self):
        result = self.change_processor.get_date(0)
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', result)

    # this tests the comment - the answer should be 'Renamed folder to the correct name'.
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
    def test_changes_get_number_of_comment_lines(self):
        result = self.change_processor.get_number_of_comment_lines(0)
        self.assertEqual('1 line', result)

    # this tests the file changes of first revision
    def test_changes_get_file_changes(self):
        result = self.change_processor.get_file_changes(0)
        self.assertEqual(['Changed paths:', 'A /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawable-xxxhdpi (from /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawablw-xxxhdpi:1551688)', \
'D /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive/res/drawablw-xxxhdpi', \
'A /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawable-xxxhdpi (from /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawablw-xxxhdpi:1551922)', \
'D /cloud/personal/syncdrive-international/android/branches/android-15.2-solutions/clients/syncdrive-bt/res/drawablw-xxxhdpi'], result)

if __name__ == '__main__':
    unittest.main()
