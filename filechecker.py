#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versioning =
#################################################################################################################


# Take in a file named changes_python.txt and assign it to the variable fname.  Next are some list creations using []
# for commits and authors and I created a dictionary using {} for commits_for_each_author.
# and initializer values for current_commit.  The variable reading_file opens the file from fname in read mode
# and uses the method readlines to read the file.  Next index which I will use to move onto the next commits
# in the file is initialized at 0.

fname = 'changes_python.txt'
reading_file = open(fname, 'r')
data = reading_file.readlines()

class commitChanges:
    def __init__(self, revision=None, author=None, date=None, comment_line_count=None, changes=None, comment=None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

        def get_commit_comment(self):
            return 'svn merge -r' + str(self.revision - 1) + ':' + str(self.revision) + ' by ' \
                   + self.author + ' with the comment ' + ','.join(self.comment) \
                   + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
commits_for_each_author = {}
authors = []
index = 0

# The variable sep looks for lines that have 72 - followed by a new line.  A while loop is used to
# go through the file.  First each commit is parsed and put into a list of commits.  split('|') separates
# the lines by the pipe character, details[1].strip removes the spaces at the end of the word, author not in
# author is used to check if the authors name is already in the list or is it a new author.  Next author[author] = []
# gives the user an empty commit array.  Each commit is parsed and put in a list of commits.
sep = 72*'-' +'\n'
while True:
    try:
        # Sets up the revision variable as with author the whitespace is removed.  The commits are added
        # to the list and index is used to find the next index by looking for the 72 hyphons.  The try/except
        # statement is used for catching an IndexError in this case and if that occurs the program will break
        # out of the while loop.
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index + 2:data.index('', index + 1)]
        # print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index - current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break


# Reverse is used on the commits list to sort the order, the list is printed and the no. of commits.  Next it prints
# the number of elements in the authors list counting the number of authors and converting it to a string to print
# the message.  For each author print a message showing how many commits they sent.  There are 422 commits and 10
# authors.
commits.reverse()
print(commits)
print(len(commits))

for author in commits_for_each_author:
    print str(author) + ' commited ' + str(len(commits_for_each_author[author]))

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())
