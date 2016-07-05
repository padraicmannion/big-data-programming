#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versioning =
#################################################################################################################


# Take in a file named changes_python.txt and assign it to the variable fname.  Originally had a basic readlines for
# reading in the file held in fname but changed to a newer version so as to not read a large file all at once in
# this case for every line in the file open it in read mode.

fname = 'changes_python.txt'
#my_file = open(changes_python, 'r')
#data = my_file.readlines()
data = [line.strip() for line in open(fname, 'r')]



# Creats a class cnamed commitChanges.  This class creates variables that will be used when searching through the files
# all variables are set to None as the default starting value this way whatever the 1st value in searching the file
# will get placed in the variable also the default value won't be shown when the variable is printed.
class commitChanges:
    def __init__(self, revision=None, author=None, date=None, comment_line_count=None, changes=None, comment=None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

        def get_commit_comment(self):
            # This function is used to return the details of the commit: revision, author, comment and changes.
            # by using str the variables are concatonated as string objects.
            return 'svn merge -r' + str(self.revision - 1) + ':' + str(self.revision) + ' by ' \
                   + self.author + ' with the comment ' + ','.join(self.comment) \
                   + ' and the changes ' + ','.join(self.changes)


# Create an empty list called commits, set the current_commit to None so the 1st commit found when serching thefile
# will take the place of current_commit.  commits_for_each_author creates a dictionary that will be used to store how
# many commits have been performed by each author.  authoris a list object that will be used to hold the list of
# authors.  Index is given the initiialization value of 0.
commits = []
current_commit = None
commits_for_each_author = {}
authors = []
index = 0

# The variable sep looks for lines that have 72 - followed by a new line.  A while loop is used to
# go through the file.  First each commit is parsed and put into a list of commits.  split('|') separates
# the lines by the pipe character, details[1].strip removes the spaces at the end of the word, ach commit is pa\rsed
# and put in a list of commits.
sep = 72 * '-' + '\n'
while True:
    try:
        # While True is used to run through all the commits in the file.  The try/except is used to catch IndexError
        # exceptions and if they occur to break out of the loop.  The details variable looks to the value held in the
        # 2nd word of the line or index position 1 and splits when it finds the pipe | character.  The revision
        # variable looks inside the value held in detials and strips when it finds r this value is being taken in
        # and parsed as an int type.  The variable author takes in the 2nd word in the details variable while date
        # takes in the 3rd.  The line_count variable looks in the 4th position in the details variable strips it
        # and splits when it finds white space.  NEED SOMETHING HERE FOR COMMIT CHANGES
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index + 2:data.index('', index + 1)]
        # print(current_commit.changes)
        # Index looks for the sep (seperator) which is 72 hyphons and uses tht to increment index by 1 and
        # move on from one commit to the next.  SOMETHING NEEDED HERE.
        # This line commits.append will append the current_commit to the list of commits and be added to the list.
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
