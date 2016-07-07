# Take in a file named changes_python.txt and assign it to the variable fname.  Next is the creation of a dictionary
# author that will be used to hold the authors of the commits.  This opens the file 1 line at a time in read mode.
# The print function returns how big the file that is read in.
# The variable sep looks for lines that have 72 - hyphens.
fname = 'changes_python.txt'
data = [line.strip() for line in open(fname, 'r')]

author = {}
print 'The file ', fname, ' has', len(data), ' lines.'
sep = 72*'-'


# Creates a class called commit with sets the initialization of the variables to None.  When using the function
# it uses __init__ for making the function private.  init and foo are common words used when creating these
# functions.  The variables revision, author, date and comment_line_count are broken down from the details variable
# taking an index and splitting.  The variables changes and comment deal with index.
class Commit:
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    # This creats a function for returning the commits and the details of each commit to the user including the revision
    # author, date, comment and changes.
    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' from ' \
                + self.author + ' sent on ' + self.date + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

# Creates a list to hold the commits.  Sets the initialisation value of current_commit to None so the 1st value
# taken in will automatically be taken into the list.  The variable index is initialised at 0.  This variable
# will be used for stepping from one comment to the next.
commits = []
current_commit = None
index = 0

# Author creates a dictionary object to hold a list of authors.
author = {}
while True:
    try:
        # A while loop is used to go through the file.  First each commit is parsed and put into a list of commits.
        # split('|') separates the lines by the pipe character, details[1].strip removes the spaces at the end of the word,
        # The commits are added to the list and index is used to find the next index by looking for the 72 hyphons.
        # The try/except statement is used for catching an IndexError in this case and if that occurs the program will break
        # out of the while loop.  The date variable strips the 3rd index from the variable details.

        # The line count takes the 4th index from the details variable strips it and then splits at white space
        # and this variable is parsed as an int.  The changes variable deals with the changes made between 1
        # version and another.  The index variable is incremented by 1 after it finds 72 hypons.
        # The comment takes the comment from the current comment.  The append function takes in the current_commit
        # the file is on in the loop and appends it to the list named commits.
        # The get_commit_comment is used for when the details variables of the commit are returned and printed
        # by using str the variables are parsed as strings.
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index + 2:data.index('', index + 1)]
        index = data.index(sep, index + 1)
        current_commit.comment = data[index - current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

# author not in author is used to check if the authors name is already in the list or is it a new author.
# Next author[author] = [] gives the user an empty commit array.  Dictionaries are created for all the variables.
# It sets up the revision variable as with author the whitespace is removed.
#commits_for_each_author = {}
#if author not in authors:
#authors.append(author)
#commits_for_each_author[author] = []
#Next it prints
# the number of elements in the authors list counting the number of authors and converting it to a string to print
# the message.  For each author print a message showing how many commits they sent.


# Reverse is used on the commits list to sort the order,  The get_commit_comment function is called which uses
# return to print all the details of each commit back to the user.
print 'There are ',(len(commits)), ' commits in the file.'
commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())
#print commits_for_each_author

#for author in commits_for_each_author:
    #print str(author) + ' commited ' + str(len(commits_for_each_author[author]))