# Take in a file named changes_python.txt and assign it to the variable fname.  Next are some list creations using []
# for commits and authors and I created a dictionary using {} for commits_for_each_author.
# and initializer values for current_commit.  The variable reading_file opens the file from fname in read mode
# and uses the method readlines to read the file.  Next index which I will use to move onto the next commits
# in the file is initialized at 0.

fname = 'changes_python.txt'

commits = []
current_commit = None
commits_for_each_author = {}
authors = []
reading_file = open(fname, 'r')
data = reading_file.readlines()
index = 0

# The variable sep looks for lines that have 72 - followed by a new line.  A while loop is used to
# go through the file.  First each commit is parsed and put into a list of commits.  split('|') separates
# the lines by the pipe character, details[1].strip removes the spaces at the end of the word, author not in
# author is used to check if the authors name is already in the list or is it a new author.  Next author[author] = []
# gives the user an empty commit array.
sep = 72*'-' +'\n'
while True:
    try:
        details = data[index + 1].split('|')
        author = details[1].strip()
        if author not in authors:
            authors.append(author)
            commits_for_each_author[author] = []

        # Sets up the revision variable as with author the whitespace is removed.  The commits are added
        # to the list and index is used to find the next index by looking for the 72 hyphons.  The try/except
        # statement is used for catching an IndexError in this case and if that occurs the program will break
        # out of the while loop.
        revision = details[0].strip()
        commits_for_each_author[author].append(revision)
        commits.append(details)
        index = data.index(sep, index + 1)
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