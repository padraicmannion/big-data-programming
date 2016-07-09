# Take in a file named changes_python.txt and assign it to the variable fname.
# This opens the file 1 line at a time in read mode.
# The print function returns how big the file that is read in.
# The variable sep looks for lines that have 72 - hyphens.
fname = 'changes_python.txt'
data = [line.strip() for line in open(fname, 'r')]
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

    # Creates a function for returning the commits and the details of each commit to the user including the revision
    # author, date, comment and changes.
    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' from ' \
                + self.author + ' sent on ' + self.date + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)


# Creates a list to hold the commits.  Sets the initialisation value of current_commit to None so the 1st value
# taken in will automatically be taken into the list.  The variable index is initialised at 0.  This variable
# will be used for stepping from one comment to the next.  The dictionary commits_for_each_author is used
# to hold how many commits each author has done and authors is a list that will hold the names of all the authors.
commits = []
current_commit = None
index = 0
commits_for_each_author = {}
authors = []

# 1st a welcome message is displayed to the user and is given 2 choices 1 for authors and 2 for all details.
# if anything else will return to the user_choice question asking for correct input.  The user_choice
# variable is taken in as a int variable.  A while true loop is used to ensure an integer is passed to the variable
# called user_choice if the user types a integer it will break out of the loop.  If not an appropriate message
# will be displayed back to the user and the program will iterate until the user enters a valid choice.  The
# if, elif handles numbers that are not 1 or 2 and except handles strings.

while True:
    try:
        user_choice = int(raw_input('Welcome to the file testing program\npress 1 for authors and 2 for all details:\n'))
        if user_choice < 1:
            print 'You have entered an invalid number the number cannot be less than 1.'
            continue
        elif user_choice > 2:
            print ' You have entered and invalid number cannot be more than 2.'
            continue
        else:
            break
    except:
        print 'Please enter only a number either 1 or 2.'
        continue


# author not in author is used to check if the authors name is already in the list or is it a new author.
# Next author[author] = [] gives the user an empty commit array.
# It sets up the revision variable as with author the whitespace is removed.
# The Author Choice
if user_choice == 1:
    while True:
        try:
            details = data[index + 1].split('|')
            author = details[1].strip()
            if author not in authors:
                authors.append(author)
                commits_for_each_author[author] = []
            revision = details[0].strip()
            commits_for_each_author[author].append(revision)
            commits.append(details)
            index = data.index(sep, index + 1)
        except IndexError:
            break

# Comments choice
if user_choice == 2:
    while True:
        # A while loop is used to go through the file.  First each commit is parsed and put into a list of commits.
        # split('|') separates the lines by the pipe character, details[1].strip removes the spaces at the end of the word,
        # The commits are added to the list and index is used to find the next index by looking for the 72 hyphens.
        # The try/except statement is used for catching an IndexError in this case and if that occurs the program will break
        # out of the while loop.  The date variable strips the 3rd index from the variable details.

        # The line count takes the 4th index from the details variable strips it and then splits at white space
        # and this variable is parsed as an int.  The changes variable deals with the changes made between 1
        # version and another.  The index variable is incremented by 1 after it finds 72 hyphens.
        # The comment takes the comment from the current comment.  The append function takes in the current_commit
        # the file is on in the loop and appends it to the list named commits.
        # The get_commit_comment is used for when the details variables of the commit are returned and printed
        # by using str the variables are parsed as strings.
        try:
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


# The print is used to print the number of commits in the file.  Reverse is used on the commits list to sort the order.
print 'There are ',(len(commits)), ' commits in the file.'
commits.reverse()

if user_choice == 1:
    print 'Author Count : ' + str(len(authors))
    print commits_for_each_author
    for author in commits_for_each_author:
        print str(author) + ' commited ' + str(len(commits_for_each_author[author]))

# The get_commit_comment function is called which uses return to print all the details of each commit back to the user.
if user_choice == 2:
    for index, commit in enumerate(commits):
        print(commit.get_commit_comment())

