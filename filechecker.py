# Take in a file named changes_python.txt and assign it to the variable fname.  Next are some list creations using []
# for commits and author and I created a dictionary using {} for commits_for_each_author.
# and initializer values for current_commit.  The variable reading_file opens the file from fname in read mode
# and uses the method readlines to read the file.  Next index which I will use to move onto the next commits
# in the file is initialized at 0.  The variable sep looks for lines that have 72 - followed by a new line.
fname = 'changes_python.txt'
reading_file = open(fname, 'r')
data = reading_file.readlines()
commits = []
commits_for_each_author = {}
authors = []
index = 0
sep = 72*'-' +'\n'


# Creates a class called commiting with sets the initialization of the variables to $None.  When using the function
# it uses __init__ for making the function private.  init and foo are common words used when creating these
# functions.
class Commiting:
    def __init__(self, revision=None, author=None, date=None, comment_line_count=None, changes=None, comment=None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment


    # The get_commit_comment is used for when the details variables of the commit are returned and printed
    # by using str the variables are parsed as strings.
    def get_commit_comment(self):
        return 'Merge the -r' + str(self.revision - 1) + ':' + str(self.revision) + ' by ' \
        + self.author + ' with the comment ' + ','.join(self.comment) \
        + ' and the changes in the new version are ' + ','.join(self.changes)


# A while loop is used to go through the file.  First each commit is parsed and put into a list of commits.
# split('|') separates the lines by the pipe character, details[1].strip removes the spaces at the end of the word,
# author not in author is used to check if the authors name is already in the list or is it a new author.
# Next author[author] = [] gives the user an empty commit array.  Dictionaries are created for all the variables.
# It sets up the revision variable as with author the whitespace is removed.
#
# The commits are added to the list and index is used to find the next index by looking for the 72 hyphons.
# The try/except statement is used for catching an IndexError in this case and if that occurs the program will break
# out of the while loop.  The date variable strips the 3rd index from the variable details.
# The line count takes the 4th index from the details variable strips it and then splits at white space
# and this variable is parsed as an int.  The changes variable deals with the changes made between 1
# version and another.  The index variable is incremented by 1 after it finds 72 hypons.
# The comment takes the comment from the current comment.  The append function takes in the current_commit
# the file is on in the loop and appends it to the list named commits.


while True:
    try:
        current_commit = Commiting()
        details = data[index + 1].split('|')
        author = details[1].strip()
        if author not in authors:
            authors.append(author)
            commits_for_each_author[author] = []

        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        index = data.index(sep, index + 1)
        current_commit.comment = data[index - current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break


# Reverse is used on the commits list to sort the order, the list is printed and the no. of commits.  Next it prints
# the number of elements in the authors list counting the number of authors and converting it to a string to print
# the message.  For each author print a message showing how many commits they sent.
commits.reverse()
print(commits)
print(len(commits))
print 'Author Count : ' + str(len(authors))
print commits_for_each_author

for author in commits_for_each_author:
    print str(author) + ' commited ' + str(len(commits_for_each_author[author]))
