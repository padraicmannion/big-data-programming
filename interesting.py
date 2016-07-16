#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versions = https://github.com/padraicmannion/big-data-programming/commits/master/filechecker.py
#################################################################################################################

# By importing division you can use the python 3.0 version of division instead of floor division.
# The operator library is brought in for later use in iterating over a dictionary to avoid the issue
# of unpacking problems when dealing with key, value pairs.  The math.sqrt is used for getting the deviation.
# Take in a file named changes_python.txt and assign it to the variable fname.
# This opens the file 1 line at a time in read mode.
# The variable sep looks for lines that have 72 - hyphens.
from __future__ import division
import operator
import math
fname = 'changes_python.txt'
data = [line.strip() for line in open(fname, 'r')]
sep = 72*'-'


# Creates a list to hold the commits.  Sets the initialisation value of current_commit to None so the 1st value
# taken in will automatically be taken into the list.  The variable index is initialised at 0.  This variable
# will be used for stepping from one comment to the next.  The dictionary commits_for_each_author is used
# to hold how many commits each author has done and authors is a list that will hold the names of all the authors.
commits = []
current_commit = None
index = 0
commits_for_each_author = {}
authors = []

# 1st a welcome message is displayed to the user and 


# author not in author is used to check if the authors name is already in the list or is it a new author.
# Next author[author] = [] gives the user an empty commit array.
# It sets up the revision variable as with author the whitespace is removed.
# The Interesting things choice.

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


# Reverse is used on the commits list to sort the order.
commits.reverse()


#This prints the number of revisions in the authors list.
# For each author print a message showing how many commits they sent this is done by parsing author as a string and
# str(len(commits_for_each_author[author])) is used to count the number of revisions done by each author and
# print the number of commits next to the authors name.

# An interesting thing is who is the author that made the most commits using max and iteritems function on the
# dictionary commits_for_each_author, the itemgetter constructs a callable that assumes iterable object dictionary as
# input an fetches n-th element out of it.
# ref: http://stackoverflow.com/questions/18595686/how-does-operator-itemgetter-and-sort-work-in-python
# The index [1] [0] holds the authors name and in the next line [1] [1] is used to print another interesting thing
# the revisions that the max author committed to the file.  Next the author count is printed using the len function
# to get the numbers of authors which should be 10.  The next interesting thing is the max_commit variable this says
# out of all the commits how many were made by the person who sent the most commits in this case 45.3%.  The next
# line tells the user out of all other users how much is the contribution in terms of commits which is 54.7%.

# The next interesting thing tells the user who is the minimum in terms of committed at 1.9% of the total
# number of commits.  The min takes apat004 as the lowest value but it's actually murari.krishnan this maybe
# due to using a dictionary instead of a list or an issue caused by the iteritems function.

print commits_for_each_author
for author in commits_for_each_author:
    print str(author) + ' committed ' + str(len(commits_for_each_author[author]))

print 'The person with the most commits is', max(commits_for_each_author.iteritems(), key=operator.itemgetter(1))[0]
print 'The revisions they made were: ', max(commits_for_each_author.iteritems(), key=operator.itemgetter(1))[1]
print 'The Author Count is: ' + str(len(authors))

max_commit = len(max(commits_for_each_author.iteritems(), key=operator.itemgetter(1))[1]) / len(commits)
print round(max_commit, 3),'of the commits were made by', max(commits_for_each_author.iteritems(), key=operator.itemgetter(1))[0]
print 'The other users committed', round(1-max_commit,3), 'out of a total of 1.'
min_commit = len(min(commits_for_each_author.iteritems(), key=operator.itemgetter(1))[0]) / len(commits)
print round(min_commit, 3),'of the commits were made by the least number of committed using the minimum function.'

# The next interesting thing is average in this case 422(number of commits) / 10(number of authors) = 42.2
# is the average.  The variable var is given an initialisation value of 0.  For every author calculate the
# variance by average - how many commits that author made and put that figure to the power of 2.  This
# increments the value in var with each iteration for each author in the file.  When all have been read in
# divide the total number into the number of authors (10) to get 4321.36 which is the variance.  The square root
# of the variance is equal to the standard deviation which is printed on the next line using the math library.
# The standard deviation is 65.737 commits.

average = float((len(commits))) / (len(authors))
print 'The average number of commits per author is', average
var = 0
for author in commits_for_each_author:
    var += (average - len(commits_for_each_author[author])) ** 2
variance = var / len(authors)
print 'The variance is', variance, 'commits squared.'
print 'The standard deviation is', round(math.sqrt(variance),3), 'commits.'



# The print is used to print the number of commits in the file.
# The 2nd print returns how big the file that is read in.
print 'There are',(len(commits)), 'commits in the file.'
print 'The file', fname, 'has', len(data), 'lines.'
